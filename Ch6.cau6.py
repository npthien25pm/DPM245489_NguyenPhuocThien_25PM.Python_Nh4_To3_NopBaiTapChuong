Tuyệt vời! Dưới đây là code Python để tạo ra một list gồm $N$ số nguyên ngẫu nhiên, không trùng nhau, trong một phạm vi nhất định.Tôi sẽ sử dụng thư viện random và hàm sample() để đảm bảo tính ngẫu nhiên và không trùng lặp.🐍 Code Python: List Số Ngẫu Nhiên Không Trùng LặpPythonimport random

def tao_list_ngau_nhien_khong_trung(N, min_value, max_value):
    """
    Tạo ra một list gồm N số nguyên ngẫu nhiên, không trùng lặp.

    Args:
        N (int): Số lượng phần tử mong muốn trong list.
        min_value (int): Giá trị nhỏ nhất có thể của số ngẫu nhiên.
        max_value (int): Giá trị lớn nhất có thể của số ngẫu nhiên.

    Returns:
        list: List chứa N số nguyên ngẫu nhiên không trùng lặp,
              hoặc thông báo lỗi nếu không thể tạo đủ N số.
    """
    # Đảm bảo phạm vi giá trị đủ lớn để chọn N số không trùng
    if N > (max_value - min_value + 1):
        return f"Lỗi: Không thể chọn {N} số không trùng lặp trong phạm vi từ {min_value} đến {max_value}. Vui lòng tăng phạm vi."

    # Tạo một dãy số có thể chọn
    day_so_khong_trung = range(min_value, max_value + 1)

    # Sử dụng random.sample để chọn N phần tử ngẫu nhiên không lặp
    list_ngau_nhien = random.sample(day_so_khong_trung, N)

    return list_ngau_nhien

# --- Phần chạy thử code ---

# 1. Nhập các tham số từ người dùng
try:
    N = int(input("Nhập số lượng phần tử N: "))
    min_val = int(input("Nhập giá trị nhỏ nhất (ví dụ: 1): "))
    max_val = int(input("Nhập giá trị lớn nhất (ví dụ: 100): "))
except ValueError:
    print("Đầu vào không hợp lệ. Vui lòng nhập số nguyên.")
    exit()

# 2. Tạo và in ra list
ket_qua = tao_list_ngau_nhien_khong_trung(N, min_val, max_val)

print("\n--- KẾT QUẢ ---")
print(f"Số lượng phần tử (N): {N}")
print(f"Phạm vi giá trị: [{min_val}, {max_val}]")
print(f"List ngẫu nhiên không trùng nhau:")
print(ket_qua)

# Kiểm tra đảm bảo không trùng lặp (Tùy chọn)
if isinstance(ket_qua, list):
    print(f"\nKiểm tra (Số phần tử duy nhất = {len(set(ket_qua))}): Đảm bảo không trùng lặp.")