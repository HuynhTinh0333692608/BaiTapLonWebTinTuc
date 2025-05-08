import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import schedule
import time
import os

def lay_du_lieu_vnexpress(url_chuyen_muc, so_trang=5):
    danh_sach_bai_viet = []
    for trang in range(1, so_trang + 1):
        if trang == 1:
            url = url_chuyen_muc
        else:
            url = f"{url_chuyen_muc}-p{trang}"
        print(f"Đang lấy dữ liệu từ trang: {url}")
        
        phan_hoi = requests.get(url)
        soup = BeautifulSoup(phan_hoi.content, 'html.parser')
        
        for muc in soup.select('.title-news a[href]'):
            url_bai_viet = muc['href']
            bai_viet = lay_bai_viet(url_bai_viet)
            if bai_viet:
                danh_sach_bai_viet.append(bai_viet)
    
    ngay_hom_nay = datetime.datetime.now().strftime('%Y%m%d')
    os.makedirs('data', exist_ok=True)
    ten_file = f"data/du_lieu_vnexpress_{ngay_hom_nay}.xlsx"
    
    df = pd.DataFrame(danh_sach_bai_viet)
    df.to_excel(ten_file, index=False)
    print(f"Đã lưu dữ liệu vào {ten_file}")

def lay_bai_viet(url_bai_viet):
    print(f"-> Đang lấy bài viết: {url_bai_viet}")
    try:
        phan_hoi = requests.get(url_bai_viet)
        soup = BeautifulSoup(phan_hoi.content, 'html.parser')
        
        tieu_de = soup.find('h1', class_='title-detail').get_text(strip=True)
        mo_ta = soup.find('p', class_='description').get_text(strip=True)
        
        the_hinh_anh = soup.find('meta', property='og:image')
        hinh_anh = the_hinh_anh['content'] if the_hinh_anh else ''
        
        noi_dung_doan = soup.select('.fck_detail p')
        noi_dung = '\n'.join(p.get_text(strip=True) for p in noi_dung_doan)
        
        return {
            'Lien_ket': url_bai_viet,
            'Tieu_de': tieu_de,
            'Mo_ta': mo_ta,
            'Hinh_anh': hinh_anh,
            'Noi_dung': noi_dung
        }
    except Exception as loi:
        print(f"Lỗi khi lấy bài viết: {loi}")
        return None

def cong_viec():
    chuyen_muc = 'https://vnexpress.net/kinh-doanh'  # Chuyên mục muốn lấy
    lay_du_lieu_vnexpress(chuyen_muc, so_trang=5)

schedule.every().day.at("06:00").do(cong_viec)  # chạy lúc 6 giờ sáng mỗi ngày

if __name__ == "__main__":
    print("Đang chạy lịch thu thập dữ liệu...")
    while True:
        schedule.run_pending()
        time.sleep(60)
