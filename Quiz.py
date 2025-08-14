class sinhvien:
    def __init__(self, masv, hoten, toan, ly, hoa):
        self.masv = masv
        self.hoten = hoten
        self.ly = ly
        self.toan = toan
        self.hoa = hoa
    def dtb(self):
        return (self.toan + self.ly + self.hoa) / 3
    def xeploai(self):
        tongdtb = self.dtb()
        if tongdtb > 10:
            return "Điểm không hợp lệ!!"
        elif tongdtb >= 9.0:
            return "Học lực xuất sắc"
        elif tongdtb >= 8.0:
            return "Học lực giỏi"
        elif tongdtb >= 6.5:
            return "Học lực khá"
        elif tongdtb >= 5.0:
            return "Học lực trung bình"
        else:
            return "Học lực yếu"
class qlsv:
    def __init__(self):
        self.dssv = []
    def themsv(self):
        sosv = int(input("Nhập số sinh viên muốn thêm: "))
        for i in range(sosv):
            print(f"Nhập vào sinh viên thứ {i + 1}:")
            masinhvien = int(input("Nhập mã số sinh viên: "))
            hotensv = input("Nhập họ tên sinh viên: ")
            diemtoan = float(input("Nhập điểm Toán: "))
            diemly = float(input("Nhập điểm Lý: "))
            diemhoa = float(input("Nhập điểm Hóa: "))
            sv = sinhvien(masinhvien, hotensv, diemtoan, diemly, diemhoa)
            self.dssv.append(sv)
    def sapxep(self):
        if not self.dssv:
            print("❌ Danh sách trống!")
            return
        n = len(self.dssv)
        for i in range(n - 1):
            max_index = i
            for j in range(i + 1, n):
                if self.dssv[j].dtb() > self.dssv[max_index].dtb():
                    max_index = j
            if max_index != i:
                self.dssv[i], self.dssv[max_index] = self.dssv[max_index], self.dssv[i]
        print("✅ Đã sắp xếp danh sách theo ĐTB giảm dần.")

    def xuat(self):
        if not self.dssv:
            print("❌ Danh sách trống!")
            return
        for sv in self.dssv:
            print(f"MSSV: {sv.masv} -- Họ tên: {sv.hoten} -- Toán: {sv.toan} -- Lý: {sv.ly} -- Hóa: {sv.hoa} -- ĐTB: {sv.dtb():.2f} -- Xếp loại: {sv.xeploai()}")
    def findsv(self):
        if not self.dssv:
            print("❌ Danh sách trống!")
            return
        a = int(input("Nhập MSSV cần tìm kiếm: "))
        for sv in self.dssv:
            if sv.masv == a:
                print(f"MSSV: {sv.masv} -- Họ tên: {sv.hoten} -- Toán: {sv.toan} -- Lý: {sv.ly} -- Hóa: {sv.hoa} -- ĐTB: {sv.dtb():.2f} -- Xếp loại: {sv.xeploai()}")
                return
        return ("❌ Không tìm thấy sinh viên!")

ql = qlsv()
while True:
    print("\n===== MENU QUẢN LÝ SINH VIÊN =====")
    print("1. Thêm sinh viên")
    print("2. Xuất danh sách sinh viên")
    print("3. Sắp xếp theo điểm trung bình")
    print("4. tìm kiếm sinh viên")
    print("5. thoát")
    chon = input("Nhập lựa chọn: ")
    if chon == "1":
        ql.themsv()
    elif chon == "2":
        ql.xuat()
    elif chon == "3":
        ql.sapxep()
    elif chon == "4":
        ql.findsv()
    elif chon == "5":
        print("👋 Tạm biệt!")
        break
    else:
        print("❌ Lựa chọn không hợp lệ! Vui lòng nhập 1-4.")