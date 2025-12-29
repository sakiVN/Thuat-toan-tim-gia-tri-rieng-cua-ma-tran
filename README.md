# Thuật toán tìm giá trị riêng của ma trận
Sử dụng các phương pháp tính khác nhau để giải quyết bài toán tìm giá trị riêng của ma trận.

Bài báo cáo này nghiên cứu và triển khai các thuật toán lặp để giải bài toán tìm trị riêng của ma trận vuông trong môn **Tính toán khoa học** (ĐHBK Hà Nội).

Nội dung chính gồm:
- **Power Method**: thuật toán đơn giản, chi phí thấp `O(n²)`, dùng để tìm trị riêng trội (ứng dụng trong PageRank).
- **Pure QR Algorithm**: tìm toàn bộ trị riêng thông qua phân rã QR lặp, có cơ sở lý thuyết vững chắc nhưng chi phí cao `O(n³)`.
- **Francis Implicit Double Shift** (đọc thêm): nền tảng của các thư viện hiện đại như LAPACK và `numpy.linalg.eig`, cho tốc độ và độ ổn định vượt trội.

Tóm lược báo cáo:
## Giới thiệu
Dự án này nghiên cứu bài toán **tìm trị riêng và vectơ riêng của ma trận vuông** – một bài toán nền tảng trong đại số tuyến tính và tính toán khoa học, với nhiều ứng dụng thực tế như PageRank, PCA và phân tích dao động cơ học.  
Do các phương pháp cổ điển dựa trên đa thức đặc trưng không ổn định và không khả thi cho ma trận lớn, dự án tập trung vào các **phương pháp lặp**.

## Mục tiêu
- Trình bày cơ sở lý thuyết của bài toán trị riêng
- Triển khai và phân tích các thuật toán lặp phổ biến
- So sánh hiệu năng, tốc độ hội tụ và độ ổn định số của các phương pháp

## Các thuật toán được sử dụng

### Power Method
Power Method là thuật toán đơn giản dùng để tìm **trị riêng trội nhất** của ma trận.
- Độ phức tạp: `O(n²)` mỗi vòng lặp
- Hội tụ tuyến tính, phụ thuộc tỉ số phổ `|λ₂ / λ₁|`
- Hiệu quả cho ma trận lớn và thưa
- Hạn chế: chỉ tìm được một trị riêng, hội tụ chậm nếu các trị riêng sát nhau

### Pure QR Algorithm
Thuật toán QR lặp cho phép tìm **toàn bộ trị riêng** của ma trận thông qua các phép phân rã QR liên tiếp.
- Dựa trên biến đổi đồng dạng, bảo toàn trị riêng
- Hội tụ về dạng tam giác trên (Schur form)
- Độ phức tạp: `O(n³)` mỗi bước lặp
- Hạn chế: chi phí tính toán cao, hội tụ chậm nếu không đưa về dạng Hessenberg

### Francis Implicit Double Shift (đọc thêm)
Francis Double Shift là cải tiến hiện đại của QR Algorithm, được sử dụng trong các thư viện chuẩn như LAPACK.
- Giữ tính toán trên trường số thực
- Hội tụ nhanh (bậc hai)
- Độ ổn định và hiệu năng cao
- Được sử dụng thông qua `numpy.linalg.eig`

## Thực nghiệm và đánh giá
Các thuật toán được thử nghiệm trên nhiều loại ma trận khác nhau:
- Ma trận có các trị riêng sát nhau
- Ma trận có một trị riêng trội

Kết quả cho thấy:
- Power Method rất nhanh khi chỉ cần trị riêng trội
- Pure QR cho kết quả đầy đủ nhưng chậm
- Francis Double Shift cho hiệu năng và độ ổn định tốt nhất khi cần toàn bộ phổ trị riêng

## Công nghệ sử dụng
- Python
- NumPy
- Các thuật toán đại số tuyến tính (Power Iteration, QR Decomposition)
- LAPACK (thông qua NumPy)
