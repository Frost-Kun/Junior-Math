import numpy as np
import matplotlib.pyplot as plt
def fsolve(f, a,b , n, error= 1e-8):
    """
  Tìm các nghiệm của hàm f(x) = 0 có trong đoạn [a, b]
    Nhập:
      f - Hàm cần tìm nghiệm. Cách tạo hàm f:
        def f(x):
          fx = f(x)
          return fx 
      Theo hình thức của Newton - Raphson.
      a, b - đoạn cần tìm nghiệm theo đề bài
      n - Số điểm trong đoạn [a, b] dùng để gần x0i =( [a, x01, ....., b])
          ban đầu cho các lần tìm nghiệm khác nhau.
          Hãy điều chỉnh n lớn hơn số điểm mà hàm số cắt trục hoành
          để tìm được hết tất cả các nghiệm có trong [a, b].
      error - Sai số cho phép, mặc định error = 1e-8 hoặc cho 1 số error khác như (1e-10, 1e-12,.....)
    Xuất x0 - Các nghiệm của hàm f(x) trong đoạn [a, b]
    Yêu cầu đề bài:
    1. Vẽ hàm f(x) trong khoảng [a, b]
    2. Xem cắt trục hoành bao nhiêu điểm (n)
    3. Chia đoạn [a, b] thành > n điểm x0i
    4. Cho vòng lặp và nghiệm ban đầu là x0i
    5. Giải tìm nghiệm
    6. Sắp xếp lại nghiệm
    7. Xuất kết quả
  Số sẽ quy định từ đề bài mà xuất ra.
Bản quyền thuộc về Chân Kiệt, không được copy hay lấy dưới mọi hình thức.
Copyrighted by PoseTona, please do not copy or take in any form.
"""
    def newton_raphson(f, x0):
        if abs(f(x0)) <= error: return x0
        while abs(f(x0)) > error:
            h = 1e-3
            x0 -= f(x0)*2*h/(f(x0+h)-f(x0-h))
        return x0
    xi = np.linspace(a, b, n)
    roots = []
    for x0 in xi:
        root = newton_raphson(f, x0)
        root = round(root, 2)
        if a <= root <= b and root not in roots: 
            roots = np.append(roots, root)
    return roots
