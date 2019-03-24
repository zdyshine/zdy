# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:38:13 2019

@author: 我自人间来
使用imgaug做在线数据增强（需要找到主程序数据传入口。即有cv2.imread或别的读入信息）
返回的即使cv2可以直接使用的图片格式

低下有使用cv2做的数据增强
"""


#import tensorflow as tf
import cv2 
import random
import os
#import numpy as np
index = random.randint(1,100)
#
#file_name = os.listdir('./tem/')
#out_dir = './out_img/'
#base_dir = './tem/'

file_name = os.listdir('./label_img/')
out_dir = './label_img/'
base_dir = './label_img/'

# aug = iaa.Sharpen(alpha=(0.0, 1.0), lightness=(0.75, 2.0))
#aug = iaa.Emboss(alpha=(0.0, 1.0), strength=(0.5, 1.5))
#aug = iaa.Add((-40, 40))
#aug = iaa.Multiply((0.5, 1.5), per_channel=0.5)
#aug = iaa.Multiply((0.5, 1.5))
#aug = iaa.PiecewiseAffine(scale=(0.01, 0.05))

#视频特定颜色追踪
import cv2 as cv
import numpy as np
from imgaug import augmenters as iaa

def augumentor(image):
    sometimes = lambda aug: iaa.Sometimes(0.5, aug)  # 建立lambda表达式，
    seq = iaa.Sequential(
        [

            iaa.SomeOf((0, 5),
                       [
                           sometimes(iaa.GaussianBlur(sigma=(0, 0.5))),

                           # 锐化处理
                           sometimes(iaa.Sharpen(alpha=(0, 1.0), lightness=(0.75, 1.5))),

                           iaa.Affine(rotate=(-1.5, 1.5)),

                           # 加入高斯噪声
                           iaa.AdditiveGaussianNoise(
                               loc=0, scale=(0.0, 0.05 * 255), per_channel=0.5
                           ),

                           # 每个像素随机加减-10到10之间的数
                           iaa.Add((-10, 10)),

                           # 像素乘上0.5或者1.5之间的数字.
                           iaa.Multiply((0.75, 1.25)),

                           # 将整个图像的对比度变为原来的一半或者二倍
                           iaa.ContrastNormalization((0.6, 1.5)),
                       
#                            改变某一通道的值
                            iaa.WithChannels(1, iaa.Add((10, 50))),
                               
#                            灰度
                           iaa.Grayscale(alpha=(0.0, 1.0)),
                           
#                            加钢印
                           iaa.Emboss(alpha=(0.0, 1.0), strength=(0.5, 1.5)),

#                            扭曲图像的局部区域
                           sometimes(iaa.PiecewiseAffine(scale=(0.01, 0.03)))
                       ],

                       random_order=True  # 随机的顺序把这些操作用在图像上
                       )
        ],
        random_order=True  # 随机的顺序把这些操作用在图像上
    )

    image_aug = seq.augment_image(image)
    return image_aug


#def img_trans(img):
#    seq = iaa.Sequential([
##            iaa.PiecewiseAffine(scale=(0.01, 0.03)) 
##            iaa.ContrastNormalization((0.6, 1.5))
##            iaa.Multiply((0.75, 1.25))
##            iaa.Affine(rotate=(-1.5, 1.5))
##            iaa.Sharpen(alpha=(0, 1.0), lightness=(0.75, 1.5))
##            iaa.AdditiveGaussianNoise(
##                               loc=0, scale=(0.0, 0.05 * 255), per_channel=0.5
##                           )
##            iaa.WithChannels(1, iaa.Add((10, 50)))
##            iaa.Grayscale(alpha=(0.0, 1.0))
##            iaa.Emboss(alpha=(0.0, 1.0), strength=(0.5, 1.5))
#            iaa.EdgeDetect(alpha=(0.0, 1.0))
#            ]) 
#    image_aug = seq.augment_image(img)
#    return image_aug



for img in file_name:
    img1 = cv2.imread(base_dir + img)
    imgdir = out_dir + img.replace('.jpg','')
    print(imgdir)
    image_aug=augumentor(img1)
#    image_aug = augumentor(img1)   
#    cv2.imwrite(imgdir + '.jpg',image_aug) 
    cv2.imwrite(imgdir + str(index) + '.jpg',image_aug)


#img=cv.imread('./err_train/img_calligraphy_100004_bg.jpg')
#hsv = augumentor(img)
#cv.imwrite('./err_train/ '+ str(index)+'.jpg', hsv)



#        cv.imshow("video",frame)
#        cv.imshow("mask", mask)
#        c = cv.waitKey(40)
#        if c == 27:      #按键Esc的ASCII码为27
##            break
#extrace_object_demo()
#cv.destroyAllWindows()

#通道的分离与合并以及某个通道值的修改
#import cv2 as cv
#src=cv.imread('./err_train/img_calligraphy_70090_bg.jpg')
#cv.namedWindow('first_image', cv.WINDOW_AUTOSIZE)
#cv.imshow('first_image', src)
#
##三通道分离形成单通道图片
#b, g, r =cv.split(src)
#cv.imshow("second_blue", b)
#cv.imshow("second_green", g)
#cv.imshow("second_red", r)
## 其中cv.imshow("second_red", r)可表示为r = cv2.split(src)[2]
#
##三个单通道合成一个三通道图片
##src = cv.merge([b, g, r])
##cv.imshow('changed_image', src)
#
##修改多通道里的某个通道的值0
#src[:, :, 0] = 0
#cv.imshow('modify_image', src)
#
#cv.waitKey(0)
#cv.destroyAllWindows()


#for img in file_name:
#    img1 = cv2.imread(base_dir + img)
#    img2 =  np.zeros([img1.shape[0],img1.shape[1],img1.shape[2]],img1.dtype)
#    imgdir = base_dir + img.replace('.jpg','')
#    print(imgdir)
#
#    Contrastimg = cv2.addWeighted(img1,1.5,img2,2,0)   # 调整对比度
#    brightness = cv2.addWeighted(img1,1,img2,2,40)     # 调整亮度
#    
#    cv2.imwrite(imgdir + str(index)+'.jpg',Contrastimg)
#    cv2.imwrite(imgdir + str(index+1)+'.jpg',brightness)
    
#with tf.Session() as sess:
#    for img in file_name:
#        original_image = cv2.imread(base_dir + img)
#        imgdir = base_dir + img.replace('.jpg','')
#        print(imgdir)
#    
#    #     通过随机因子调整图像的亮度
#        random_brightness_image = tf.image.random_brightness(original_image, 0.3)
#        
#        # 通过随机因子调整图像的对比度
#        random_contrast_image = tf.image.random_contrast(original_image, 0.2, 0.5 )
#        
#        # 通过随机因子调整RGB图像的色调
#        random_hue_image = tf.image.random_hue(original_image, 0.5)
#        
#        # 通过随机因子调整RGB图像的饱和度
#        random_saturation_image = tf.image.random_saturation(original_image, 0.3, 0.5)
#
#        random_brightness_image = sess.run(random_brightness_image)
#        cv2.imwrite(imgdir + str(index)+'.jpg',random_brightness_image)
#    
#        
#        random_contrast_image = sess.run(random_contrast_image)
#        cv2.imwrite(imgdir + str(index+1)+'.jpg',random_contrast_image)
#        
#        random_hue_image = sess.run(random_hue_image)
#        cv2.imwrite(imgdir + str(index+2)+'.jpg',random_hue_image)
#        
#        random_saturation_image = sess.run(random_saturation_image)
#        cv2.imwrite(imgdir +str(index+3)+'.jpg',random_saturation_image)
