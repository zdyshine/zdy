# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 09:08:09 2019

@author: 我自人间来
计算两个框的iou
函数传入方式：（[xmin1, ymin1, xmax1, ymax1],[xmin2, ymin2, xmax2, ymax2]）

txt格式：
./test_image/img_calligraphy_85886_bg.jpg 1 a 20 52 68 227
./test_image/img_calligraphy_87888_bg.jpg 3 a 104 54 149 298 a 56 59 104 295 a 22 57 64 185
"""
import pandas as pd
import shutil 
#def compute_iou(rec1, rec2):
#    """
#    computing IoU
#    :param rec1: (y0, x0, y1, x1), which reflects
#            (top, left, bottom, right)
#    :param rec2: (y0, x0, y1, x1)
#    :return: scala value of IoU
#    """
#    # computing area of each rectangles
#    S_rec1 = (rec1[2] - rec1[0]) * (rec1[3] - rec1[1])
#    S_rec2 = (rec2[2] - rec2[0]) * (rec2[3] - rec2[1])
# 
#    # computing the sum_area
#    sum_area = S_rec1 + S_rec2
# 
#    # find the each edge of intersect rectangle
#    left_line = max(rec1[1], rec2[1])
#    right_line = min(rec1[3], rec2[3])
#    top_line = max(rec1[0], rec2[0])
#    bottom_line = min(rec1[2], rec2[2])
# 
#    # judge if there is an intersect
#    if left_line >= right_line or top_line >= bottom_line:
#        return 0
#    else:
#        intersect = (right_line - left_line) * (bottom_line - top_line)
#        return intersect / (sum_area - intersect)*1.0
# 
 

import numpy as np
def compute_iou(box1, box2, wh=False):
    """
    compute the iou of two boxes.
    Args:
        box1, box2: [xmin, ymin, xmax, ymax] (wh=False) or [xcenter, ycenter, w, h] (wh=True)
        wh: the format of coordinate.
    Return:
        iou: iou of box1 and box2.
    """
    if wh == False:
        xmin1, ymin1, xmax1, ymax1 = box1
        xmin2, ymin2, xmax2, ymax2 = box2
    else:
        xmin1, ymin1 = int(box1[0]-box1[2]/2.0), int(box1[1]-box1[3]/2.0)
        xmax1, ymax1 = int(box1[0]+box1[2]/2.0), int(box1[1]+box1[3]/2.0)
        xmin2, ymin2 = int(box2[0]-box2[2]/2.0), int(box2[1]-box2[3]/2.0)
        xmax2, ymax2 = int(box2[0]+box2[2]/2.0), int(box2[1]+box2[3]/2.0)

    ## 获取矩形框交集对应的左上角和右下角的坐标（intersection）
    xx1 = np.max([xmin1, xmin2])
    yy1 = np.max([ymin1, ymin2])
    xx2 = np.min([xmax1, xmax2])
    yy2 = np.min([ymax1, ymax2])

    ## 计算两个矩形框面积
    area1 = (xmax1-xmin1) * (ymax1-ymin1) 
    area2 = (xmax2-xmin2) * (ymax2-ymin2)
    
    inter_area = (np.max([0,xx2-xx1]))*(np.max([0,yy2-yy1]))
    iou = inter_area / (area1+area2-inter_area+1e-6) *1.0

#    inter_area = (np.max([0, xx2-xx1])) * (np.max([0, yy2-yy1]))#计算交集面积
#    iou = inter_area / (area1+area2-inter_area+1e-6) *1.0　＃计算交并比

    return iou

#def test_iou():
#    rect1 = (661, 27, 679, 47)
#    # (top, left, bottom, right)
#    rect2 = (662, 27, 682, 47)
#    iou = compute_iou(rect1, rect2)
#    print(iou)
#test_iou()

Label = []
IOU = []
Image_name = []
a = []
b = []
with open ('./submission_label2.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace('\n','')
        img_name = line.replace('\n','').split(' ')[0]
#        print(img_name)
        num = line.split(' a ')[0][-1]
        num = int(num)
#        print(num)
        label = line.split(' a ')[1:] #['21 52 61 329', '72 59 111 436', '125 62 163 405']
        
        if num == 1:
            continue
        
        for i in range(num):
            Label.append(label[i].split(' '))
           
        for n in range(num-1):
            a.append(int(Label[n][0]))
            a.append(int(Label[n][1]))
            a.append(int(Label[n][2]))
            a.append(int(Label[n][3]))
            
            b.append(int(Label[n+1][0]))
            b.append(int(Label[n+1][1]))
            b.append(int(Label[n+1][2]))
            b.append(int(Label[n+1][3]))
#            print(a,b)

#            rect1 = (int(Label[n][0]), int(Label[n][1]), int(Label[n][2]), int(Label[n][3]))
#            rect2 = (int(Label[n+1][0]), int(Label[n+1][1]), int(Label[n+1][2]), int(Label[n+1][3]))
#            iou =compute_iou(rect1, rect2)
            iou = compute_iou(a,b)
            a = []
            b = []            
#            print(iou)
            if iou > 0.1:
                IOU.append(iou)
                Image_name.append(img_name)
        Label = []
#print(len(IOU))
#print(len(Image_name))
image_names = list(set(Image_name))
print(len(image_names))
#data_iou = pd.DataFrame(columns=['FileName','Iou'])
#data_iou['FileName'] = Image_name
#data_iou['Iou'] = IOU
#data_iou.to_csv('./submission2_iou_5.csv', header=True, index=None, encoding='utf_8_sig')

#for img in image_names:
##        f1.write(img + '\n')  
#    imgname = img.split('image/')[-1]
##        print(img)
#    shutil.copy(img,'./test_image_err2/'+imgname)

#with open('./img_list.txt','w') as f1:
#    for img in image_names:
##        f1.write(img + '\n')  
#        imgname = img.split('image/')[-1]
##        print(img)
#        shutil.copy(img,'./test_image_err'+imgname)
                
#image_names = []
#with open('./123.txt','r') as f:
#    lines = f.readlines()
#    for line in lines:
#        image_name = line.split(',')[0]
#        image_names.append(image_name)
#image_names = list(set(image_names))
#
#
#


