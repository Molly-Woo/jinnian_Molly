from PIL import Image
import math
import operator
from functools import reduce
import os

GOAL = []

def get_goal():
    filepath0='./test/'
    pathdir0 = os.listdir(filepath0)
    
    for i in range(1,10):
        flag_goal = 0
        for cur0 in pathdir0:
            if str(os.path.splitext(cur0)[0]) == str(i):
                GOAL.append(i)
                flag_goal = 1
                break;
        if flag_goal == 0:
            GOAL.append(0)

if __name__ == '__main__':
    
    get_goal()
    print(GOAL)
    
