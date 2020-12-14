from ITBooks import db,admin
from sqlalchemy import  Column,Integer,String,Float,Boolean,ForeignKey,Numeric,Date,DateTime,Enum
from sqlalchemy.orm import relationship
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin,current_user
from enum import Enum as UserEnum


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(55), nullable=False)


class TheLoai(db.Model):
    __tablename__ ="TheLoai"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nametl = Column(String(55), nullable=False)
    sach_tl = relationship('Sach', backref='theloai', lazy=True)

    def __str__(self):
        return self.nametl


class TacGia(db.Model):
    __tablename__ ="TacGia"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nametg = Column(String(55), nullable=False)
    sach_tg = relationship('Sach', backref='tacgia', lazy=True)

    def __str__(self):
        return self.nametg



class Sach(BaseModel):
    __tablename__ = "Sach"
    donGia = Column(Numeric, nullable=False)
    avatar = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    theLoai_id = Column(Integer, ForeignKey(TheLoai.id), nullable=False)
    tacGia_id = Column(Integer, ForeignKey(TacGia.id), nullable=False)
    baoCaoTon_id = relationship('BaoCaoTon', backref="sach",lazy = True)
    phieuNhap_id = relationship('ChiTietPhieuNhap', backref='sach', lazy=True)
    ctHoaDon_id = relationship('ChiTietHoaDon', backref='sach', lazy=True)
    soluongSach_id = relationship("SoLuongSach", backref='sach', lazy=True)

    def __str__(self):
        return self.name


class SoLuongSach(db.Model):
    __tablename__ = "soluongsach"
    sach_id = Column(Integer, ForeignKey(Sach.id), primary_key=True, nullable=False)
    soLuong = Column(Integer, nullable=False)

'''
Nhan Vien voi khách hàng có quyền đăng nhập , Trong nhân viên gồm có Admin và nhân viên quản lý bằng UserRole.
'''
class UserRole(UserEnum):
    KH = 1
    USER = 2
    ADMIN = 3


class User(BaseModel, UserMixin):
    email = Column(String(50))
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100))
    active = Column(Boolean, default=True)
    user_role = Column(Enum(UserRole), default=UserRole.KH)
    qd = relationship('QuyDinh', backref="User", lazy= True)

    def __unicode__(self):
        return self.username

    def is_anonymous(self):
        return False


class QuyDinh(db.Model):
    __tablename__ = "quydinh"
    id = Column(Integer, nullable=False, default=1)
    id_user = Column(Integer, ForeignKey(User.id),primary_key=True, nullable=False)
    quydinhnhap = Column(Integer, nullable=True, default= 150)
    luongtonlon = Column(Integer, nullable=True, default= 300)
    luongtonnho = Column(Integer, nullable=True, default=20)
    tienno = Column(Numeric, nullable=True, default=20000 )
    active = Column(Boolean, default=True)


class NhanVien(BaseModel):
    __tablename__ ="NhanVien"
    email = Column(String(50), nullable=False)
    ngaySinh = Column(Date, nullable=False)
    diaChi = Column(String(100), nullable=False)
    cmnd = Column(String(15),nullable=False)
    hd = relationship('HoaDon', backref="nhanvien", lazy=True)

    def __str__(self):
        return self.name


class KhachHang(BaseModel):
    __tablename__ ="KhachHang"
    diaChi = Column(String(250), nullable=False)
    dienThoai = Column(String(15), nullable=False)
    email = Column(String(50), nullable=False)
    hd = relationship('HoaDon', backref='KhachHang', lazy=True)
    pttn = relationship('PhieuThuTienNo', backref='khachhang', lazy=True)
    tienNo = relationship('KhachHangNo', backref='khachhang', lazy=True)
    congNo = relationship('BaoCaoCongNo', backref='khachhang', lazy=True)

    def __str__(self):
        return self.name


class BaoCaoTon(db.Model):
    __tablename__ = "BaoCaoTon"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tonDau = Column(Numeric, nullable=False)
    phatSinh = Column(Numeric, nullable=False)
    tonCuoi = Column(Numeric, nullable=False)
    ms = Column(Integer, ForeignKey(Sach.id),nullable=False)


class HoaDon(db.Model):
    __tablename__ = "HoaDon"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ngayLapHD = Column(DateTime, nullable=False)
    khachHang_id = Column(Integer, ForeignKey(KhachHang.id), nullable=False)
    nhanVien_id = Column(Integer, ForeignKey(NhanVien.id), nullable=False)
    cthd = relationship('ChiTietHoaDon', backref = 'hoadon', lazy=True)

    def __repr__(self):
        return repr(self.id)


class ChiTietHoaDon(db.Model):
    __tablename__ = "ChiTietHoaDon"
    soLuong = Column(Integer, nullable=False)
    donGia = Column(Numeric, nullable=False)
    thanhTien = Column(Numeric, nullable=False)
    hoaDon_id = Column(Integer, ForeignKey(HoaDon.id), primary_key=True, nullable=False)
    sach_id = Column(Integer, ForeignKey(Sach.id), primary_key=True, nullable=False)

    def __repr__(self) -> str:
        '''
        :return: lấy ra được id 1 thay vi` <phieunhapsach 1>
        '''
        return repr(self.hoaDon_id)

class PhieuNhapSach(db.Model):
    __tablename__ = "PhieuNhap"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ngayNhap = Column(DateTime, nullable=False)
    ctpn = relationship('ChiTietPhieuNhap', backref='phieunhap', lazy=True)

    def __repr__(self) -> str:
        '''
        :return: lấy ra được id 1 thay vi` <phieunhapsach 1>
        '''
        return repr(self.id)


class ChiTietPhieuNhap(db.Model):
    __tablename__ = "ChiTietPhieuNhap"
    soLuong = Column(Integer, nullable=False)
    phieuNhap_id = Column(Integer, ForeignKey(PhieuNhapSach.id), primary_key=True, nullable=False)
    sach_id = Column(Integer, ForeignKey(Sach.id), primary_key=True, nullable=False)


    def __repr__(self) -> str:
        '''
        :return: lấy ra được id 1 thay vi` <phieunhapsach 1>
        '''
        return repr(self.phieuNhap_id)


class PhieuThuTienNo(db.Model):
    __tablename__ = "PhieuThuTienNo"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ngayThu = Column(DateTime, nullable=False)
    soTien = Column(Numeric, nullable=False)
    khachHang_id = Column(Integer, ForeignKey(KhachHang.id), nullable=False)


class BaoCaoCongNo(db.Model):
    __tablename__ = "BaoCaoCongNo"
    id = Column(Integer, primary_key=True,autoincrement=True)
    thang = Column(Date, nullable=False)
    noDau = Column(Numeric, nullable=False)
    phatSinh = Column(Numeric, nullable=False)
    khachHang_id = Column(Integer, ForeignKey(KhachHang.id), nullable=False)


class KhachHangNo(db.Model):
    __tablename__ = "KhachHangNo"
    ngayNo = Column(Date,nullable=False)
    soTien = Column(Numeric, nullable=False)
    khachHang_id = Column(Integer, ForeignKey(KhachHang.id), primary_key=True, nullable=False)


if __name__ == '__main__':
    db.create_all()