import sinhvienpoly as svpl
class QuanlySinhVien:
    def __init__(self):
        self.danh_sach_sinh_vien = []

    def nhap_danh_sach_sinh_vien(self):
        while True:
            ho_ten = input("Nhap ho ten sinh vien: ")
            nganh = input("Nhap nganh: ")
            if nganh.lower() == "it":
                java = float(input("Nhap diem Java: "))
                html = float(input("Nhap diem HTML: "))
                css = float(input("Nhap diem CSS: "))
                sv = svpl.SinhVienIT(ho_ten, java, html, css, nganh)
                self.danh_sach_sinh_vien.append(sv)
            elif nganh.lower() == "biz":
                marketing = float(input("Nhap diem Marketing: "))
                sales = float(input("Nhap diem Sales: "))
                sv = svpl.SinhVienBiz(ho_ten, marketing, sales, nganh)
                self.danh_sach_sinh_vien.append(sv)
            elif nganh.lower() == "exit":
                break
            else:
                print("Nganh khong hop le. Vui long nhap lai.")
        return self.danh_sach_sinh_vien
    def xuat_danh_sach_sinh_vien(self):
        if not self.danh_sach_sinh_vien:
            print("Danh sach sinh vien trong.")
        else:
            print(f'{"tên sinh vien"}, {"nganh"}, {"diem"}, {"hoc_luc"}')
            for sv in self.danh_sach_sinh_vien:
                sv.xuat_danh_sach_sinh_vien()
    def Xuat_sinh_vien_gioi(self):
        pass
    def sap_xep_sinh_vien_theo_diem(self):
        pass