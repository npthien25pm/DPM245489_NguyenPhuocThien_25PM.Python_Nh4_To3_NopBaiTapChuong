print(f"(a) lst[0]: {lst[0]}")
print(f"(b) lst[3]: {lst[3]}")
print(f"(c) lst[x]: {lst[x]}")
print(f"(d) lst[-x]: {lst[-x]}")
print(f"(e) lst[x + 1]: {lst[x + 1]}")
print(f"(f) lst[x] + 1: {lst[x] + 1}")
print(f"(g) lst[lst[x]]: {lst[lst[x]]}")
print(f"(h) lst[lst[lst[x]]]: {lst[lst[lst[x]]]}\n")

# Kết quả tóm tắt
print("--- Tóm Tắt Kết Quả ---")
results = {
    "lst[0]": lst[0],
    "lst[3]": lst[3],
    "lst[x]": lst[x],
    "lst[-x]": lst[-x],
    "lst[x + 1]": lst[x + 1],
    "lst[x] + 1": lst[x] + 1,
    "lst[lst[x]]": lst[lst[x]],
    "lst[lst[lst[x]]]": lst[lst[lst[x]]]
}

for expr, res in results.items():
    print(f"Kết quả của {expr:<18} là: {res}")