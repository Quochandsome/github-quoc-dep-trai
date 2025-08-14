class SinhVien:
    def __init__(self, masv, hoten, toan, ly, hoa):
        self.masv = masv
        self.hoten = hoten
        self.toan = toan
        self.ly = ly
        self.hoa = hoa

    def dtb(self):
        return (self.toan + self.ly + self.hoa) / 3

    def xeploai(self):
        tongdtb = self.dtb()
        if tongdtb >= 9.0:
            return "Xuất sắc"
        elif tongdtb >= 8.0:
            return "Giỏi"
        elif tongdtb >= 6.5:
            return "Khá"
        elif tongdtb >= 5.0:
            return "Trung bình"
        else:
            return "Yếu"


class QuanLySinhVien:
    def __init__(self):
        self.dssv = []

    def themsv(self):
        sosv = int(input("Nhập số sinh viên muốn thêm: "))
        for i in range(sosv):
            print(f"\nNhập sinh viên thứ {i + 1}:")
            masv = input("Mã SV: ")
            hoten = input("Họ tên: ")
            toan = float(input("Điểm Toán: "))
            ly = float(input("Điểm Lý: "))
            hoa = float(input("Điểm Hóa: "))
            sv = SinhVien(masv, hoten, toan, ly, hoa)
            self.dssv.append(sv)
        print("✅ Thêm sinh viên thành công!")

    def xuat(self):
        if not self.dssv:
            print("❌ Danh sách trống!")
            return
        for sv in self.dssv:
            print(f"MSSV: {sv.masv} | Họ tên: {sv.hoten} | "
                  f"Toán: {sv.toan} | Lý: {sv.ly} | Hóa: {sv.hoa} | "
                  f"ĐTB: {sv.dtb():.2f} | Xếp loại: {sv.xeploai()}")

    def sapxep(self):
        self.dssv.sort(key=lambda sv: sv.dtb(), reverse=True)
        print("✅ Đã sắp xếp danh sách theo ĐTB giảm dần.")


# ====================== CHẠY MENU ======================

ql = QuanLySinhVien()

while True:
    print("\n===== MENU QUẢN LÝ SINH VIÊN =====")
    print("1. Thêm sinh viên")
    print("2. Xuất danh sách sinh viên")
    print("3. Sắp xếp theo điểm trung bình")
    print("4. Thoát")
    chon = input("Nhập lựa chọn: ")

    if chon == "1":
        ql.themsv()
    elif chon == "2":
        ql.xuat()
    elif chon == "3":
        ql.sapxep()
    elif chon == "4":
        print("👋 Tạm biệt!")
        break
    else:
        print("❌ Lựa chọn không hợp lệ! Vui lòng nhập 1-4.")
