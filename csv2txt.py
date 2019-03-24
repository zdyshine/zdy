'''
华为文字识别大赛
把csv格式处理成txt格式
csv格式：
filename x1,y1,x2,y2,x3,y3,x4,y4,text
img_calligraphy_80011_bg.jpg, 4个坐标, 我自人间来

txt格式：
filename num a x1 y1 x2 y2 a x1 y1 x2 y2...
./test_image/img_calligraphy_85886_bg.jpg 1 a 20 52 68 227
./test_image/img_calligraphy_87888_bg.jpg 3 a 104 54 149 298 a 56 59 104 295 a 22 57 64 185
@author 我自人间来
'''
import pandas as pd
import numpy as np
import cv2
import codecs
# data = pd.read_table("./train_labels.csv", sep=",")
# image_names = data['ID'].tolist()
# image_names = list(set(image_names))


def to_widerface(image_names, save_path):
    result = open(save_path, 'w')
    for name in image_names:
        image_path = './images/'+name
        points_list = np.array(data[data['ID'] == name][' Detection'])
        result.write(image_path + ' ' + str(len(points_list)))
        for points in points_list:
            points = points.split(' ')
            result.writelines(
                [' ', str(points[0]), ' ', str(points[1]), ' ', str(int(points[2]) - int(points[0])), ' ', str(int(points[3]) - int(points[1])), ' '])
            result.write("1")
        result.write("\n")
    result.close()

def to_coco(image_names, data, save_path):
    result = open(save_path, 'w')
    for name in image_names:
        image_path = './test_image/' + name
        x1 = np.array(data[data['filename'] == name]['x1'])
        y1 = np.array(data[data['filename'] == name]['y1'])
        x3 = np.array(data[data['filename'] == name]['x3'])
        y3 = np.array(data[data['filename'] == name]['y3'])
        w = x3 - x1
        h = y3 - y1
        if all(np.array(w)>0) and all(np.array(h)>0):
            points_list = []
#            print(x1.shape[0])
            for i in range(x1.shape[0]):
                points_list.append([x1[i], y1[i], x3[i], y3[i]])
                if len(points_list) == x1.shape[0]:                
                    result.write(image_path + ' ' + str(len(points_list)))
                    for points in points_list:
                        result.writelines(
                            [' ', 'a', ' ', str(points[0]), ' ', str(points[1]), ' ', str(points[2]), ' ', str(points[3])])
                    result.write("\n")
                else:
                    continue
        else:
            continue
    result.close()

def data_process(image_names, data, save_path):
    # delete the data with the wrong marking format

    problem_name_list = []
    for name in image_names:

        x1 = np.array(data[data['filename'] == name]['x1'])
        y1 = np.array(data[data['filename'] == name]['y1'])
        x3 = np.array(data[data['filename'] == name]['x3'])
        y3 = np.array(data[data['filename'] == name]['y3'])
        w = x3 - x1
        h = y3 - y1
        if all(np.array(w)>0) and all(np.array(h)>0):
            problem_name_list.append(name)
        else:
            continue



if __name__ == '__main__':
#    image_names = []
#    datas = []
    data = pd.read_table("./submission2.csv", sep=",")
    image_names = data['filename'].tolist()
#    with open('./123.txt','r') as f:
#        lines = f.readlines()
#        for line in lines:
#            image_name = line.split(',')[0]
#            data = line.split(',')[0:-1]
#            image_names.append(image_name)
#            datas.append(data)
    image_names = list(set(image_names))
#    print(image_names)
    to_coco(image_names, data, './submission_label2.txt')
#    to_widerface(image_names, './verify_lable.txt')
