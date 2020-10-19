import unittest
from PIL import Image
import function.check_picture as f_checkPicture
import function.cut as f_cut
import function.eight as  f_eight

x = {}
x['0.png'] = '0.png'
x['1.png'] = '1.png'
x['2.png'] = '2.png'
x['3.png'] = '3.png'
x['4.png'] = '4.png'
x['5.png'] = '5.png'
x['00.png'] = '00.png'

#此处代码与上面大同小异，故省略n行
class MyTestCase(unittest.TestCase):
    def test_cut(self):
        image = Image.open('a.jpg')
        image_list = f_cut.cut_image(image)
        print("图片切割成功")
        index = 0
        for image in image_list:
            image.save(str(index) + '.png', 'PNG')
            index += 1
            print("第" + str(index) + "张图片保存成功")

    @staticmethod
    def test_checkPicture():
        for i in x.keys():
            if x[i] != '':
                ans = f_checkPicture.image_contrast(x['00.png'], x[i])
                print('样本：%s，误差率为：%.2f' % (i, ans))

    def test_eight(self):
        BLOCK = [[0, 5, 1], [9, 3, 6], [2, 4, 8]]
        f_eight.start(BLOCK, 8, 6, 3)  # step=2,a=2,b=3

if __name__ == '__main__':
    unittest.main()
