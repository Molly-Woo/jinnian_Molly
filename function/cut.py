from PIL import Image
import os

def get_fileNames(rootdir):
	fs = []
	for root, dirs, files in os.walk(rootdir,topdown = True):
		for name in files:
			_, ending = os.path.splitext(name)
			if ending == ".jpg":
					fs.append(os.path.join(root,name))
	return fs

def cut_image(image):
    width, height = image.size
    item_width = int(width / 3)
    box_list = []
    # (left, upper, right, lower)
    for i in range(0,3):
        for j in range(0,3):
            #print((i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width))
            box = (j*item_width,i*item_width,(j+1)*item_width,(i+1)*item_width)
            box_list.append(box)
    image_list = [image.crop(box) for box in box_list]
    return image_list
#保存
def save_images(image_list , index):
    #save_path = "../picture/"#文件存储路径
    save_path = "./test/"
    for image in image_list:
        image.save(save_path + chr(index) + '.png', 'PNG')
        index += 1

if __name__ == '__main__':
    '''
    a = get_fileNames("无框字符")
    index = 0
    for i in range (len(a)) :
        image = Image.open(a[i])
        image_list = cut_image(image)
        save_images(image_list , index)
        index += 9
    '''
    image = Image.open('../a.jpg')
    image_list = cut_image(image)
    save_images(image_list, ord('a'))