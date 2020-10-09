import heapq
import copy
import re
import datetime
import sys
from PIL import Image
import math
import operator
from functools import reduce
import os

BLOCK = [[0,0,0],[0,0,0],[0,0,0]]  # 给定状态
GOAL = [[0,0,0],[0,0,0],[0,0,0]]  # 目标状态

# 4个方向
direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# OPEN表
OPEN = []

# 节点的总数
SUM_NODE_NUM = 0

flag=0  #标记是否为第一次的位置
flag_ans = 0 #是否找到目标状态
operation = []    #操作序列
xx=-1
yy=-1
cnt=0
mark = 0
#求目标状态
def get_goal(block):    
    arr0 = block
    new1 = []
    new2 = []
    
    for i in range(3):
        for j in range(3):
            new1.append(arr0[i][j]);
                
    for i in range(1,10):
        flag_goal = 0
        for j in new1:
            if str(j) == str(i):
                new2.append(i)
                flag_goal = 1
                break;
        if flag_goal == 0:
            new2.append(0)
    new1 = new2
    num = 0
    for i in range(0,3):
        for j in range(0,3):
            GOAL[i][j] = new1[num]
            num+=1
    return GOAL

# 状态节点
class State(object):
    def __init__(self, gn=0, hn=0, state=None, hash_value=None, par=None):
        '''
        初始化
        :param gn: gn是初始化到现在的距离
        :param hn: 启发距离
        :param state: 节点存储的状态
        :param hash_value: 哈希值，用于判重
        :param par: 父节点指针
        '''
        self.gn = gn
        self.hn = hn
        self.fn = self.gn + self.hn
        self.child = []  # 孩子节点
        self.par = par  # 父节点
        self.state = state  # 局面状态
        self.hash_value = hash_value  # 哈希值

    def __lt__(self, other):  # 用于堆的比较，返回距离最小的
        return self.fn < other.fn

    def __eq__(self, other):  # 相等的判断
        return self.hash_value == other.hash_value

    def __ne__(self, other):  # 不等的判断
        return not self.__eq__(other)


def manhattan_dis(cur_node, end_node):
    '''
    计算曼哈顿距离
    :param cur_state: 当前状态
    :return: 到目的状态的曼哈顿距离
    '''
    cur_state = cur_node.state
    end_state = end_node.state
    dist = 0
    N = len(cur_state)
    for i in range(N):
        for j in range(N):
            if cur_state[i][j] == end_state[i][j]:
                continue
            num = cur_state[i][j]
            if num == 0:
                x = N - 1
                y = N - 1
            else:
                x = num / N  # 理论横坐标
                y = num - N * x - 1  # 理论的纵坐标
            dist += (abs(x - i) + abs(y - j))

    return dist


def test_fn(cur_node, end_node):
    return 0


def generate_child(cur_node, end_node, hash_set, open_table, dis_fn):
    '''
    生成子节点函数
    :param cur_node:  当前节点
    :param end_node:  最终状态节点
    :param hash_set:  哈希表，用于判重
    :param open_table: OPEN表
    :param dis_fn: 距离函数
    :return: None
    '''
    if cur_node == end_node:
        heapq.heappush(open_table, end_node)
        return
    num = len(cur_node.state)
    for i in range(0, num):
        for j in range(0, num):
            if cur_node.state[i][j] != 0:
                continue
            for d in direction:  # 四个偏移方向
                x = i + d[0]
                y = j + d[1]
                if x < 0 or x >= num or y < 0 or y >= num:  # 越界了
                    continue
                # 记录扩展节点的个数
                global SUM_NODE_NUM
                SUM_NODE_NUM += 1

                state = copy.deepcopy(cur_node.state)  # 复制父节点的状态
                state[i][j], state[x][y] = state[x][y], state[i][j]  # 交换位置
                h = hash(str(state))  # 哈希时要先转换成字符串
                if h in hash_set:  # 重复了
                    continue
                hash_set.add(h)  # 加入哈希表
                gn = cur_node.gn + 1  # 已经走的距离函数
                hn = dis_fn(cur_node, end_node)  # 启发的距离函数
                node = State(gn, hn, state, h, cur_node)  # 新建节点
                cur_node.child.append(node)  # 加入到孩子队列
                heapq.heappush(open_table, node)  # 加入到堆中

#强制交换
def swap(a,b,blo):
    blo[int((a-1)/3)][(a-1)%3],blo[int((b-1)/3)][(b-1)%3]=blo[int((b-1)/3)][(b-1)%3],blo[int((a-1)/3)][(a-1)%3]
    
    print("强制交换后 ： ")
    for i in blo:
        print(i)
    flag = 0
    start(blo,10000,10,10)
    
#计算逆序对1
def inverse_number(arr):
    ans = 0
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] > arr[i]:
                ans += 1
    return ans

#计算逆序对2
def Reverse_pair(block):
    
    arr0 = block
    arr = []
        
    for i in range(3):
        for j in range(3):
            if arr0[i][j]!=0:
                arr.append(arr0[i][j]);

    print("逆序对：",inverse_number(arr))
    if inverse_number(arr)%2==0:
        return True;
    else:
        return False


#自由交换
free_change1 = 0    #自由交换的位置
free_change2 = 0
def free_change(block0):
    global free_change1
    global free_change2
    for i in range(0,3):
        for j in range(0,2):
            if block0[i][j]!=0 and block0[i][j+1]!=0 and j+1<3:
                block0[i][j],block0[i][j+1] = block0[i][j+1],block0[i][j]

                free_change1 = i*3+j+1
                free_change2 = i*3+j+2
                
                print("自由交换后 ：")
                for i in block0:
                    print(i)
                flag = 1   
                return block0;
#强制交换前                
def before_swap(block,step,a,b):
    global cnt
    flag2 = 0
    if step%2 != 0:
        for i in range(0,3):
            for j in range(0,3):
                if block[i][j]==0 and i-1>=0:
                    block[i][j],block[i-1][j]=block[i-1][j],block[i][j]
                    flag2 = 1
                    operation.append('ws'*int(step/2)+'w')
                    print('ws'*int(step/2)+'d')
                    break
                elif block[i][j]==0 and i+1<=2:
                    block[i][j],block[i+1][j]=block[i+1][j],block[i][j]
                    flag2 = 1
                    operation.append('sw'*int(step/2)+'s')
                    print('sw'*int(step/2)+'a')
                    break
                elif block[i][j]==0 and j-1>=0:
                    block[i][j],block[i][j-1]=block[i][j-1],block[i][j]
                    flag2 = 1
                    operation.append('ad'*int(step/2)+'a')
                    print('ad'*int(step/2)+'s')
                    break
                elif block[i][j]==0 and j+1<=2:
                    block[i][j],block[i][j+1]=block[i][j+1],block[i][j]
                    flag2 = 1
                    operation.append('da'*int(step/2)+'d')
                    print('da'*int(step/2)+'w')
                    break
            if flag2 == 1:
                break
    else:
        for i in range(0,3):
            for j in range(0,3):
                if block[i][j]==0 and i-1>=0:
                    flag2 = 1
                    operation.append('ws'*int(step/2))
                    print('ws'*int(step/2))
                    break
                elif block[i][j]==0 and i+1<=2:
                    flag2 = 1
                    operation.append('sw'*int(step/2))
                    print('sw'*int(step/2))
                    break
                elif block[i][j]==0 and j-1>=0:
                    flag2 = 1
                    operation.append('ad'*int(step/2))
                    print('ad'*int(step/2))
                    break
                elif block[i][j]==0 and j+1<=2:
                    flag2 = 1
                    operation.append('da'*int(step/2))
                    print('da'*int(step/2))
                    break
            if flag2 == 1:
                break
    cnt += step
    swap(a,b,block)

def print_path(node,step,a,b):
    '''
    输出路径
    :param node: 最终的节点
    :return: None
    '''
    num = node.gn
    
        
    def show_block(block,step,a,b):
        global flag
        global xx
        global yy
        global cnt
        global mark
        
        print("---------------")
        for b0 in block:
            print(b0)
        
        cnt+=1
        #输出操作序列
        for i in range(3):
            for j in range(3):
                if block[i][j]==0:
                    '''
                    print(xx)
                    print(yy)
                    print("flag_ans：",flag_ans)
                    '''
                    if flag==0:
                        xx=i
                        yy=j
                        flag=1;
                    elif cnt!=step+2:
                        if xx==i and yy>j and flag_ans==0:
                            print("a")
                            operation.append("a")
                        elif xx==i and yy<j and flag_ans==0:
                            print("d")
                            operation.append("d")
                        elif xx<i and yy==j and flag_ans==0:
                            print("s")
                            operation.append("s")
                        elif xx>i and yy==j and flag_ans==0:
                            print("w")
                            operation.append("w")
                    xx=i
                    yy=j
                    
        if cnt==step+1:
            swap(a,b,block)
            mark = 1
        '''
        if block==GOAL:
            print("Got it!  ")
            print("swap:",free_change1,free_change2)
            print("Operations：")
            for x in operation:
                print(x,end = '')
            print()
            #sys.exit(0);
        '''
    stack = []  # 模拟栈
    stack.clear()
    while node.par is not None:
        stack.append(node.state)
        node = node.par
    stack.append(node.state)
    while len(stack) != 0:
        t = stack.pop()
        show_block(t,step,a,b)
        
        if flag_ans ==1 or mark==1:
            break
        
    return num


def A_start(step,a,b,start, end, distance_fn, generate_child_fn, time_limit=10):
    '''
    A*算法
    :param start: 起始状态
    :param end: 终止状态
    :param distance_fn: 距离函数，可以使用自定义的
    :param generate_child_fn: 产生孩子节点的函数
    :param time_limit: 时间限制，默认10秒
    :return: None
    '''
    OPEN = []
    root = State(0, 0, start, hash(str(BLOCK)), None)  # 根节点
    end_state = State(0, 0, end, hash(str(GOAL)), None)  # 最后的节点
    '''
    if root == end_state:
        print("start == end !")
    '''
    OPEN.append(root)
    heapq.heapify(OPEN)

    node_hash_set = set()  # 存储节点的哈希值
    node_hash_set.add(root.hash_value)
    #start_time = datetime.datetime.now()
    while len(OPEN) != 0:
        top = heapq.heappop(OPEN)
        if top == end_state:  # 结束后直接输出路径
            return print_path(top,step,a,b)
        # 产生孩子节点，孩子节点加入OPEN表
        generate_child_fn(cur_node=top, end_node=end_state, hash_set=node_hash_set,
                          open_table=OPEN, dis_fn=distance_fn)
        '''
        cur_time = datetime.datetime.now()
        # 超时处理
        if (cur_time - start_time).seconds > time_limit:
            print("Time running out, break !")
            print("Number of nodes:", SUM_NODE_NUM)
            return -1
        '''
    '''
    print("No road !")  # 没有路径
    '''
    return -1

    
def start(BLOCK,step,a,b):
    global cnt
    flag=0
    NUMBER = 3  #N的取值
    GOAL = get_goal(BLOCK)
    print("GOAL:",GOAL)
    OPEN = []  # 这里别忘了清空
    #BLOCK = []
    #read_block(BLOCK, line, NUMBER)
    SUM_NODE_NUM = 0
    if Reverse_pair(BLOCK):
        #print("有解")
        flag=0
        OPEN = []
    else:
        
        print("无解")
        if cnt == 0:
            before_swap(BLOCK,step,a,b)
        else:
            print("自由交换前 ： ")
            print(BLOCK)
        
            BLOCK=free_change(BLOCK)
            flag=0
            OPEN = [];
    '''
    start_t = datetime.datetime.now()
    '''
    # 这里添加5秒超时处理，可以根据实际情况选择启发函数
    length = A_start(step,a,b,BLOCK, GOAL, manhattan_dis, generate_child, time_limit=10)
    '''    
    end_t = datetime.datetime.now()
    if length != -1:
        print("length =", length)
        print("time = ", (end_t - start_t).total_seconds(), "s")
        print("Nodes =", SUM_NODE_NUM)
    '''
    ans_operation = ''.join(operation)
    print("ans_operation：",ans_operation)
    global flag_ans
    flag_ans = 1
    #print("flag_ans：",flag_ans)
    return ans_operation,free_change1,free_change2

if __name__ == '__main__':
    BLOCK = [[0, 1, 2], [6, 3, 7], [9, 5, 8]]
    print(start(BLOCK,8,3,7))   #step=2,a=2,b=3

