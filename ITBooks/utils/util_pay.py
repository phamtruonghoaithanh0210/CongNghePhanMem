
from ITBooks.models import  HoaDon, ChiTietHoaDon, PhieuNhapSach, ChiTietPhieuNhap,Sach, SoLuongSach, TheLoai, TacGia, KhachHangNo, KhachHang,  QuyDinh,User
from ITBooks import  db
from flask_login import current_user
from datetime import datetime


def cart_stats(cart):
    total_amount, total_quantity = 0, 0
    if cart:
        for p in cart.values():
            total_quantity = total_quantity + p["quantity"]
            total_amount = total_amount + p["quantity"]*p["donGia"]

    return total_quantity, total_amount


def add_receipt(cart):
    if cart and current_user.is_authenticated:
        hoadon = HoaDon(khachHang_id=current_user.id,
                        nhanVien_id = 1,
                        ngayLapHD = datetime.now())
        db.session.add(hoadon)

        for p in list(cart.values()):
            detail = ChiTietHoaDon(hoadon=hoadon,
                                   sach_id=int(p["id"]),
                                   soLuong=p["quantity"],
                                   donGia=p["donGia"],
                                   thanhTien=p["donGia"] * p["quantity"])
            db.session.add(detail)
        try:
            db.session.commit()
            return True
        except Exception as ex:
            print(ex)
    return False


def nhap_sach(ngaynhap, idsach , soluong):

    sach = Sach.query.get(idsach)
    p = sach.id

    sls = SoLuongSach.query.filter(p == SoLuongSach.sach_id).first()
    qd = QuyDinh.query.filter(QuyDinh.id == 1).first()
    t = qd.quydinhnhap
    y = qd.luongtonlon
    if sls is None:
        sl = 0
    else:
        sl = sls.soLuong
    if sl <= int(y) and int(soluong) <= int(t):
        phieunhap = PhieuNhapSach(ngayNhap=ngaynhap)
        db.session.add(phieunhap)
        detail = ChiTietPhieuNhap(phieunhap = phieunhap,
                                soLuong=soluong,
                                  sach_id = idsach)
        db.session.add(detail)
        SoLuongSach.query.filter(p == SoLuongSach.sach_id).delete()
        soluongsach = SoLuongSach(sach_id = idsach,
                                      soLuong = sl + int(soluong))
        db.session.add(soluongsach)
        try:
            db.session.commit()
            return True
        except Exception as ex:
            print(ex)
    return False


def  thu_tien_no(ngaynhap, idkhach, sotien):
    khn = KhachHangNo.query.filter(KhachHangNo.khachHang_id == idkhach).first()
    qd = QuyDinh.query.filter(QuyDinh.id == 1).first()
    if qd.active:
        active = 1
    else:
        active = 0
    if khn is None:
        return  False
    else:
        tienno = khn.soTien
    if int(sotien) <= int(tienno):
        if int(sotien) == int(tienno):
            KhachHangNo.query.filter(idkhach == KhachHangNo.khachHang_id).delete()
        else:
            tiennomoi = int(tienno) - int(sotien)
            KhachHangNo.query.filter(idkhach == KhachHangNo.khachHang_id).delete()
            khno = KhachHangNo(khachHang_id = idkhach,
                              soTien=tiennomoi,
                              ngayNo=ngaynhap)
            db.session.add(khno)
    elif int(sotien) > int(tienno) and active == 0:
        KhachHangNo.query.filter(idkhach == KhachHangNo.khachHang_id).delete()
        tienthua = int(sotien) - int(tienno)
    else:
        return  False
    try:
        db.session.commit()
        return True
    except Exception as ex:
        print(ex)
    return False



def thay_doi_quy_dinh(iduser, nhaptoithieu, tontoithieunhap, tontoithieuban, tiennotoida, check):
    t = User.query.filter(iduser == User.id).first()
    if iduser is None:
        id = current_user.id
    else:
        id = t.id
    if QuyDinh.query.count() == 1:
        QuyDinh.query.filter(QuyDinh.id_user).delete()
    if check :
        check = 1
    else:
        check = 0
    quydinh = QuyDinh(id_user= id,
                      quydinhnhap=nhaptoithieu,
                      luongtonlon=tontoithieunhap,
                      luongtonnho=tontoithieuban,
                      tienno=tiennotoida,
                      active =check)
    db.session.add(quydinh)
    try:
        db.session.commit()
        return True
    except Exception as ex:
        print(ex)
    return False
