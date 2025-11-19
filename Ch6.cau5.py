# List đầu vào
lst = [20, 1, -34, 40, -8, 60, 1, 3]

print("--- KẾT QUẢ THỰC THI LIST ---")
print(f"List gốc: {lst}")
print("-" * 35)

# (a) lst
print(f"(a) lst: {lst}")

# (b) lst[0:3] (Từ chỉ số 0 đến trước 3)
print(f"(b) lst[0:3]: {lst[0:3]}")

# (c) lst[4:8] (Từ chỉ số 4 đến trước 8, tức là cuối list)
print(f"(c) lst[4:8]: {lst[4:8]}")

# (d) lst[4:33] (Từ chỉ số 4 đến cuối list, vì 33 vượt quá phạm vi)
print(f"(d) lst[4:33]: {lst[4:33]}")

# (e) lst[-5:-3] (Từ chỉ số -5 đến trước -3)
print(f"(e) lst[-5:-3]: {lst[-5:-3]}")

# (f) lst[-22:3] (Từ đầu list (0) đến trước chỉ số 3, vì -22 vượt quá giới hạn âm)
print(f"(f) lst[-22:3]: {lst[-22:3]}")

# (g) lst[4:] (Từ chỉ số 4 đến hết)
print(f"(g) lst[4:]: {lst[4:]}")

# (h) lst[:] (Sao chép toàn bộ list)
print(f"(h) lst[:]: {lst[:]}")

# (i) lst[:4] (Từ đầu đến trước chỉ số 4)
print(f"(i) lst[:4]: {lst[:4]}")

# (j) lst[1:5] (Từ chỉ số 1 đến trước 5)
print(f"(j) lst[1:5]: {lst[1:5]}")

# (k) -34 in lst (Kiểm tra sự tồn tại)
print(f"(k) -34 in lst: {-34 in lst}")

# (l) -34 not in lst (Kiểm tra phủ định của sự tồn tại)
print(f"(l) -34 not in lst: {-34 not in lst}")

# (m) len(lst) (Độ dài list)
print(f"(m) len(lst): {len(lst)}")