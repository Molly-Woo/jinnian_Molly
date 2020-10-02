import function.getsend as getsendfunction
import function.check_picture as checkpicturefunction
import function.cut as picturecutfunction
import base64
import os
from PIL import Image
import cv2
import function.eight as eightfunction

if __name__ == '__main__':
    getdata = getsendfunction.getpicture()
    step = getdata['step']
    swap = getdata['swap']
    uuid = getdata['uuid']
    image_byte = base64.b64decode(getdata['img'])
    image_json = open("a.jpg", 'wb')
    image_json.write(image_byte)
    image_json.close()

    image = Image.open('a.jpg')
    image_list = picturecutfunction.cut_image(image)
    picturecutfunction.save_images(image_list, ord('a'))

    pathtest = "./test/"
    pathsuffix = ".png"
    pathfile = "picture/"
    picture_order = 0
    for i in range (ord("a") , ord("i")+1) :
        path1 = pathtest + chr(i) +pathsuffix
        same_number = 0
        for j in range (324) :
            path2 = pathfile + str(j) + pathsuffix
            result = checkpicturefunction.image_contrast(path1, path2)
            if result == 0.0:
                #print(j)
                picture_order = j
                same_number += 1
        if same_number == 1 :
            picture_order //= 9
            break

    targets = []
    for i in range(ord("a"), ord("i") + 1):
        path1 = pathtest + chr(i) + pathsuffix
        flag = 0
        for j in range(picture_order * 9 , picture_order * 9 + 9):
            path2 = pathfile + str(j) + pathsuffix
            result = checkpicturefunction.image_contrast(path1, path2)
            if result == 0.0 :
                targets.append(j % 9 + 1)
                flag = 1
                break
        if flag == 0 :
            targets.append(0)
    #print(targets)

    result = eightfunction.start(step , swap[0] , swap[1])
    thepath = result[0]
    theswap = []
    theswap.append(0 , result[1])
    theswap.append(1 , result[2])
    getsendfunction.sendpicture(thepath, theswap, uuid)