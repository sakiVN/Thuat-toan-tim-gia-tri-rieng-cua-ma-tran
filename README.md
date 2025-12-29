# Thuật toán tìm giá trị riêng của ma trận
Sử dụng các phương pháp tính khác nhau để giải quyết bài toán tìm giá trị riêng của ma trận.

Bài báo cáo này nghiên cứu và triển khai các thuật toán lặp để giải bài toán tìm trị riêng của ma trận vuông trong môn **Tính toán khoa học** (ĐHBK Hà Nội).

Nội dung chính gồm:
- **Power Method**: thuật toán đơn giản, chi phí thấp `O(n²)`, dùng để tìm trị riêng trội (ứng dụng trong PageRank).
- **Pure QR Algorithm**: tìm toàn bộ trị riêng thông qua phân rã QR lặp, có cơ sở lý thuyết vững chắc nhưng chi phí cao `O(n³)`.
- **Francis Implicit Double Shift** (đọc thêm): nền tảng của các thư viện hiện đại như LAPACK và `numpy.linalg.eig`, cho tốc độ và độ ổn định vượt trội.
