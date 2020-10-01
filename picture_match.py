from PIL import Image
import math
import operator
from functools import reduce
import os

GOAL = []


def image_contrast(name1,name2):

    image1 = Image.open(name1)    # 指定图片路径
    image2 = Image.open(name2)

    h1 = image1.histogram()
    h2 = image2.histogram()

    result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    return result   #result==0.0表示一样

def get_goal():
    filepath0='./test/'
    pathdir0 = os.listdir(filepath0)
    filepath = './picture/'
    pathdir = os.listdir(filepath)
    for cur0 in pathdir0:
        name1 = os.path.join(filepath0,cur0)  #路径拼接成绝对路径
        print(cur0)
        for cur in pathdir:
            name2 = os.path.join(filepath,cur)
            if image_contrast(name1,name2)==0.0:
                GOAL.append(os.path.splitext(cur)[0])
                break
            #print(cur)

if __name__ == '__main__':
    
    get_goal()
    print(GOAL)
    
