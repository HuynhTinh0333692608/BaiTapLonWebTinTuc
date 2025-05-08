# Hướng Dẫn Cài Đặt và Sử Dụng Dự Án **Trình Thu Thập Dữ Liệu VNExpress**

Chào mừng bạn đến với dự án **Trình Thu Thập Dữ Liệu VNExpress**. Dự án này sẽ tự động thu thập dữ liệu tin tức từ **VNExpress** vào mỗi ngày lúc **6 giờ sáng**, bao gồm các bài viết từ các chuyên mục của trang web. Dữ liệu sẽ được lưu trữ vào **file Excel** để dễ dàng quản lý và phân tích.

---

## Yêu Cầu Cài Đặt

### 1. **Cài Đặt Python** (phiên bản >= 3.8)
   - Để chạy chương trình, bạn cần cài đặt Python từ [Trang chính thức của Python](https://www.python.org/downloads/).
   - Kiểm tra xem Python đã được cài đặt chưa bằng cách chạy lệnh sau trong terminal hoặc CMD:

     ```bash
     python --version
     ```

   Nếu chưa cài đặt Python, bạn có thể tải về và cài đặt theo hướng dẫn trên trang chính thức.

### 2. **Cài Đặt Git** (nếu chưa có)
   - Tải và cài đặt Git từ [Trang chính thức của Git](https://git-scm.com/downloads).

### 3. **Clone Dự Án từ GitHub**
   - Để bắt đầu, bạn cần sao chép (clone) dự án từ GitHub về máy tính của mình. Chạy lệnh sau trong terminal hoặc CMD:

     ```bash
     git clone (https://github.com/HuynhTinh0333692608/BaiTapLonWebTinTuc.git)
     ```

   Thay `tennguoidung` bằng **tên tài khoản GitHub** của bạn.

### 4. **Di Chuyển Vào Thư Mục Dự Án**
   - Sau khi clone xong, bạn cần di chuyển vào thư mục chứa dự án:

     ```bash
     cd BaiTapLonWebTinTuc
     ```

---

## Cài Đặt Môi Trường

Chương trình yêu cầu một số thư viện Python để hoạt động. Bạn cần cài đặt chúng trước khi chạy dự án.

### 1. **Cài Đặt Các Thư Viện Python**

Dự án sử dụng các thư viện Python để thu thập và xử lý dữ liệu. Để cài đặt các thư viện cần thiết, chạy lệnh sau trong terminal:

```bash
pip install -r requirements.txt
