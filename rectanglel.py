# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:08:58 2019

@author: 我自人间来
针对文字检测识别，有4个坐标点来画框
数据格式：
img_calligraphy_100004_bg.jpg 20 362 26 53 102 57 93 370
img_calligraphy_100005_bg.jpg 106 53 225 53 225 174 106 174
img_calligraphy_100005_bg.jpg 225 53 344 53 344 184 225 184
img_calligraphy_100005_bg.jpg 344 53 463 53 463 172 344 172
img_calligraphy_100005_bg.jpg 463 53 582 53 582 175 463 175
img_calligraphy_100005_bg.jpg 20 72 50 72 50 135 20 135
"""
import numpy as np
import cv2
import codecs

name = []
boxs = []
box = np.zeros((4,2))
#box[0][0] = 1
#box[0][1] = 2
#print (box)
img_dir = './out_img/'
out_dir = './output1/'
box = np.zeros((4,2))
def get_images(img_dir):
    '''
    find image files in test data path
    :return: list of files found
    '''
    files = []
    exts = ['jpg', 'png', 'jpeg', 'JPG']
    for parent, dirnames, filenames in os.walk(img_dir):
        for filename in filenames:
            for ext in exts:
                if filename.endswith(ext):
                    files.append(os.path.join(parent, filename))
                    break
    print('Find {} images'.format(len(files)))
    return files

img_list = get_images(img_dir)

#print(img_list)
for im_dir in img_list:
    im_name = im_dir.split('/')[-1]
#    print(im_name)
    image = cv2.imread(im_dir)[:, :, ::-1]
    with codecs.open('./verifyImage.txt','r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n').split(' ') 
            box[0][0] = int(line[1])
            box[0][1] = int(line[2])
            box[1][0] = int(line[3])
            box[1][1] = int(line[4])
            box[2][0] = int(line[5])
            box[2][1] = int(line[6])
            box[3][0] = int(line[7])
            box[3][1] = int(line[8])
#            print(box)
            
#            cv2.polylines(image[:, :, ::-1], [box.astype(np.int32).reshape((-1, 1, 2))], True, color=(255, 255, 0), thickness=1)
            
###            print(im_path)
            if im_name == line[0]: #画框
                cv2.polylines(image[:, :, ::-1], [box.astype(np.int32).reshape((-1, 1, 2))], True, color=(255, 255, 0), thickness=1)
#        boxs.append(box)
            box = np.zeros((4,2))
    cv2.imwrite(out_dir + im_name, image[:, :, ::-1]) #保存图片
#    for b in boxs:
#        print('bbbb:',b)
#    boxs=[]
##                print('boxs:',boxs)
##                print('123213412')
##    print(im_name)
#i = 0
#for b in boxs:
#    i+=1
#    print('bbbb:',b)
#print(i)
#    cv2.polylines(image[:, :, ::-1], [box.astype(np.int32).reshape((-1, 1, 2))], True, color=(255, 255, 0), thickness=1)
#    cv2.imwrite(im_name, image[:, :, ::-1])
#    boxs = []
#        im_path = base_dir + line[0]
#            image = cv2.imread(im_path)[:, :, ::-1]
#            print(line[0])
#            box[0][0] = int(line[1])
#            box[0][1] = int(line[2])
#            box[1][0] = int(line[3])
#            box[1][1] = int(line[4])
#            box[2][0] = int(line[5])
#            box[2][1] = int(line[6])
#            box[3][0] = int(line[7])
#            box[3][1] = int(line[8])
#    #        print('box:',box)     
#    #        cv2.polylines(image[:, :, ::-1], [box.astype(np.int32).reshape((-1, 1, 2))], True, color=(255, 255, 0), thickness=1)
#        cv2.imwrite(out_dir + img_name , image[:, :, ::-1])
    #        if img_name not in name:
    #            name.append(line[0])
    #            boxs.append(box)
    #        
    #        box = box = np.zeros((4,2))
    #        
    #        print(boxs)
    #        print(box)
    #        for li in line[1:-1]:
    ##            box.append(li)
    #            print(li)
