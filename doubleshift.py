import numpy as np
import time

# Nhap kich thuoc ma tran tu ban phim
size = int(input("Nhap kich thuoc ma tran (size): "))

# Tao ma tran ngau nhien
A = np.random.rand(size, size)

# Bat dau do thoi gian
start_time = time.time()

# Su dung thu vien NumPy (goi den LAPACK)
eigenvalues, eigenvectors = np.linalg.eig(A)

end_time = time.time()

print("Tri rieng tinh boi NumPy (LAPACK):")
print(np.round(eigenvalues, 6))

print(f"Thoi gian thuc thi: {(end_time - start_time) * 1000:.4f} ms")
