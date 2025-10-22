class Sinhvienpoly:
    def __init__(self, ho_ten, nganh):
        self.__ho_ten = ho_ten
        self.__nganh = nganh
#tinh diem
    def get_diem(self):
        pass
#xep loai hoc luc
    def get_hoc_luc(self):
        if self.get_diem() >= 9 and self.get_diem() <= 10:
            return "Xuat Sac"
        elif self.get_diem() >= 8:
            return "Gioi"
        elif self.get_diem() >= 7:
            return "Kha"
        elif self.get_diem() >= 5:
            return "Trung Binh"
        elif self.get_diem() >= 0:
            return "chua dat"
        else:
            print("diem khong hop le")
        return hoc_luc
def xuat_thong_tin_sv(self):
        print(f"Sinh vien: {self.__ho_ten}, Nganh: {self.__nganh}, Diem: {self.get_diem()}, Hoc luc: {self.get_hoc_luc()}")
#in thong tin sinh vien
def __str__(self):
        return f"Sinh vien: {self.__ho_ten}, Nganh: {self.__nganh}, Diem: {self.get_diem()}, Hoc luc: {self.get_hoc_luc()}"
        
class SinhVienIT(Sinhvienpoly):
    def __init__(self, ho_ten, java, html, css, nganh):
        super().__init__(ho_ten, nganh)
        self.__java = java
        self.__html = html
        self.__css = css           
    
    def get_diem(self):
        return (self.__java * 2 + self.__html + self.__css) / 4
    
class SinhVienBiz(Sinhvienpoly):
    def __init__(self, ho_ten, marketing, sales, nganh):
        super().__init__(ho_ten, nganh)
        self.__marketing = marketing
        self.__sales = sales
    def get_diem(self):
        return (self.__marketing * 2 + self.__sales) / 3
        