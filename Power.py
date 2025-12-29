import numpy as np
from datetime import datetime

# 1. Tạo ma trận ban đầu
size = int(input("Nhập kích thước ma trận: "))

print(f"Nhập {size * size} giá trị cách nhau bởi dấu cách:")
values = list(map(float, input().split()))
    
A = np.array(values).reshape(size, size)
print("Ma trận ban đầu (A):")
print(A)

# 2. Chọn vector khởi tạo ngẫu nhiên
x = np.random.rand(size, 1)

print("\nVector khởi tạo (x):")
print(x)

tol = 1e-6

max_iter = 100000000

iter_count = 0

lam = 0

lam_prev = 0

# 3. Thuật toán lũy thừa để tìm trị riêng lớn nhất
s = datetime.now()

for i in range(max_iter):
    # cập nhật x bằng cách nhân ma trận A với x và chuẩn hóa
    x = A @ x / np.linalg.norm(A @ x)

    # Tính xấp xỉ trị riêng
    lam = (x.T @ A @ x) / (x.T @ x)

    # Kiểm tra điều kiện dừng
    if np.abs(lam - lam_prev) < tol:
        break

    iter_count += 1
    lam_prev = lam

# 4. In kết quả
print(f'\nTrị riêng lớn nhất tìm được sau {iter_count} lần lặp: {np.round(lam[0, 0], 6)}')

print((datetime.now() - s).total_seconds() * 1e3)
