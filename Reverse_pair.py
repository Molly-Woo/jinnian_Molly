def inverse_number(arr):
    ans = 0
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] > arr[i]:
                ans += 1
    return ans

def Reverse_pair():
    
    arr0 = [[1,6,3],[4,5,0],[8,7,2]]
    arr = []
        
    for i in range(3):
        for j in range(3):
            if arr0[i][j]!=0:
                arr.append(arr0[i][j]);

    if inverse_number(arr)%2==0:
        return True;
    else:
        return False

if Reverse_pair():
    print("有解")
else:
    print("无解")

