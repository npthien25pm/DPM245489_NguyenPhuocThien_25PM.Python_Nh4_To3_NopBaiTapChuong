def kiem_tra_so_nguyen_to(n):
    """
    Kiểm tra xem một số nguyên có phải là số nguyên tố hay không.
    Số nguyên tố là số tự nhiên lớn hơn 1 và chỉ có 2 ước là 1 và chính nó.
    """
    if n < 2:
        return False
    # Chỉ cần kiểm tra đến căn bậc hai của n
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def xu_ly_mang_so_tu_nhien(M):
    """
    Phân loại các số trong mảng thành số lẻ, số chẵn, số nguyên tố, và 
    số không phải số nguyên tố, sau đó in ra kết quả.

    Args:
        M (list): Mảng chứa các số tự nhiên.
    """
    so_le = []
    so_chan = []
    so_nguyen_to = []
    so_khong_phai_nguyen_to = []

    # Duyệt qua từng phần tử trong mảng
    for so in M:
        # --- Phân loại Lẻ/Chẵn ---
        if so % 2 == 0:
            so_chan.append(so)
        else:
            so_le.append(so)

        # --- Phân loại Nguyên tố ---
        if kiem_tra_so_nguyen_to(so):
            so_nguyen_to.append(so)
        else:
            so_khong_phai_nguyen_to.append(so)

    print("\n--- KẾT QUẢ XỬ LÝ MẢNG ---")

    # Dòng 1: Số lẻ
    print(f"Dòng 1 : Các số lẻ là: {so_le}. Tổng cộng có {len(so_le)} số lẻ.")

    # Dòng 2: Số chẵn
    print(f"Dòng 2 : Các số chẵn là: {so_chan}. Tổng cộng có {len(so_chan)} số chẵn.")

    # Dòng 3: Số nguyên tố
    print(f"Dòng 3 : Các số nguyên tố là: {so_nguyen_to}.")

    # Dòng 4: Số không phải là số nguyên tố
    print(f"Dòng 4 : Các số không phải là số nguyên tố là: {so_khong_phai_nguyen_to}.")

# --- Chương trình chính ---

# Mảng mẫu theo yêu cầu
M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8]

# Xử lý và in kết quả
xu_ly_mang_so_tu_nhien(M)