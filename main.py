import sys
import pyperclip

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import hoanvi
import tusinh
import hill
import affine
import vigenere
import dich_vong


class Window(QWidget):
    def __init__(self):
        self.n = 26

        super().__init__()
        self.resize(1200, 900)
        self.setWindowTitle("Pham Van Cuong - Ma hoa - Giai Ma")

        self.UI()

    def UI(self):
        self.onlyInt = QIntValidator()

        self.font = QFont()
        self.font.setFamily("Arial")
        self.font.setPointSize(20)

        self.z26 = QRadioButton("Z26", self)
        self.z26.move(10, 10)
        self.z26.setChecked(True)
        self.z26.clicked.connect(self.changeToZ26)

        self.unicode = QRadioButton("UTF-8", self)
        self.unicode.move(110, 10)
        self.unicode.clicked.connect(self.changeToUtf8)

        self.ui_dich_vong()
        self.ui_vigine()
        self.ui_tusinh()
        self.ui_affine()
        self.ui_hill()
        self.ui_hoanvi()

    def ui_dich_vong(self):
        x_pos = 100
        y_pos = 150

        self.labelDichVong = QLabel("Dịch Vòng", self)
        self.labelDichVong.move(x_pos, y_pos - 70)
        self.labelDichVong.setFont(self.font)

        self.banRoDichVong = QLineEdit(self)
        self.banRoDichVong.move(x_pos - 50, y_pos)
        self.banRoDichVong.resize(300, 40)
        self.banRoDichVong.setPlaceholderText("Bản rõ")

        self.banMaDichVong = QLineEdit(self)
        self.banMaDichVong.move(x_pos - 50, y_pos + 50)
        self.banMaDichVong.resize(300, 40)
        self.banMaDichVong.setPlaceholderText("Bản mã")

        self.khoaDichVong = QLineEdit(self)
        self.khoaDichVong.move(x_pos - 50, y_pos + 100)
        self.khoaDichVong.resize(300, 40)
        self.khoaDichVong.setPlaceholderText("Khóa(int)")
        self.khoaDichVong.setValidator(self.onlyInt)

        self.maHoaDichVong = QPushButton("Mã hóa", self)
        self.maHoaDichVong.move(x_pos - 50, y_pos + 150)
        self.maHoaDichVong.clicked.connect(self.dich_vong_encode)

        self.giaMaDichVong = QPushButton("Giải mã", self)
        self.giaMaDichVong.move(x_pos + 110, y_pos + 150)
        self.giaMaDichVong.clicked.connect(self.dich_vong_decode)

        self.ketQuaDichVong = QLabel("Kết quả:", self)
        self.ketQuaDichVong.resize(300, 40)
        self.ketQuaDichVong.move(x_pos - 50, y_pos + 200)
        self.ketQuaDichVong.setTextInteractionFlags(Qt.TextSelectableByMouse)

    def dich_vong_encode(self):
        ban_ro = self.banRoDichVong.text()
        khoa = int(self.khoaDichVong.text())
        print(ban_ro)

        ban_ma = dich_vong.encode(ban_ro, khoa, self.n)
        self.ketQuaDichVong.setText(f"Kết quả: {ban_ma}")
        print(ban_ma)

    def dich_vong_decode(self):
        ban_ma = self.banMaDichVong.text()
        khoa = int(self.khoaDichVong.text())
        ban_ro = dich_vong.decode(ban_ma, khoa, self.n)
        self.ketQuaDichVong.setText(f"Kết quả: {ban_ro}")

    def ui_vigine(self):
        x_pos = 500
        y_pos = 150

        self.labelVigenere = QLabel("Vigenere", self)
        self.labelVigenere.move(x_pos, y_pos - 70)
        self.labelVigenere.setFont(self.font)

        self.banRoVigenere = QLineEdit(self)
        self.banRoVigenere.move(x_pos - 50, y_pos)
        self.banRoVigenere.resize(300, 40)
        self.banRoVigenere.setPlaceholderText("Bản rõ")

        self.banMaVigenere = QLineEdit(self)
        self.banMaVigenere.move(x_pos - 50, y_pos + 50)
        self.banMaVigenere.resize(300, 40)
        self.banMaVigenere.setPlaceholderText("Bản mã")

        self.khoaVigenere = QLineEdit(self)
        self.khoaVigenere.move(x_pos - 50, y_pos + 100)
        self.khoaVigenere.resize(300, 40)
        self.khoaVigenere.setPlaceholderText("Khóa(str)")

        self.maHoaVigenere = QPushButton("Mã hóa", self)
        self.maHoaVigenere.move(x_pos - 50, y_pos + 150)
        self.maHoaVigenere.clicked.connect(self.vigenere_encode)

        self.giaMaVigenere = QPushButton("Giải mã", self)
        self.giaMaVigenere.move(x_pos + 110, y_pos + 150)
        self.giaMaVigenere.clicked.connect(self.vigenere_decode)

        self.ketQuaVigenere = QLabel("Kết quả:", self)
        self.ketQuaVigenere.resize(300, 40)
        self.ketQuaVigenere.move(x_pos - 50, y_pos + 200)
        self.ketQuaVigenere.setTextInteractionFlags(Qt.TextSelectableByMouse)

    def vigenere_encode(self):
        ban_ro = self.banRoVigenere.text()
        khoa = self.khoaVigenere.text()

        ban_ma = vigenere.encode(ban_ro, khoa, self.n)
        self.ketQuaVigenere.setText(f"Kết quả: {ban_ma}")

    def vigenere_decode(self):
        ban_ma = self.banMaVigenere.text()
        khoa = self.khoaVigenere.text()
        ban_ro = vigenere.decode(ban_ma, khoa, self.n)
        self.ketQuaVigenere.setText(f"Kết quả: {ban_ro}")

    def ui_tusinh(self):
        x_pos = 900
        y_pos = 150

        self.labelTusinh = QLabel("Tự Sinh", self)
        self.labelTusinh.move(x_pos, y_pos - 70)
        self.labelTusinh.setFont(self.font)

        self.banRoTusinh = QLineEdit(self)
        self.banRoTusinh.move(x_pos - 50, y_pos)
        self.banRoTusinh.resize(300, 40)
        self.banRoTusinh.setPlaceholderText("Bản rõ")

        self.banMaTusinh = QLineEdit(self)
        self.banMaTusinh.move(x_pos - 50, y_pos + 50)
        self.banMaTusinh.resize(300, 40)
        self.banMaTusinh.setPlaceholderText("Bản mã")

        self.khoaTusinh = QLineEdit(self)
        self.khoaTusinh.move(x_pos - 50, y_pos + 100)
        self.khoaTusinh.resize(300, 40)
        self.khoaTusinh.setPlaceholderText("Khóa(int)")
        self.khoaTusinh.setValidator(self.onlyInt)

        self.maHoaTusinh = QPushButton("Mã hóa", self)
        self.maHoaTusinh.move(x_pos - 50, y_pos + 150)
        self.maHoaTusinh.clicked.connect(self.tusinh_encode)

        self.giaMaTusinh = QPushButton("Giải mã", self)
        self.giaMaTusinh.move(x_pos + 110, y_pos + 150)
        self.giaMaTusinh.clicked.connect(self.tusinh_decode)

        self.ketQuaTusinh = QLabel("Kết quả:", self)
        self.ketQuaTusinh.resize(300, 40)
        self.ketQuaTusinh.move(x_pos - 50, y_pos + 200)
        self.ketQuaTusinh.setTextInteractionFlags(Qt.TextSelectableByMouse)

    def tusinh_encode(self):
        ban_ro = self.banRoTusinh.text()
        khoa = int(self.khoaTusinh.text())

        ban_ma = tusinh.encode(ban_ro, khoa, self.n)
        self.ketQuaTusinh.setText(f"Kết quả: {ban_ma}")

    def tusinh_decode(self):
        ban_ma = self.banMaTusinh.text()
        khoa = int(self.khoaTusinh.text())
        ban_ro = tusinh.decode(ban_ma, khoa, self.n)
        self.ketQuaTusinh.setText(f"Kết quả: {ban_ro}")

    def ui_affine(self):
        x_pos = 100
        y_pos = 500

        self.labelAffine = QLabel("Affine", self)
        self.labelAffine.move(x_pos, y_pos - 70)
        self.labelAffine.setFont(self.font)

        self.banRoAffine = QLineEdit(self)
        self.banRoAffine.move(x_pos - 50, y_pos)
        self.banRoAffine.resize(300, 40)
        self.banRoAffine.setPlaceholderText("Bản rõ")

        self.banMaAffine = QLineEdit(self)
        self.banMaAffine.move(x_pos - 50, y_pos + 50)
        self.banMaAffine.resize(300, 40)
        self.banMaAffine.setPlaceholderText("Bản mã")

        self.khoaAffineA = QLineEdit(self)
        self.khoaAffineA.move(x_pos - 50, y_pos + 100)
        self.khoaAffineA.resize(130, 40)
        self.khoaAffineA.setPlaceholderText("Khóa a(int)")
        self.khoaAffineA.setValidator(self.onlyInt)

        self.khoaAffineB = QLineEdit(self)
        self.khoaAffineB.move(x_pos + 120, y_pos + 100)
        self.khoaAffineB.resize(130, 40)
        self.khoaAffineB.setPlaceholderText("Khóa b(int)")
        self.khoaAffineB.setValidator(self.onlyInt)

        self.maHoaAffine = QPushButton("Mã hóa", self)
        self.maHoaAffine.move(x_pos - 50, y_pos + 150)
        self.maHoaAffine.clicked.connect(self.affine_encode)

        self.giaMaAffine = QPushButton("Giải mã", self)
        self.giaMaAffine.move(x_pos + 110, y_pos + 150)
        self.giaMaAffine.clicked.connect(self.affine_decode)

        self.ketQuaAffine = QLabel("Kết quả:", self)
        self.ketQuaAffine.resize(300, 40)
        self.ketQuaAffine.move(x_pos - 50, y_pos + 200)
        self.ketQuaAffine.setTextInteractionFlags(Qt.TextSelectableByMouse)

    def affine_encode(self):
        ban_ro = self.banRoAffine.text()
        khoa_a = int(self.khoaAffineA.text())
        khoa_b = int(self.khoaAffineB.text())

        ban_ma = affine.encode(ban_ro, (khoa_a, khoa_b), self.n)
        self.ketQuaAffine.setText(f"Kết quả: {ban_ma}")

    def affine_decode(self):
        ban_ma = self.banMaAffine.text()
        khoa_a = int(self.khoaAffineA.text())
        khoa_b = int(self.khoaAffineB.text())

        ban_ro = affine.decode(ban_ma, (khoa_a, khoa_b), self.n)
        self.ketQuaAffine.setText(f"Kết quả: {ban_ro}")

    def ui_hill(self):
        x_pos = 500
        y_pos = 500

        self.labelHill = QLabel("Hill", self)
        self.labelHill.move(x_pos, y_pos - 70)
        self.labelHill.setFont(self.font)

        self.banRoHill = QLineEdit(self)
        self.banRoHill.move(x_pos - 50, y_pos)
        self.banRoHill.resize(300, 40)
        self.banRoHill.setPlaceholderText("Bản rõ")

        self.banMaHill = QLineEdit(self)
        self.banMaHill.move(x_pos - 50, y_pos + 50)
        self.banMaHill.resize(300, 40)
        self.banMaHill.setPlaceholderText("Bản mã")

        self.khoaHillK00 = QLineEdit(self)
        self.khoaHillK00.move(x_pos - 50, y_pos + 100)
        self.khoaHillK00.resize(130, 40)
        self.khoaHillK00.setPlaceholderText("K00(int)")
        self.khoaHillK00.setValidator(self.onlyInt)

        self.khoaHillK01 = QLineEdit(self)
        self.khoaHillK01.move(x_pos + 110, y_pos + 100)
        self.khoaHillK01.resize(130, 40)
        self.khoaHillK01.setPlaceholderText("K01(int)")
        self.khoaHillK01.setValidator(self.onlyInt)

        self.khoaHillK10 = QLineEdit(self)
        self.khoaHillK10.move(x_pos - 50, y_pos + 150)
        self.khoaHillK10.resize(130, 40)
        self.khoaHillK10.setPlaceholderText("K10(int)")
        self.khoaHillK10.setValidator(self.onlyInt)

        self.khoaHillK11 = QLineEdit(self)
        self.khoaHillK11.move(x_pos + 110, y_pos + 150)
        self.khoaHillK11.resize(130, 40)
        self.khoaHillK11.setPlaceholderText("K11(int)")
        self.khoaHillK11.setValidator(self.onlyInt)

        self.maHoaHill = QPushButton("Mã hóa", self)
        self.maHoaHill.move(x_pos - 50, y_pos + 200)
        self.maHoaHill.clicked.connect(self.hill_encode)

        self.giaMaHill = QPushButton("Giải mã", self)
        self.giaMaHill.move(x_pos + 110, y_pos + 200)
        self.giaMaHill.clicked.connect(self.hill_decode)

        self.ketQuaHill = QLabel("Kết quả:", self)
        self.ketQuaHill.resize(300, 40)
        self.ketQuaHill.move(x_pos - 50, y_pos + 250)
        self.ketQuaHill.setTextInteractionFlags(Qt.TextSelectableByMouse)

    def hill_encode(self):
        ban_ro = self.banRoHill.text()
        k00 = int(self.khoaHillK00.text())
        k01 = int(self.khoaHillK01.text())
        k10 = int(self.khoaHillK10.text())
        k11 = int(self.khoaHillK11.text())

        ban_ma = hill.encode(ban_ro, (k00, k01, k10, k11), self.n)
        self.ketQuaHill.setText(f"Kết quả: {ban_ma}")
        pyperclip.copy(ban_ma)

    def hill_decode(self):
        ban_ma = self.banMaHill.text()
        k00 = int(self.khoaHillK00.text())
        k01 = int(self.khoaHillK01.text())
        k10 = int(self.khoaHillK10.text())
        k11 = int(self.khoaHillK11.text())

        ban_ro = hill.decode(ban_ma, (k00, k01, k10, k11), self.n)
        self.ketQuaHill.setText(f"Kết quả: {ban_ro}")

    def ui_hoanvi(self):
        x_pos = 900
        y_pos = 500

        self.labelHoanVi = QLabel("Hoán Vị", self)
        self.labelHoanVi.move(x_pos, y_pos - 70)
        self.labelHoanVi.setFont(self.font)

        self.banRoHoanVi = QLineEdit(self)
        self.banRoHoanVi.move(x_pos - 50, y_pos)
        self.banRoHoanVi.resize(300, 40)
        self.banRoHoanVi.setPlaceholderText("Bản rõ")

        self.banMaHoanVi = QLineEdit(self)
        self.banMaHoanVi.move(x_pos - 50, y_pos + 50)
        self.banMaHoanVi.resize(300, 40)
        self.banMaHoanVi.setPlaceholderText("Bản mã")

        self.khoaHoanVi = QLineEdit(self)
        self.khoaHoanVi.move(x_pos - 50, y_pos + 100)
        self.khoaHoanVi.resize(300, 40)
        self.khoaHoanVi.setPlaceholderText("Khóa(int)")
        self.khoaHoanVi.setValidator(self.onlyInt)

        self.maHoaHoanVi = QPushButton("Mã hóa", self)
        self.maHoaHoanVi.move(x_pos - 50, y_pos + 150)
        self.maHoaHoanVi.clicked.connect(self.hoanvi_encode)

        self.giaMaHoanVi = QPushButton("Giải mã", self)
        self.giaMaHoanVi.move(x_pos + 110, y_pos + 150)
        self.giaMaHoanVi.clicked.connect(self.hoanvi_decode)

        self.ketQuaHoanVi = QLabel("Kết quả:", self)
        self.ketQuaHoanVi.resize(300, 40)
        self.ketQuaHoanVi.move(x_pos - 50, y_pos + 200)
        self.ketQuaHoanVi.setTextInteractionFlags(Qt.TextSelectableByMouse)

    def hoanvi_encode(self):
        ban_ro = self.banRoHoanVi.text()
        khoa = int(self.khoaHoanVi.text())
        print(ban_ro)

        ban_ma = hoanvi.encode(ban_ro, khoa, self.n)
        self.ketQuaHoanVi.setText(f"Kết quả: {ban_ma}")
        print(ban_ma)

    def hoanvi_decode(self):
        ban_ma = self.banMaHoanVi.text()
        khoa = int(self.khoaHoanVi.text())
        ban_ro = hoanvi.decode(ban_ma, khoa, self.n)
        self.ketQuaHoanVi.setText(f"Kết quả: {ban_ro}")

    def changeToZ26(self):
        print("z26")
        self.n = 26

    def changeToUtf8(self):
        print("utf-8")
        self.n = 1112064


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
