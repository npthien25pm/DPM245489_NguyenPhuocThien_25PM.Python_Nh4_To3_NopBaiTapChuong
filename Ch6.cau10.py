import numpy as np

def nhap_ma_tran(ten_ma_tran):
    """
    Hàm nhập ma trận từ người dùng.
    Yêu cầu người dùng nhập kích thước và các phần tử.
    """
    print(f"\n--- NHẬP MA TRẬN {ten_ma_tran} ---")
    
    while True:
        try:
            # Nhập kích thước ma trận (ví dụ: 3 3)
            kich_thuoc_str = input(f"Nhập số hàng và số cột của {ten_ma_tran} (cách nhau bởi dấu cách, ví dụ: 2 3): ")
            hang, cot = map(int, kich_thuoc_str.split())
            if hang <= 0 or cot <= 0:
                print("Lỗi: Số hàng và số cột phải là số nguyên dương.")
                continue
            break
        except ValueError:
            print("Lỗi: Vui lòng nhập hai số nguyên hợp lệ (số hàng, số cột).")
            
    print(f"Nhập các phần tử của {ten_ma_tran} theo từng hàng (cách nhau bởi dấu cách):")
    
    du_lieu_hang = []
    for i in range(hang):
        while True:
            try:
                # Nhập các phần tử của hàng hiện tại
                hang_str = input(f"Nhập các phần tử Hàng {i+1} (cần {cot} số): ")
                phan_tu_hang = list(map(float, hang_str.split()))
                
                if len(phan_tu_hang) != cot:
                    print(f"Lỗi: Cần nhập đủ {cot} phần tử cho hàng này.")
                    continue
                
                du_lieu_hang.append(phan_tu_hang)
                break
            except ValueError:
                print("Lỗi: Vui lòng nhập các số hợp lệ.")
                
    # Tạo ma trận NumPy
    return np.array(du_lieu_hang)

def cong_hai_ma_tran(A, B):
    """
    Cộng hai ma trận A và B. Chỉ thực hiện được nếu A và B cùng kích thước.
    """
    print("\n--- PHÉP CỘNG MA TRẬN (A + B) ---")
    if A.shape != B.shape:
        return "Lỗi: Hai ma trận phải có cùng kích thước để cộng."
    
    # NumPy tự động thực hiện phép cộng từng phần tử
    C = A + B
    return C

def tinh_ma_tran_hoan_vi(M):
    """
    Tính ma trận hoán vị (Transpose) của ma trận M.
    """
    # NumPy cung cấp thuộc tính .T hoặc hàm np.transpose()
    M_transpose = M.T
    return M_transpose

# --- CHƯƠNG TRÌNH CHÍNH ---

# 1. Nhập hai ma trận A và B
A = nhap_ma_tran("A")
B = nhap_ma_tran("B")

print("\n--- THÔNG TIN MA TRẬN ---")
print("Ma trận A:\n", A)
print("Ma trận B:\n", B)
print("-" * 30)

# 2. Cộng hai ma trận
C = cong_hai_ma_tran(A, B)
print("Kết quả A + B:\n", C)
print("-" * 30)

# 3. Tính ma trận hoán vị (Transpose)
print("--- MA TRẬN HOÁN VỊ (TRANSPOSE) ---")

# Hoán vị ma trận A
A_transpose = tinh_ma_tran_hoan_vi(A)
print("Hoán vị của Ma trận A (A^T):\n", A_transpose)

# Hoán vị ma trận B
B_transpose = tinh_ma_tran_hoan_vi(B)
print("Hoán vị của Ma trận B (B^T):\n", B_transpose)