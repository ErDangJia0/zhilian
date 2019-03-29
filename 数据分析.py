import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba 
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['font.family']='sans-serif' #解决中文不显示问题
data=pd.read_csv('taiyuan.csv',encoding='gbk')
data['eduLevel'].value_counts().plot(kind='bar',rot=0)
plt.show() #学历要求 条形图

str=''
for f in data['welfare']:
    str+=f
txt=jieba.cut(str)
result=" ".join(txt)
wc = WordCloud(
    font_path='simfang.ttf',
    background_color='white',
    max_font_size=50,
    width=500,
    height=500
).generate(result)
plt.imshow(wc)
plt.axis('off')
plt.show() #福利词云

data['workingExp'].value_counts().plot(kind='pie',autopct='%1.2f%%',explode=np.linspace(0,0.2,5))
plt.show()