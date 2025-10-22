import csv
import os
class nhanvien:
    def __init__(self, ma_nv, ten_nv, luong_nv):
        self.ma_nv = ma_nv
        self.ten_nv = ten_nv
        self.luong_nv = luong_nv
    
    def get_thu_nhap(self):
        return self.luong_nv
    def get_loai_nv(self):
        return "hanh chinh"
    def get_thue (self):
        if self.luong_nv < 9000000:
            return self.luong_nv * 0.1
        elif 9000000 <= self.luong_nv <= 15000000:
            return self.luong_nv * 0.12
        else:
            return self.luong_nv * 0.15
    def to_list(self):
        return [self.get_loai_nv(), self.ma_nv, self.ten_nv, str(self.luong_nv), "", "", ""]
    def xuat (self):
        print(f"{self.ma_nv}, {self.ten_nv}, {self.luong_nv}, {self.get_thue()}, {self.get_loai_nv()}, {self.get_thu_nhap()}")
    
class tiepthi (nhanvien):
        def __init__(self, ma_nv, ten_nv, luong_nv, doanh_so, hoa_hong):
            super().__init__(ma_nv, ten_nv, luong_nv)
            self.doanh_so = doanh_so
            self.hoa_hong = hoa_hong
        def get_thu_nhap(self):
            return self.luong_nv + (self.doanh_so * self.hoa_hong / 100)
        def get_loai_nv(self):
            return "tiep thi"
        def to_list(self):
            return [self.get_loai_nv(), self.ma_nv, self.ten_nv, str(self.luong_nv), str(self.doanh_so), str(self.hoa_hong), ""]
        
class truongphong (nhanvien):
        def __init__(self, ma_nv, ten_nv, luong_nv, trach_nhiem):
            super().__init__(ma_nv, ten_nv, luong_nv)
            self.trach_nhiem = trach_nhiem
        def get_thu_nhap(self):
            return self.luong_nv + self.trach_nhiem
        def get_loai_nv(self):
            return "truong phong"
        def to_list(self):
            return [self.get_loai_nv(), self.ma_nv, self.ten_nv, str(self.luong_nv), "", "", str(self.trach_nhiem)]



ds_nv = []

def doc_nhan_vien():
    print("Y2. Đọc thông tin nhân viên từ file và xuất danh sách nhân viên ra màn hình.")
def xoa_nhan_vien_ma():
    print("Y4. Xóa nhân viên theo mã nhập từ bàn phím. Cập nhật file dữ liệu.")
def cap_nhat_nhan_vien_ma():
    print("Y5. Cập nhật thông tin nhân viên theo mã nhập từ bàn phím và ghi thay đổi vào file.")


def nhap_nhan_vien(self):
    while True:
        print("\nChọn loại nhân viên:")
        print("1. Hành chính")
        print("2. Tiếp thị")
        print("3. Trưởng phòng")
        print("0. Kết thúc nhập")
        loai = input("Chọn: ")
        if loai == "0":
            break
        ma_nv = input("Mã NV: ")
        ho_ten = input("Họ tên: ")
        luong = float(input("Lương cơ bản: "))
        if loai == "1":
            nv = nhanvien[ma_nv, ho_ten, luong]
        elif loai == "2":
            doanh_so = float(input("Doanh số bán hàng: "))
            hoa_hong = float(input("Tỉ lệ hoa hồng (%): "))
            nv = tiepthi[ma_nv, ho_ten, luong, doanh_so, hoa_hong]
            ds_nv.append(nv)
        elif loai == "3":
            trach_nhiem = float(input("Lương trách nhiệm: "))
            nv = truongphong[ma_nv, ho_ten, luong, trach_nhiem]
            ds_nv.append(nv)
        else:
            print("Loại nhân viên không hợp lệ!")
            continue
    return self.ds_nv

filename = input ("nhap ten file .csv: ")
file_exist = os.path.exists (filename)
mode = 'a' if file_exist else 'w'
with open (filename, mode, newline='', encoding='utf-8') as file:
    writer = csv.writer (file)
    for nv in ds_nv:
        writer.writerow (nv.to_list())
    print (f"Da luu {len(ds_nv)} nhan vien vao file {filename}")

def tim_nv_ma(self):
        ma_tim = input("Nhập mã nhân viên cần tìm: ")
        for nv in ds_nv:
            if nv.ma_nv == ma_tim:
                nv.xuat()
                return
        print("Không tìm thấy nhân viên với mã đã cho.")
    
def tim_nv_luong(self):
        min_luong = float(input("Nhập mức lương thấp nhất: "))
        max_luong = float(input("Nhập mức lương cao nhất: "))
        for nv in ds_nv:
            if min_luong <= nv.luong_nv <= max_luong:
                nv.xuat()
                found = True
        if not found:
            print("Không có nhân viên nào trong khoảng lương đã cho.")
def sap_xep_ho_ten(self):
        ds_nv.sort(key=lambda nv: nv.ten_nv)
        print("Đã sắp xếp nhân viên theo họ tên.")
        for nv in ds_nv:
            nv.xuat()
def sap_xep_thu_nhap(self):
        ds_nv.sort(key=lambda nv: nv.get_thu_nhap(), reverse=True)
        print("Đã sắp xếp nhân viên theo thu nhập.")
def top_5_thu_nhap(self):
        ds_nv.sort(key=lambda nv: nv.get_thu_nhap(), reverse=True)
        print("Top 5 nhân viên có thu nhập cao nhất:")
        for nv in ds_nv[:5]:
            nv.xuat()

def thoat():
    print("Thoát chương trình.")
