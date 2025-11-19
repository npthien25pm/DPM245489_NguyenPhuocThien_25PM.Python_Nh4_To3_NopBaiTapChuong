def nhap_day_so_tang_dan():
    """
    Yêu cầu người dùng nhập một dãy số theo thứ tự tăng dần.
    Nếu nhập sai quy cách (số sau nhỏ hơn số trước), yêu cầu nhập lại số đó.
    Kết thúc việc nhập khi người dùng nhập một chuỗi rỗng.

    Returns:
        list: Dãy số đã được nhập và kiểm tra hợp lệ.
    """
    day_so = []
    so_truoc = None  # Theo dõi số cuối cùng được chấp nhận

    print("--- BẮT ĐẦU NHẬP DÃY SỐ TĂNG DẦN ---")
    print("Nhấn Enter (hoặc nhập chuỗi rỗng) để kết thúc nhập liệu.")

    while True:
        # Lấy giá trị nhập từ người dùng
        nhap_vao = input(f"Nhập số tiếp theo (hoặc Enter để dừng): ")

        # Kiểm tra điều kiện dừng
        if not nhap_vao.strip():
            break

        try:
            # Chuyển đổi đầu vào thành số
            so_hien_tai = float(nhap_vao)

            # Kiểm tra quy tắc tăng dần
            # Nếu đây không phải là số đầu tiên, kiểm tra xem nó có lớn hơn
            # hoặc bằng số trước đó không.
            if so_truoc is not None and so_hien_tai < so_truoc:
                print(f"⚠️ LỖI: Số {so_hien_tai} phải lớn hơn hoặc bằng số trước đó ({so_truoc}). Vui lòng nhập lại số này.")
                continue # Bỏ qua vòng lặp hiện tại, yêu cầu nhập lại số đó

            # Nếu hợp lệ, thêm số vào list và cập nhật số_truoc
            day_so.append(so_hien_tai)
            so_truoc = so_hien_tai
            print(f"✅ Đã thêm: {so_hien_tai}")

        except ValueError:
            # Xử lý trường hợp người dùng nhập ký tự không phải là số
            print("⚠️ LỖI: Đầu vào không phải là số hợp lệ. Vui lòng nhập lại.")
            continue # Yêu cầu nhập lại

    return day_so

# --- Phần chạy chương trình ---
day_so_cuoi_cung = nhap_day_so_tang_dan()

print("\n--- KẾT QUẢ CUỐI CÙNG ---")
if day_so_cuoi_cung:
    # In dãy số sau khi đã nhập xong
    print("Dãy số đã nhập theo thứ tự tăng dần là:")
    print(day_so_cuoi_cung)
else:
    print("Bạn đã không nhập bất kỳ số nào.")