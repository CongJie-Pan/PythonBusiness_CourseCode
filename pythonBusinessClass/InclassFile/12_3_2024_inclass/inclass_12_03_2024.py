# Topic: Web Image Scraping

import requests
from bs4 import BeautifulSoup
import os
import urllib.parse

def download_image(url, folder_path, base_url='https://www.bbc.com'):
    try:
        # 處理相對URL
        if url.startswith('/'):
            url = base_url + url
        elif not url.startswith(('http://', 'https://')):
            url = base_url + '/' + url

        # 建立資料夾(如果不存在)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # 獲取檔案名稱
        filename = os.path.join(folder_path, url.split('/')[-1])

        # 下載圖片
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f'成功下載: {filename}')
        else:
            print(f'下載失敗: {url}')

    except Exception as e:
        print(f'跳過預設佔位圖片: {url}')  # 改進錯誤訊息


# 指定 BBC News 網址
url = 'https://www.bbc.com/news'

# 發送請求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # 解析HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # 找到所有圖片標籤，排除預設佔位圖片
    images = soup.find_all('img', class_='sc-a34861b-0')

    # 建立下載資料夾
    download_folder = 'bbc_images'

    # 下載每張圖片
    downloaded_urls = set()  # 用來追蹤已下載的URL

    for img in images:
        # 取得最大解析度的圖片URL
        srcset = img.get('srcset', '')
        if srcset and not 'grey-placeholder' in srcset:  # 排除預設佔位圖片
            # 解析srcset以獲取最大解析度的圖片
            urls = [url.strip().split(' ')[0] for url in srcset.split(',')]
            if urls:
                # 選擇最後一個URL(通常是最高解析度)
                img_url = urls[-1]
                if img_url not in downloaded_urls:  # 檢查是否已下載
                    download_image(img_url, download_folder)
                    downloaded_urls.add(img_url)
        else:
            # 如果沒有srcset，使用src屬性
            img_url = img.get('src')
            if img_url and not 'grey-placeholder' in img_url:  # 排除預設佔位圖片
                if img_url not in downloaded_urls:  # 檢查是否已下載
                    download_image(img_url, download_folder)
                    downloaded_urls.add(img_url)

else:
    print(f'錯誤: 無法訪問網頁。狀態碼: {response.status_code}')