import pandas as pd
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud

# 1、读取数据
data = open('太原1.csv', 'r').read()
# 2、把数据分开
cut_data = jieba.cut(data)
result = ' '.join(cut_data)
# 3、生成词云图
wc = WordCloud(
    font_path='simfang.ttf',
    background_color='white',
    # 图片的宽
    width=500,
    # 图片的高
    height=350,
    # 字体大小
    max_font_size=50,
    min_font_size=10,
)
wc.generate(result)
# 保存词云图
wc.to_file('word.png')

# 4、显示图片
# 指定图片名称
plt.figure('Python')
plt.imshow(wc)
plt.axis('off')
plt.show()