import numpy as np
from datetime import datetime

# 1. Tạo ma trận ban đầu
size = int(input("Nhập kích thước ma trận: "))

print(f"Nhập {size * size} giá trị cách nhau bởi dấu cách:")
values = list(map(float, input().split()))
    
A = np.array(values).reshape(size, size)
print("Ma trận ban đầu (A):")
print(A)

# 2. Thuật toán QR để tìm trị riêng
max_iter = 100000000

s = datetime.now()

iter_count = 0

for i in range(max_iter):
    # Phân rã QR
    Q, R = np.linalg.qr(A)
    # Cập nhật ma trận A
    A = R @ Q
    # Kiểm tra điều kiện dừng
    rows, cols = np.tril_indices(A.shape[0], k=-1)
    if (np.all(A[rows, cols] < 1e-6)):
        break

    iter_count += 1

# 3. Trích xuất trị riêng từ đường chéo chính
lam = np.diag(A)

# 4. In kết quả
print(f"\nMa trận sau {iter_count} lần lặp:")
print(np.round(A, 6))

print('\nTrị riêng tìm được bằng thuật toán QR:')
print(np.round(lam, 6))

print((datetime.now() - s).total_seconds() * 1e3)