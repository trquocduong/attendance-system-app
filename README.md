# Hướng dẫn Setup Dự Án Attendance

## 1. Tạo Virtual Environment

```bash
python -m venv venv
```


## 2. Kích hoạt Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### MacOS / Linux

```bash
source venv/bin/activate
```


## 3. Kiểm tra phiên bản Python

```bash
python --version
```

Khuyến nghị sử dụng Python 3.10+


## 4. Cài đặt thư viện

### Cài FastAPI và Uvicorn

```bash
pip install fastapi uvicorn
```

### Hoặc cài toàn bộ thư viện từ requirements.txt

```bash
pip install -r requirements.txt
```


## 5. Xuất danh sách thư viện

```bash
pip freeze > requirements.txt
```


## 6. Chạy server FastAPI

```bash
uvicorn main:app --reload
```


## 7. Truy cập ứng dụng

Sau khi chạy thành công:

- API Server:

```text
http://127.0.0.1:8000
```

- Swagger UI:

```text
http://127.0.0.1:8000/docs
```

- ReDoc:

```text
http://127.0.0.1:8000/redoc
```


#  Cấu trúc thư mục gợi ý

```text
project/
│── venv/
│── main.py
│── requirements.txt
│── README.md
```


#  Lệnh hữu ích

## Tắt Virtual Environment

```bash
deactivate
```

## Cập nhật pip

```bash
python -m pip install --upgrade pip
```


#  Công nghệ sử dụng

- FastAPI
- Uvicorn
- Python


#  Ghi chú

Không push thư mục `venv/` lên GitHub.

Thêm file `.gitignore`:

```gitignore
venv/
__pycache__/
*.pyc
.env
```
