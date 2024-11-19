from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read the text file
with open('Shiji_Introduction.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Create and generate a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud
plt.figure(figsize=(10,5))
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('wordcloud.png')
plt.close()