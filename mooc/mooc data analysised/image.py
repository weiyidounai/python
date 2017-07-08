#图像表示
# RGB形成的颜色包括了人类视力所能感知的所有颜色(PIL库）
from PIL import Image
import numpy as np;
#图像是像素组成的二维矩阵，每个元素是一个矩阵
# im = np.array(Image.open("D:\wcc.jpg", "r"))
# print(im.shape, im.dtype)
# print('\n')
# #图像的变换
# a = np.array(Image.open("D:\wcc.jpg"))
# print(a.shape, a.dtype)
# b = [255, 255, 255] -a
# im = Image.fromarray(b.astype('uint8'))
# im.save("D:\wcc1.jpg")

# a = np.array(Image.open("D:\wcc.jpg").convert('L'))
# b = 255 -a
# im = Image.fromarray(b.astype('uint8'))
# im.save("D:\wcc2.jpg")

# a = np.array(Image.open("D:\wcc.jpg").convert('L'))
# c = (100/255)*a + 150 #区间变化
# im = Image.fromarray(c.astype('uint8'))
# im.save("D:\wcc3.jpg")

# a = np.array(Image.open("D:\wcc.jpg").convert('L'))
# d = 255*(a/255)**a #像素平方
# im = Image.fromarray(d.astype('uint8'))
# im.save("D:\wcc4.jpg")

# 图像的手绘效果
a = np.asarray(Image.open("D:\wcc.jpg").convert('L')).astype('float')

depth = 10.  # (0-100)
grad = np.gradient(a)  # 取图像灰度的梯度值
grad_x, grad_y = grad  # 分别取横纵图像梯度值
grad_x = grad_x * depth / 100.
grad_y = grad_y * depth / 100.
A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
uni_x = grad_x / A
uni_y = grad_y / A
uni_z = 1. / A

vec_el = np.pi / 2.2  # 光源的俯视角度，弧度值
vec_az = np.pi / 4.  # 光源的方位角度，弧度值
dx = np.cos(vec_el) * np.cos(vec_az)  # 光源对x 轴的影响
dy = np.cos(vec_el) * np.sin(vec_az)  # 光源对y 轴的影响
dz = np.sin(vec_el)  # 光源对z 轴的影响

b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)  # 光源归一化
b = b.clip(0, 255)

im = Image.fromarray(b.astype('uint8'))  # 重构图像
im.save("D:\wccshouhui.jpg")