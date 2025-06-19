import numpy as np

# Hàm thực hiện phân tích QR bằng biến đổi Householder
# Đầu vào: ma trận A (m x n)
# Đầu ra: ma trận Q (vuông, trực giao) và R (tam giác trên) sao cho A = Q @ R
def householder_qr(A):
    """
    Compute the QR decomposition of an m-by-n matrix A using Householder transformations.
    Returns Q, R such that A = Q @ R
    """

    A = np.array(A, dtype=float)  # Đảm bảo A là mảng numpy kiểu float
    m, n = A.shape                # Lấy kích thước của A
    Q = np.eye(m)                 # Khởi tạo Q là ma trận đơn vị (vuông)
    R = A.copy()                  # Khởi tạo R là bản sao của A
    for j in range(n):            # Lặp qua từng cột
        x = R[j:, j]              # Lấy vector cột từ hàng j trở xuống
        normx = np.linalg.norm(x) # Tính chuẩn (norm) của x
        s = -np.sign(x[0]) if x[0] != 0 else -1  # Xác định dấu để ổn định số học
        u1 = x[0] - s * normx     # Tính phần tử đầu của vector Householder
        w = x / u1 if u1 != 0 else x.copy()      # Chuẩn hóa vector Householder
        w[0] = 1                  # Đặt phần tử đầu là 1
        tau = -s * u1 / normx if normx != 0 else 0  # Hệ số Householder
        # Cập nhật R bằng phản xạ Householder
        R[j:, :] = R[j:, :] - (tau * np.outer(w, w @ R[j:, :]))
        # Cập nhật Q bằng phản xạ Householder
        Q[:, j:] = Q[:, j:] - np.outer(Q[:, j:] @ w, tau * w)
    R = np.triu(R)                # Đảm bảo R là tam giác trên
    return Q, R                   # Trả về Q và R

if __name__ == "__main__":
    # Ví dụ sử dụng: phân tích QR cho ma trận 3x3
    A = np.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]], dtype=float)
    Q, R = householder_qr(A)      # Gọi hàm phân tích QR
    print("Q =\n", Q)             # In ma trận Q
    print("R =\n", R)             # In ma trận R
    print("Check: Q @ R =\n", Q @ R)  # Kiểm tra lại phép nhân Q @ R
    print("Original A =\n", A)        # In lại ma trận gốc
