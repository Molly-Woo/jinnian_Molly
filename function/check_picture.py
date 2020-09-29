from PIL import Image
import math
import operator
from functools import reduce

def image_contrast():

    image1 = Image.open("a.jpg")    # 指定图片路径
    image2 = Image.open("b.jpg")

    h1 = image1.histogram()
    h2 = image2.histogram()

    result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    return result   #result==0.0表示一样

if __name__ == '__main__':
    
    result = image_contrast()
    if result==0.0:
        print("一样")
    else:
        print("不一样")
    
