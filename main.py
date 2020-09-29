import function.getsend as fg
import base64

if __name__ == '__main__':
    r = fg.getpicture()
    image_byte = base64.b64decode(r['img'])
    image_json = open("a.jpg", 'wb')
    image_json.write(image_byte)
    image_json.close()