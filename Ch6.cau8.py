Đây là code Python thực hiện việc nhập vào một dãy $n$ số thực, sắp xếp dãy số đó theo thứ tự giảm dần, và sau đó in ra kết quả.🐍 Code Python: Nhập và Sắp Xếp Dãy Số Giảm DầnPythondef nhap_day_so():
    """
    Yêu cầu người dùng nhập một dãy các số thực (float) cho đến khi 
    người dùng nhập chuỗi rỗng để kết thúc.

    Returns:
        list: List chứa các số thực đã nhập.
    """
    M = []
    print("--- BẮT ĐẦU NHẬP DÃY SỐ (M[0], M[1],...) ---")
    print("Nhấn Enter (hoặc nhập chuỗi rỗng) để kết thúc nhập liệu.")

    while True:
        # Lấy đầu vào từ người dùng
        nhap_vao = input(f"Nhập phần tử M[{len(M)}]: ")

        # Kiểm tra điều kiện dừng
        if not nhap_vao.strip():
            break

        try:
            # Chuyển đổi đầu vào thành số thực
            so_thuc = float(nhap_vao)
            M.append(so_thuc)
        except ValueError:
            # Xử lý trường hợp người dùng nhập ký tự không phải là số
            print("⚠️ LỖI: Đầu vào không phải là số thực hợp lệ. Vui lòng nhập lại.")
            continue # Yêu cầu nhập lại

    return M

def sap_xep_giam_dan(M):
    """
    Sắp xếp list số thực M theo thứ tự giảm dần.

    Args:
        M (list): List các số thực.

    Returns:
        list: List đã được sắp xếp giảm dần.
    """
    # Sử dụng phương thức .sort() của list với tham số reverse=True
    M.sort(reverse=True)
    return M

# --- Chương trình chính ---
# 1. Nhập dãy số
day_so_goc = nhap_day_so()

print("\n--- KẾT QUẢ ---")

if not day_so_goc:
    print("Bạn đã không nhập bất kỳ số nào.")
else:
    # 2. Sắp xếp dãy số
    # Lưu ý: Hàm sort() thay đổi list gốc (in-place). 
    # Nếu muốn giữ lại list gốc, bạn nên dùng sorted(day_so_goc, reverse=True)
    day_so_da_sap_xep = sap_xep_giam_dan(day_so_goc)
    
    # 3. Xuất ra dãy số sau khi sắp xếp
    print(f"Dãy số sau khi sắp xếp giảm dần là (n = {len(day_so_da_sap_xep)}):")
    print(day_so_da_sap_xep)