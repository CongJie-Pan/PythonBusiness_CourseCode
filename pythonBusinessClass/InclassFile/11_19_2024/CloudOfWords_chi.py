import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
from collections import Counter

# First let's check if the font exists
font_path = os.path.join(os.environ['WINDIR'], 'Fonts', 'msjh.ttc')
print(f"Checking font path: {font_path}")
print(f"Font exists: {os.path.exists(font_path)}")

# Read the Chinese text file
with open('Shiji_Introduction_chi.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Use jieba for Chinese word segmentation
word_list = list(jieba.cut(text))

# Filter words to keep only meaningful words with 2 or more characters
meaningful_words = [word for word in word_list if len(word) >= 2 and not word.isspace()]

# Count word frequencies and get top 45
word_freq = Counter(meaningful_words)
top_45_words = dict(word_freq.most_common(45))

# Print the top 45 words and their frequencies
print("\nTop 45 most frequent meaningful words:")
for word, freq in top_45_words.items():
    print(f"{word}: {freq}")

try:
    # Create and generate a word cloud with top 45 meaningful words
    word_cloud = WordCloud(
        font_path=font_path,  # Microsoft JhengHei
        width=1000,          # Increased width for better display of more words
        height=500,          # Increased height for better display of more words
        background_color='white',
        random_state=30,
        max_font_size=100,
        prefer_horizontal=0.9,
        collocations=False,
        max_words=45        # Updated to show all 45 words
    ).generate_from_frequencies(top_45_words)

    # Display the generated image
    plt.figure(figsize=(12, 6))  # Increased figure size for better visibility
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.savefig('chinese_wordcloud_meaningful.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("\nWord cloud has been generated successfully!")

except Exception as e:
    print(f"Error occurred: {str(e)}")