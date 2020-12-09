from ITBooks import db, app
from ITBooks.models import  Sach,TheLoai,TacGia
import os, json


def read_books(keyword=None, from_price=None, to_price=None, theloai = None):
    '''

    :param keyword: từ khóa cần tìm kiếm
    :param from_price:  tìm từ khoảng giá
    :param to_price: tới giá .
    :return: trả về sách đạt các yêu cầu
    '''
    books = Sach.query.join(TheLoai, Sach.theLoai_id==TheLoai.id).join(TacGia, Sach.tacGia_id == TacGia.id)\
            .add_columns(Sach.avatar,Sach.id, Sach.name,Sach.donGia, TheLoai.nametl,TacGia.nametg)

    if keyword:
        books = books.filter(Sach.name.contains(keyword))

    if theloai:
        books = books.filter(TheLoai.nametl.like(theloai))

    if from_price and to_price:
        books = books.filter(Sach.donGia.__gt__(from_price),
                             Sach.donGia.__lt__(to_price))

    return books.all()


def read_books_by_id(book_id):
    return Sach.query.get(book_id)


def read_theloai():
    return TheLoai.query.all()


def read_books_by_theloai(theloai_id):
    return TheLoai.query.get(theloai_id).books