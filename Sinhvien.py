class sinhvien:
    def __init__(self, ten, namsinh,diem_mon):
        self.ten = ten
        self.namsinh = namsinh
        self.diem_mon = diem_mon
    def Nhap_thong_tin_sv(self):
        print(f"sinh vien: {self.ten}, nam sinh: {self.namsinh}, diem mon: {self.diem_mon}")
    def __str__(self):
        return f"sinh vien: {self.ten}, nam sinh: {self.namsinh}, diem mon: {self.diem_mon}"

class sinhvienXLDL(sinhvien):
    def __init__(self, ten, namsinh, diem_mon, Lap_trinh):
        super().__init__(ten, namsinh, diem_mon)
        self.Lap_trinh = Lap_trinh

    def Nhap_thong_tin_sv(self):
        print(f"{sinhvien.__str__(self)} va lap trinh: {self.Lap_trinh}")
    def __str__(self):
        return f"{super().__str__()} va lap trinh: {self.Lap_trinh}"
    
sv1 = sinhvienXLDL("Nguyen Van A", 2000, 8.5, "Python")
print(sv1)
