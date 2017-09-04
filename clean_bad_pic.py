from PIL import Image,ImageFilter,ImageDraw,ImageFont
from os import listdir

# im=Image.open('9.jpg')
# im_rotate=im.rotate(90)
# im_rotate.show()
# im_contour=im.filter(ImageFilter.CONTOUR)
# im_contour.show()
# im.show()
#
# print(im.format,im.size,im.mode)
# im2=im.filter(ImageFilter.BLUR)
# im2.save('cc.jpg')
# w,h=im.size
# print(w,h)

for filename in listdir('./'):
    if filename.endswith('.jpg'):
        try:
            img=Image.open('./'+filename)
            img.verify()
        except(IOError,SyntaxError) as e:
            print('Bad file',filename)


#     bValid=True
#     try:
#         v_ima = Image.open(file)
#         v_ima.verify()
#     except:
#         bValid = False
#     return bValid
#
#
#
#
# def is_valid_jpg(jpg_file):
#     '''
#     判断jpg文件是否完整
#     :param jpg_file:
#     :return:
#     '''
#     if jpg_file.split('.')[-1].lower()=='jpg':
#         with open(jpg_file,'rb') as f :
#             f.seek(-2,2)
#             return f.read()=='\xff\xd9'
#     else:
#         return True