# Tuần 13 — Modules, Packages, CLI và HTTP/API

Mục tiêu của tuần này là biết chia code thành nhiều file có trách nhiệm rõ ràng, chạy chương trình bằng command line và đọc một HTTP response cơ bản. Các ví dụ dùng Python standard library, không cần cài thư viện ngoài và các bài kiểm tra không gọi mạng thật.

## 1. Sau tuần này, bạn có thể

- Import function từ module khác và hiểu `if __name__ == "__main__"`.
- Nhận biết package qua `__init__.py` và phân biệt module/package.
- Dùng `argparse` để đọc tham số dòng lệnh.
- Tạo HTTP GET request bằng `urllib.request.Request`.
- Đọc status code, giải mã JSON và từ chối response lỗi.
- Giải thích vì sao phần xử lý nghiệp vụ nên tách khỏi CLI và HTTP adapter.

## 2. Cấu trúc thư mục

```text
week-13-modules-cli-api/
├── bot_course/
│   ├── __init__.py
│   ├── core.py
│   ├── adapter.py
│   └── http_foundation.py
├── checks/check_week.py
├── examples/offline_http.py
├── exercises/
│   ├── ex01_modules.py
│   ├── ex02_cli.py
│   └── ex03_http.py
├── mini-project/
├── cli.py
├── hints.md
├── notes.md
└── README.md
```

- `core.py`: quyết định hành động, không phụ thuộc giao diện hay mạng.
- `adapter.py`: chuyển dữ liệu đầu vào thành định dạng dùng trong bài học.
- `http_foundation.py`: tạo request và kiểm tra JSON response.
- `cli.py`: nhận input từ terminal bằng `argparse`.
- `exercises/`: bài thực hành theo từng chủ đề.

## 3. Chuẩn bị và chạy

Mở terminal tại thư mục gốc của repository. Không bắt buộc phải tạo virtual environment vì tuần này chỉ dùng thư viện có sẵn của Python.

Chạy CLI mẫu:

```bash
python weeks/week-13-modules-cli-api/cli.py --position 1 --goal 4
```

Kết quả là một dictionary có action `right`. Thử thêm các trường hợp:

```bash
python weeks/week-13-modules-cli-api/cli.py --position 4 --goal 4
python weeks/week-13-modules-cli-api/cli.py --position 3 --goal 1
```

Chạy bộ kiểm tra offline:

```bash
python weeks/week-13-modules-cli-api/checks/check_week.py
```

Nếu máy dùng lệnh `python3` thay vì `python`, thay lệnh tương ứng bằng `python3`.

## 4. Thứ tự học đề xuất

1. Đọc [notes.md](notes.md) để nắm khái niệm.
2. Đọc code trong `bot_course/`, đặc biệt là `core.py` và `adapter.py`.
3. Chạy `cli.py` với các giá trị khác nhau.
4. Hoàn thành hoặc đọc lời giải trong ba file thuộc `exercises/`.
5. Chạy `checks/check_week.py` để kiểm tra các hành vi chính.
6. Đọc [hints.md](hints.md) và thử [mini-project](mini-project/README.md).

## 5. Kiến thức cốt lõi

### Module và package

Một file Python là một module. Một thư mục chứa các module liên quan có thể được dùng như package. Dùng `import` để tái sử dụng code, tránh sao chép cùng một function vào nhiều file.

### Main guard

`if __name__ == "__main__":` giúp đoạn chạy thử chỉ thực thi khi file được chạy trực tiếp, không chạy ngoài ý muốn khi file được import.

### CLI

`argparse` đọc các tham số người dùng truyền vào terminal. Với `type=int`, chương trình chuyển input sang số nguyên và báo lỗi nếu input không hợp lệ.

### HTTP và JSON

HTTP response có status code và body. Trong bài này, chỉ status thuộc nhóm 200–299 được chấp nhận; body phải là JSON hợp lệ và có dạng object. Các fixture được tạo ngay trong code nên bài kiểm tra không cần kết nối Internet.

## 6. Lưu ý

Các ví dụ về bot chỉ là bài tập mô phỏng. Chuỗi `COURSE LOCAL FORMAT` được dùng để luyện ranh giới adapter; không phải định dạng tương thích với dịch vụ production nào. Không đưa token, mật khẩu hoặc dữ liệu riêng tư vào source code.

## 7. Tự kiểm tra

- [ ] Tôi giải thích được vì sao nên tách core và CLI.
- [ ] Tôi có thể chạy CLI với tham số bắt buộc.
- [ ] Tôi biết xử lý status code không thành công.
- [ ] Tôi hiểu JSON không hợp lệ sẽ gây lỗi.
- [ ] Tôi chạy được bộ kiểm tra offline.
