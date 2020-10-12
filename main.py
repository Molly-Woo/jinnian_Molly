import function.getsend as gs_function
import function.check_picture as check_function
import function.cut as cut_function
import function.eight as eight_function
import base64
from PIL import Image

if __name__ == '__main__':
    get_data = gs_function.getpicture()#从接口获取图片
    step = get_data['step']
    swap = get_data['swap']
    uuid = get_data['uuid']
    image_byte = base64.b64decode(get_data['img'])
    image_json = open("a.jpg", 'wb')
    image_json.write(image_byte)
    image_json.close()

    image = Image.open('a.jpg')#对图片进行切割
    image_list = cut_function.cut_image(image)
    cut_function.save_images(image_list, ord('a'))

    path_test = "./test/"#查找可以与图片相匹配的字符
    path_suffix = ".png"
    path_file = "picture/"
    picture_order = 0
    for i in range (ord("a") , ord("i")+1) :
        path1 = path_test + chr(i) + path_suffix
        same_number = 0
        for j in range (324) :
            path2 = path_file + str(j) + path_suffix
            result = check_function.image_contrast(path1, path2)
            if result == 0.0:
                #print(j)
                picture_order = j
                same_number += 1
        if same_number == 1 :
            picture_order //= 9
            break

    targets = []
    for i in range(ord("a"), ord("i") + 1):#匹配图片和字符块，得到图片排列顺序
        path1 = path_test + chr(i) + path_suffix
        flag = 0
        for j in range(picture_order * 9 , picture_order * 9 + 9):
            path2 = path_file + str(j) + path_suffix
            result = check_function.image_contrast(path1, path2)
            if result == 0.0 :
                targets.append(j % 9 + 1)
                flag = 1
                break
        if flag == 0 :
            targets.append(0)
    #print(targets)

    block = [[] , [] , []]
    for i in range (0 , 3) :
        for j in range (0 , 3) :
            block[i].append(targets[i * 3 + j])

    result = eight_function.start(block, step, swap[0], swap[1])#调用A*算法，获取路径
    print(result)

    result_path = result[0]
    result_path = "".join(result_path)
    result_swap = []
    result_swap.append(result[1])
    result_swap.append(result[2])
    gs_function.sendpicture(result_path, result_swap, uuid)#从接口提交路径答案