#Câu 8: Các loại lỗi và cách bắt lỗi

#1. Các loại lỗi trong lập trình Python

#   Lỗi cú pháp (SyntaxError): sai quy tắc Python
#   Lỗi logic: chương trình chạy nhưng sai kết quả
#   Lỗi runtime (quá trình chạy): ví dụ chia cho 0, sai kiểu dữ liệu…

#2. Cách bắt lỗi – dùng try/except
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Không thể chia cho 0")