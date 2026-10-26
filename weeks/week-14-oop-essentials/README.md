# Tuần 14 — OOP Essentials, Composition và Inheritance

Tuần này luyện cách gom dữ liệu và hành vi liên quan vào object. Ví dụ xuyên suốt là một bot chọn hành động trong môi trường mô phỏng. Mục tiêu không phải tạo hệ thống phức tạp, mà là hiểu class, object, composition và inheritance qua code nhỏ.

## 1. Sau tuần này, bạn có thể

- Tạo class và object; dùng `__init__`, instance attributes và methods.
- Dùng `__str__` để quyết định cách object hiển thị khi gọi `print()`.
- Giải thích composition: một object nhận một hành vi khác từ bên ngoài.
- Thay strategy mà không phải sửa class `Bot`.
- Viết inheritance cơ bản khi quan hệ “is-a” hợp lý.
- Chạy các kiểm tra để xác nhận kết quả và hành vi dự kiến.

## 2. Cấu trúc thư mục

```text
week-14-oop-essentials/
├── checks/check_week.py
├── examples/
│   ├── 01_class_object.py
│   ├── 02_composition.py
│   └── 03_basic_inheritance.py
├── exercises/
│   ├── ex01_classes.py
│   ├── ex02_composition.py
│   └── ex03_inheritance.py
├── mini-project/
├── solutions/
│   └── oop_models.py
├── hints.md
├── notes.md
└── README.md
```

- `examples/`: ví dụ ngắn theo từng khái niệm.
- `exercises/`: bài tập thực hành.
- `solutions/oop_models.py`: các class và strategy mẫu để tham khảo.
- `checks/check_week.py`: kiểm tra hành vi chính của lời giải.

## 3. Chạy chương trình

Từ thư mục gốc repository, chạy từng ví dụ:

```bash
python weeks/week-14-oop-essentials/examples/01_class_object.py
python weeks/week-14-oop-essentials/examples/02_composition.py
python weeks/week-14-oop-essentials/examples/03_basic_inheritance.py
```

Chạy các bài thực hành:

```bash
python weeks/week-14-oop-essentials/exercises/ex01_classes.py
python weeks/week-14-oop-essentials/exercises/ex02_composition.py
python weeks/week-14-oop-essentials/exercises/ex03_inheritance.py
```

Chạy bộ kiểm tra lời giải:

```bash
python weeks/week-14-oop-essentials/checks/check_week.py
```

Nếu máy dùng `python3`, thay `python` bằng `python3`.

## 4. Đọc code theo thứ tự

1. Đọc [notes.md](notes.md) để hiểu class, object và composition.
2. Chạy `examples/01_class_object.py`; quan sát cách khởi tạo object và gọi method.
3. Chạy `examples/02_composition.py`; xem cách truyền strategy vào `Bot`.
4. Chạy `examples/03_basic_inheritance.py`; xem `Dog` kế thừa từ `Animal`.
5. Đọc các file trong `exercises/` và tự thay đổi giá trị để quan sát kết quả.
6. Đọc `solutions/oop_models.py` sau khi đã thử bài tập.
7. Chạy `checks/check_week.py` và làm [mini-project](mini-project/README.md).

## 5. Giải thích các khái niệm

### Class và object

Class là bản mô tả cách tạo object. Object là một thực thể được tạo từ class. `__init__` khởi tạo dữ liệu ban đầu; method là function gắn với class và thường làm việc trên dữ liệu của object thông qua `self`.

### Composition

Composition là đưa một object hoặc hành vi vào object khác thay vì bắt buộc kế thừa. Trong ví dụ, `Bot(strategy)` nhận một function làm strategy. Có thể thay `defensive`, `balanced` hoặc `aggressive` khi tạo Bot mà không sửa class Bot.

### Inheritance

Inheritance phù hợp khi quan hệ “is-a” rõ ràng. `Dog` là một loại `Animal`, vì vậy Dog có thể kế thừa dữ liệu chung như `name` rồi bổ sung method `speak()`.

### Vì sao ưu tiên composition?

Nếu chỉ muốn thay đổi hành vi, composition thường linh hoạt hơn kế thừa: class chính không cần biết cụ thể strategy được triển khai như thế nào. Chỉ dùng inheritance khi thật sự có quan hệ phân loại hợp lý.

## 6. Tự kiểm tra

- [ ] Tôi có thể giải thích `self`, `__init__` và method.
- [ ] Tôi biết cách tạo object và gọi method.
- [ ] Tôi có thể truyền một function vào `Bot`.
- [ ] Tôi hiểu sự khác nhau giữa composition và inheritance.
- [ ] Tôi chạy được bộ kiểm tra Week 14.
