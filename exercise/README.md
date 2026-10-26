# Python Journey - Exercise Week 13 va Week 14

Tai lieu nay huong dan chay cac bai tap Week 13 va Week 14 trong thu muc `exercise/`.
Code duoc dat truc tiep trong thu muc nay, khong tach thanh cac thu muc week13/week14.

## Yeu cau

- Python 3.10 tro len.
- VS Code hoac editor bat ky.
- Week 13 co lenh goi API can Internet; cac lenh con lai chay offline.
- Week 14 va unit test chi dung thu vien co san cua Python, khong can cai them package.

Kiem tra Python:

```bash
python --version
```

Neu may dung lenh `py` tren Windows, co the thay `python` bang `py`.

---

# Week 13 - Modules, CLI va API/HTTP

## Muc tieu hoc tap

Sau bai nay, ban co the:

1. Tach code thanh cac module Python va import ham tu module khac.
2. Viet ham co tham so, gia tri tra ve va kiem tra du lieu dau vao.
3. Nhan tham so tu terminal bang `argparse`.
4. Hieu HTTP GET, status code, JSON, timeout va loi mang.
5. Chay mot chuong trinh bang lenh terminal va doc ket qua.

## Cac file

- `week13_utils.py`: ham tien ich, gom loi chao va kiem tra so chan.
- `week13_api.py`: gui HTTP GET, kiem tra status code va doc JSON.
- `week13_cli.py`: giao dien dong lenh ket noi cac chuc nang.

## Cach chay

Mo terminal tai thu muc `exercise`:

```bash
python week13_cli.py --help
python week13_cli.py greet Dung
python week13_cli.py even 8
python week13_cli.py even 7
python week13_cli.py get https://api.github.com
```

Vi du ket qua:

```text
Xin chao, Dung!
So chan
So le
```

Lenh `get` in JSON do API tra ve. Ket qua cu the co the thay doi theo API. Lenh nay can Internet.

### Y nghia cac lenh

| Lenh | Tac dung |
|---|---|
| `greet Dung` | Tao loi chao tu ten |
| `even 8` | Kiem tra mot so nguyen chan hay le |
| `get URL` | Goi HTTP GET va in JSON |
| `--help` | Xem huong dan su dung |

### Kien thuc can nho

- **Module**: mot file `.py` co the chua ham va lop de file khac import.
- **CLI**: command-line interface, cho phep truyen lenh va tham so tu terminal.
- **HTTP GET**: gui yeu cau lay du lieu tu server.
- **Status code**: ma phan hoi HTTP; nhom 2xx thuong la thanh cong, 4xx la loi yeu cau, 5xx la loi server.
- **JSON**: dinh dang du lieu thuong duoc API su dung.
- **Timeout**: gioi han thoi gian cho server phan hoi. Khong nen de chuong trinh cho vo han.
- **Dependency**: thu vien ben ngoai ma du an can cai. Week 13 nay dung thu vien chuan `urllib`, nen khong can cai them.

### Bai tap tu luyen

1. Sua loi chao de ten rong bi tu choi.
2. Them lenh `square NUMBER` de tinh binh phuong.
3. Goi mot API cong khai khac va mo ta cac truong JSON.
4. Thu mot URL sai de quan sat cach chuong trinh bao loi.
5. Giai thich tai sao `argparse` phu hop hon viec tu tach `sys.argv` bang tay.

---

# Week 14 - OOP Essentials

## Muc tieu hoc tap

Sau bai nay, ban co the:

1. Tao class va khoi tao object bang `__init__`.
2. Hieu vai tro cua `self`, attribute va method.
3. Dinh nghia `__str__` de in object de doc.
4. Dung composition: mot Student co nhieu Course.
5. Hieu inheritance co ban qua SavingsAccount ke thua BankAccount.
6. Dung exception de chan du lieu khong hop le va viet unit test.

## Cac file

- `week14_oop.py`: cac class Course, Student, BankAccount va SavingsAccount, kem vi du chay.
- `test_week14_oop.py`: unit test cho cac hanh vi chinh.

## Cach chay chuong trinh

```bash
python week14_oop.py
```

Chuong trinh minh hoa sinh vien dang ky mon hoc, tinh tong tin chi, nap/rut tien va tinh lai tiet kiem.

## Chay unit test

```bash
python -m unittest -v test_week14_oop.py
```

Neu tat ca test thanh cong, dong cuoi se cho biet so test da chay va trang thai OK.

## Giai thich mo hinh

- `Course`: luu ten mon hoc va so tin chi.
- `Student`: luu ten sinh vien va danh sach mon hoc. Student **co** cac Course, day la composition.
- `BankAccount`: quan ly chu tai khoan, so du, nap tien va rut tien.
- `SavingsAccount`: la mot BankAccount co them lai suat, day la vi du inheritance don gian.
- `__init__`: chay khi tao object, dung de khoi tao du lieu ban dau.
- `self`: tham chieu den object hien tai.
- `__str__`: quy dinh cach object hien thi khi dung `print()`.
- `super()`: goi phuong thuc khoi tao cua lop cha.

## Bai tap tu luyen

1. Them phuong thuc `drop_course()` cho Student.
2. Them phuong thuc hien thi danh sach mon hoc.
3. Chan rut tien neu so tien nho hon hoac bang 0.
4. Them test cho ten sinh vien rong.
5. Giai thich vi sao Student chua danh sach Course la composition, con SavingsAccount ke thua BankAccount la inheritance.

---

# Quy trinh tu kiem tra

Chay lan luot cac lenh sau tu thu muc `exercise`:

```bash
python week13_cli.py greet Dung
python week13_cli.py even 10
python week14_oop.py
python -m unittest -v test_week14_oop.py
```

Neu lenh nao loi:

1. Doc dong cuoi cua traceback truoc.
2. Xac dinh file va dong bi loi.
3. Kiem tra ten file, ten ham va du lieu dau vao.
4. Sua loi nho nhat co the.
5. Chay lai lenh va unit test.

**Luu y:** README huong dan bai tap va cach tu kiem tra. Hay tu chay cac lenh tren may cua ban de xac nhan moi truong Python hoat dong dung.
