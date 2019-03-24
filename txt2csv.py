# coding=utf8
'''
把txt文件转成csv文件
txt格式：
filename x1 y1 x2 y2...
img_calligraphy_80006_bg.jpg,20,52,66,52,66,212,20,212
img_calligraphy_80007_bg.jpg,331,83,452,83,452,209,331,209
img_calligraphy_80007_bg.jpg,445,94,559,94,559,205,445,205
img_calligraphy_80007_bg.jpg,221,80,335,80,335,199,221,199
img_calligraphy_80007_bg.jpg,105,79,225,79,225,204,105,204
img_calligraphy_80007_bg.jpg,22,52,54,52,54,121,22,121

csv格式：
filename x1,y1,x2,y2,x3,y3,x4,y4
'''

import os
import json
from PIL import Image
import numpy as np
import sys
import pandas as pd

#统计生成图片的h，w信息，并保存至train_size.csv
X1 = []
Y1 = []
X2 = []
Y2 = []
X3 = []
Y3 = []
X4 = []
Y4 = []
filename = []
#def Train_size(image_dir):
#    for image in os.listdir(image_dir):
#        filename.append(image)
#        h,w = Image.open(os.path.join(image_dir, image)).size
#        H.append(h)
#        W.append(w)
#        
#               
with open('./submission.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n','')
        image_name = line.split(',')[0]
#        print(image_name)
        x1 = line.split(',')[1]
        X1.append(x1)
        y1 = line.split(',')[2]
        Y1.append(y1)
#        x2 = line.split(',')[3]
#        X2.append(x2)
#        y2 = line.split(',')[4]
#        Y2.append(y2)
        x3 = line.split(',')[5]
        X3.append(x3)
        y3 = line.split(',')[6]
        Y3.append(y3)
#        x4 = line.split(',')[7]
#        X4.append(x4)
#        y4 = line.split(',')[8]
#        Y4.append(y4)
#        print(X1,Y1,X2,Y2,X3,Y3,X4,Y4)
#        data = line.split(',')[0:-1]
        filename.append(image_name)
#        datas.append(data)
#image_names = list(set(image_names))
#
#Train_size('../../data/dataset/test/')
data_csv = pd.DataFrame(columns=['FileName','x1','y1','x3','y3'])
data_csv['FileName'] = filename
data_csv['x1'] = X1
data_csv['y1'] = Y1
data_csv['x3'] = X3
data_csv['y3'] = Y3
##程序所在文件
data_csv.to_csv('./submission.csv', header=True, index=None, encoding='utf_8_sig')
