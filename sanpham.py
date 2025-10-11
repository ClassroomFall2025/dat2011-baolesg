class Sanpham:
    def __init__(self, ten, gia, giam_gia):
        self.__ten = ten
        self.__gia = gia
        self.__giam_gia = giam_gia

    #def dc_giam_gia(self):
    #    return self.__giam_gia
    #def ghi_giam_gia(self, giam_gia_moi):
    #    self.__giam_gia = giam_gia_moi
    #setter, getter ten sp
    def get_ten (self):
        return self.__ten
    def set_ten (self, ten_sp):
        self.__ten = ten_sp
    #setter, getter gia sp
    def get_gia (self):
        return self.__gia
    def set_gia (self, gia):
        self.__gia = gia
    #setter, getter giam gia sp
    def get_giam_gia (self):
        return self.__giam_gia
    def set_giam_gia (self, giam_gia):
        self.__giam_gia = giam_gia
    #nhap thong tin san pham
    def Nhap_thong_tin_sp(self):
        self.__ten = input("Nhập tên sản phẩm: ")
        self.__gia = float(input("Nhập giá sản phẩm: "))
        self.__giam_gia = float(input("Nhập giảm giá sản phẩm: "))
    def thue_nhap_khau(self):
        return self.__gia * 0.1
    def hien_thong_tin(self):
        print(f"Tên san pham: {self.__ten}, Giá: {self.__gia}, Giảm giá: {self.__giam_gia}, Thuế nhập khẩu: {self.thue_nhap_khau()}")
    def __str__(self):
        return f"Tên san pham: {self.__ten}, Giá: {self.__gia}, Giảm giá: {self.__giam_gia}, Thuế nhập khẩu: {self.thue_nhap_khau()}"




