from ITBooks import  db,admin
from flask_admin.contrib.sqla import ModelView
from ITBooks.models import  Sach , TheLoai ,TacGia, PhieuNhapSach ,ChiTietPhieuNhap ,\
    BaoCaoTon , BaoCaoCongNo , NhanVien , KhachHang , KhachHangNo , HoaDon, ChiTietHoaDon , PhieuThuTienNo, UserRole, User,SoLuongSach
from flask_admin import BaseView, expose
from flask_login import  current_user, logout_user
from  flask  import redirect,request, url_for


class ContactView(BaseView):
    @expose('/')
    def __index__(self):
        return self.render('admin/contact.html')


class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')

    def is_accessible(self):
            return current_user.is_authenticated



#class can phai dang nhap
class Authenticated(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        '''
         chưa test thử cái chức năng này
        :param name:
        :param kwargs:
        :return:
        '''
        # redirect to login page if user doesn't have access
        return redirect(url_for('admin/login', next=request.url))



class ChiTietPhieuNhapModelView(Authenticated):
    column_display_pk = True
    can_view_details = True


class SoLuongSachModelView(Authenticated):
    column_display_pk = True


class TacGiaModelView(Authenticated):
    column_display_pk =  True
    can_view_details = True


class SachModelView(Authenticated):
    column_display_pk = True


class TheLoaiModelView(Authenticated):
    can_view_details = True


class PhieuNhapSachModelView(Authenticated):
    column_display_pk = True

    def __repr__(self):
        return repr(self.id)



class NhanVienModelView(ModelView):
    column_display_pk = True

    def is_accessible(self):
        user = User.query.filter(User.user_role == "ADMIN").first()
        if current_user == user:
            return current_user.is_authenticated



class BaoCaoTonModelView(Authenticated):
    column_display_pk = True


class BaoCaoCongNoModelView(Authenticated):
    column_display_pk = True


class KhachHangModelView(Authenticated):
    column_display_pk = True


class KhachHangNoModelView(Authenticated):
    column_display_pk = True


class HoaDonModelView(Authenticated):
    column_display_pk = True


class ChiTietHoaDonModelView(Authenticated):
    column_display_pk = True


class PhieuThuNoModelView(Authenticated):
    column_display_pk = True


admin.add_view(NhanVienModelView(NhanVien, db.session, name="Nhân Viên"))

admin.add_view(KhachHangModelView(KhachHang, db.session, name='Khách Hàng'))

admin.add_view(KhachHangNoModelView(KhachHangNo, db.session, name= 'Khách Hàng Nợ'))

admin.add_view(TacGiaModelView(TacGia, db.session, name= 'Tác Giả'))

admin.add_view(TheLoaiModelView(TheLoai, db.session, name='Thể Loại'))

admin.add_view(SachModelView(Sach, db.session, name='Sách'))

admin.add_view(PhieuNhapSachModelView(PhieuNhapSach, db.session, name ="Phiếu Nhập Sách"))

admin.add_view(ChiTietPhieuNhapModelView(ChiTietPhieuNhap, db.session, name="Nhập Sách"))

admin.add_view(HoaDonModelView(HoaDon, db.session, name= 'Hóa Đơn'))

admin.add_view(ChiTietHoaDonModelView(ChiTietHoaDon, db.session, name='Chi Tiết Hóa Đơn'))

admin.add_view(PhieuThuNoModelView(PhieuThuTienNo, db.session, name="Phiếu Thu Nợ"))

admin.add_view(BaoCaoTonModelView(BaoCaoTon, db.session, name='Báo Cáo Tồn'))

admin.add_view(BaoCaoCongNoModelView(BaoCaoCongNo, db.session, name='Báo Cáo Công Nợ'))

admin.add_view(ContactView(name='Lien He'))

admin.add_view(LogoutView(name='Log Out'))

admin.add_view(SoLuongSachModelView(SoLuongSach, db.session, name="Số Lượng"))
