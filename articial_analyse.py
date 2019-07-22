# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 08:24:15 2017

@author: dell
"""
import re
import pandas as pd
import numpy as np

textdata1=open('d:\\python-practice\\article.txt','r').read()

#文本处理
#textdata1=textdata.decode('gbk')

newtextdata=textdata1.split(u'\n\n')
for i in range(newtextdata.count(u'')):
    newtextdata.remove(u'')
for i in range(newtextdata.count(u'\n')):
    newtextdata.remove(u'\n')

data=[]
for s in newtextdata:
    data.append(s.replace('\n',''))

#文本挖掘
company=[]
for s in data:
    s=re.findall(u'[（）\u4e00-\u9fa5]+一、公司简介',s)
    for a in s:
        company.append(a.replace(u'一、公司简介',''))

pollution_air=[]
for s in data:
    s=re.findall(u'废气：.*?[；。]',s)
    if s==[]:
        pollution_air.append(s)
    else:
        for a in s:
            pollution_air.append(a.replace(u'废气：',u'').replace(u'；',u'').replace(u'。',u'').split(u'、'))


#
pollution_air_set=[]
for i in range(len(pollution_air)):
    for j in range(len(pollution_air[i])):
        pollution_air_set.append(pollution_air[i][j])

new_pollution_air_set=list(set(pollution_air_set))

matrix_air=np.zeros((len(pollution_air),len(new_pollution_air_set)))

#for a in new_pollution_air_set:
#    for s in pollution_air:
#        for k in s:
#            if a in k:
#                matrix_air[pollution_air.index(s),new_pollution_air_set.index(a)]=1
#会出现，只要有字段在，就能匹配上的错误，例如含有a中含有二氯甲烷，用B中氯甲烷也能匹配上

#                            
for i in range(len(new_pollution_air_set)):
    for j in range(len(pollution_air)):
        for k in range(len(pollution_air[j])):
            if new_pollution_air_set[i]==pollution_air[j][k]:
                matrix_air[j,i]=1

result=pd.DataFrame(matrix_air,index=company,columns=new_pollution_air_set)
result.to_csv('C:\\Users\\dell\Desktop\\result.csv',index=True,encoding='gbk')

#废气排放排名
pollution_air_count=np.sum(result,axis=0)
pollution_air_count.sort(axis=0,ascending=False)


#制作词云图
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image
import matplotlib.pyplot as plt

plt_pollution_air=','.join(new_pollution_air_set)

coloring=np.array(Image.open("C:\\Users\\dell\\Desktop\\1.jpg "))
my_wordcloud = WordCloud(background_color="white",max_words=2000,
                         font_path = 'C:/Windows/Fonts/msyh.ttf',
                         mask=coloring,max_font_size=60,random_state=42,scale=2
                         ).generate(plt_pollution_air)

image_colors=ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
