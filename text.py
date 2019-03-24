# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:46:44 2019
获取csv文件的整行内容。并判断左上和右下的关系。
@author: jxufe
"""

import csv
import os
import shutil
res = {}
err = []
#base_dir = '/media/zdy/新加卷/DYng_Z/2-text_detect/data'

def get_annotations(path):
  i = 0
  j = 0
  k = 0
  with open(path, "r", encoding = 'utf-8') as f:
    reader = csv.reader(f)
    for item in reader[0:]:
        with open('./verifyImage.txt', "a", encoding = 'utf-8') as f1:
                f1.write(item[0] + ' ' + item[1] + ' ' + item[2] + ' '  + item[3] + ' ' + item[4] + ' '  + item[5] + ' '  + item[6] + ' ' + item[7] + ' ' + item[8]+'\n')
#                f1.write(item[0] + '\n')
#        print(item[0])
#        
#        if not item[0].endswith('jpg'):
#          continue
#        x1 = item[1]
#        y1 = item[2]
#        x2 = item[3]
#        y2 = item[4]
#        x3 = item[5]
#        y3 = item[6]
#        x4 = item[7]
#        y4 = item[8]
#        
##        print(int(x1)-int(x2))
##        print(x1,y1,x2,y2,x3,y3,x4,y4)
#        xa = int(x3) - int(x1)
#        xb = int(x2) - int(x1)
#        ya = int(y4) - int(y1)
#        yb = int(y3) - int(y1)
#        if xa<0 or yb<0 or xb<0 or ya<0:
#            a = item[1]
#            b = item[2]
#            item[1] = item[3]
#            item[2] = item[4]
#            
#            item[3] = item[5]
#            item[4] = item[6]
#            
#            item[5] = item[7]
#            item[6] = item[8]
#            
#            item[7] = a
#            item[8] = b
#            if item[0] not in err:
#                err.append(item[0])
#            i+=1
#            with open('./label_error1.txt', "a", encoding = 'utf-8') as f1:
#                f1.write(item[0] + ' ' + item[1] + ' ' + item[2] + ' '  + item[3] + ' ' + item[4] + ' '  + item[5] + ' '  + item[6] + ' ' + item[7] + ' ' + item[8] + ' '  +'\n')
#                f1.write(item[0] + '\n')
            
#        else:
#            j+=1
##            continue
#        if item[0] not in res:
##          with open('./label_trye.txt', "a", encoding = 'utf-8') as f2:
##              f2.write(item[0] + '\n')
#          k+=1
#          res[item[0]] = []
#        res[item[0]].append(item[1:])
#  print(i)
#  print(j)
#  print(k)
#  print(err)
#  for er in err:
#      shutil.move('./verifyImage/'+er, './err_train/'+er)
##      with open('./error.txt', "a", encoding = 'utf-8') as f3:
##                f3.write(er +'\n')
#  return res

def write_txt(d, path):
  for name, objects in d.items():
    name = name.split('.')[0] + '.txt'
    with open(os.path.join(path, name), 'w') as f:
      for ob in objects:
        f.write(','.join(ob) + '\n')


if __name__ == '__main__':
  path ='./verify_lable.csv'
  save_path ='./trian_dataset/'
  d = get_annotations(path)
#  write_txt(d, save_path)
  
'''
a = item[1]
b = item[2]
item[1] = item[3]
item[2] = item[4]

item[3] = item[5]
item[4] = item[6]

item[5] = item[7]
item[6] = item[8]

item[7] = a
item[8] = b
'''
