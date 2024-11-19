import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os

# 設定字體路徑
font_path = os.path.join(os.environ['WINDIR'], 'Fonts', 'msjh.ttc')

# 擴充的中文停用詞列表
chinese_stopwords = set([
    # 基本語助詞
    '的', '了', '和', '是', '就', '都', '而', '及', '與', '這', '有', '在',
    '人', '我', '他', '來', '去', '到', '說', '要', '以', '之', '為', '也',
    '所', '又', '行', '道', '出', '入', '中', '其', '不', '可', '她', '那',
    '你', '會', '家', '能', '得', '於', '著', '下', '而', '過', '年', '月',
    '日', '時', '分', '秒', '把', '給', '讓',

    # 代詞和指示詞
    '這個', '那個', '這些', '那些', '他們', '自己', '什麼', '這樣', '那樣',

    # 數量詞和時間詞
    '一', '二', '三', '四', '五', '六', '七', '八', '九', '十',
    '百', '千', '萬', '億', '個', '多', '少', '今天', '明天', '昨天',

    # 特定於文本的無意義詞
    '先生', '因此', '只有', '然而', '大概', '如此', '以來',
    '如是', '所以', '便是', '其中', '由於', '至於', '認為',
    '不是', '可以', '一個', '一部', '一些', '這些', '那些',
    '甚至', '之中', '之後', '之前'
])

# 讀取文本
with open('Shiji_Introduction_chi.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 使用結巴分詞並過濾
words_list = jieba.cut(text)
filtered_words = [word for word in words_list
                  if word not in chinese_stopwords
                  and len(word) >= 2
                  and not word.isspace()]

words = ' '.join(filtered_words)

# 讀取並處理遮罩圖片
original_mask = np.array(Image.open("originalBook.png"))

# 放大遮罩圖片
enlarged_size = (1200, 1200)  # 調整大小
mask_image = Image.fromarray(original_mask).resize(enlarged_size, Image.Resampling.LANCZOS)
book_mask = np.array(mask_image)

# 確保遮罩是二值的
if len(book_mask.shape) > 2:
    book_mask = book_mask.mean(axis=2)
thresh = book_mask.max() / 2
book_mask = (book_mask > thresh) * 255


# 自定義顏色函數 - 使用深藍色系
def custom_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    # 使用較深的藍色
    return f"hsl(220, 100%, {random_state.randint(20, 40)}%)"


# 生成文字雲
wordcloud_masked = WordCloud(
    font_path=font_path,
    mask=book_mask,
    background_color='white',
    max_words=50,  # 增加詞數
    max_font_size=100,  # 增加最大字體
    min_font_size=20,  # 調整最小字體
    prefer_horizontal=0.7,
    relative_scaling=0.3,  # 適當的相對縮放
    repeat=True,
    random_state=42,
    color_func=custom_color_func,
    contour_width=3,  # 加粗輪廓
    contour_color='black',
    collocations=False,
    margin=2  # 適當的邊距
).generate(words)

# 創建更大的圖形
plt.figure(figsize=(15, 15))  # 增加圖形大小
plt.imshow(wordcloud_masked, interpolation='bilinear')
plt.axis("off")

# 保存高解析度圖片
wordcloud_masked.to_file("book_wordcloud_enlarged.png")
plt.savefig('book_wordcloud_enlarged_plot.png',
            dpi=300,
            bbox_inches='tight',
            pad_inches=0.1)
plt.close()

print("\n詞頻統計:")
word_freq = {}
for word in filtered_words:
    if len(word) >= 2:
        word_freq[word] = word_freq.get(word, 0) + 1

print("\n最常出現的詞(Top 20):")
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:20]
for word, freq in sorted_words:
    print(f"{word}: {freq}")