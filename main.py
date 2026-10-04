'''Интеграл.
[a,b] = [0,1], n = 10, n = 100, n= 2000, f(x) = cos(x)*sin(x).
Изображения.
{angle = 20} {color =same, 100, 200} {shift = 4} {shuffle? = {b,g,g}}
{color_filter = {r,b}}
{alpha = 0.3} {betta = 0.2}
Используя массивы numpy написать программу, которая получает
новую матрицу путем деления строк матрицы на элементы побочной
диагонали.
'''

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import scipy.ndimage as ndimage
import time


def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        elapsed_ns = time.perf_counter_ns() - start_time
        elapsed_seconds = elapsed_ns / 1000000000
        print(f"Время исполнения функции {function.__name__}: {elapsed_seconds:.7f} секунд")
        return res
    return wrapped

def integ(x):
    return np.cos(x) * np.sin(x)

@time_of_function
def trapezoid_slices(f, a, b, n):
    x = np.linspace(a, b, n + 1)    #массив всех точек
    y = f(x)     #значение функции
    h = (b - a) / n     #шаг интегрирования
    integral = h * (y[0]/2 + y[-1]/2 + np.sum(y[1:-1]))     #вычисление интеграла
    return integral

@time_of_function
def trapezoid_cycle(f, a, b, n):
    x = np.linspace(a, b, n + 1) #массив всех точек
    y = f(x)  #значение функции
    h = (b - a) / n  # шаг интегрирования
    integral = 0
    integral += y[0] / 2 #первая точка с коэффициентом 1/2
    for i in range(1, n):
        integral += y[i]

    integral += y[-1] / 2 #последняя точка с коэффициентом 1/2

    return integral * h

@time_of_function
def rectangles(f, a, b, n):
    h = (b - a) / n  #шаг интегрирования
    x_mid = np.linspace(a + h/2, b - h/2, n) #массив всех средних точек
    return np.sum(f(x_mid)) * h

@time_of_function
def rectangles_cycle(f, a, b, n):
    h = (b - a) / n #шаг интегрирования
    total = 0.0

    for i in range(n):
        x_mid = a + (i + 0.5) * h    #вычисление средней точки для каждого интервала
        total += f(x_mid)

    return total * h


print("")
print("Представление интеграла с помощью среза в формате f-строки:")
res_slice_t_10 = trapezoid_slices(integ, 0, 1, 10)
print(f"Значение интеграла с 10 точками (метод трапцеий): {res_slice_t_10}")
res_slice_t_100 = trapezoid_slices(integ, 0, 1, 100)
print(f"Значение интеграла с 100 точками (метод трапцеий): {res_slice_t_100}")
res_slice_t_2000 = trapezoid_slices(integ, 0, 1, 2000)
print(f"Значение интеграла с 2000 точками (метод трапцеий): {res_slice_t_2000}")

res_slice_r_10 = rectangles(integ, 0, 1, 10)
print(f"Значение интеграла с 10 точками (метод прямоугольников): {res_slice_r_10}")
res_slice_r_100 = rectangles(integ, 0, 1, 100)
print(f"Значение интеграла с 100 точками (метод прямоугольников): {res_slice_r_100}")
res_slice_r_2000 = rectangles(integ, 0, 1, 2000)
print(f"Значение интеграла с 2000 точками (метод прямоугольников): {res_slice_r_2000}")
print("")
print("Представление интеграла с помощью среза в формате форматированной строки:")
print("Значение интеграла с 10 точками (метод трапеций): {:10.10e}".format(res_slice_t_10))
print("Значение интеграла с 100 точками (метод трапеций): {:10.10e}".format(res_slice_t_100))
print("Значение интеграла с 2000 точками (метод трапеций): {:10.10e}".format(res_slice_t_2000))
print("Значение интеграла с 10 точками (метод прямоугольников): {:10.10e}".format(res_slice_r_10))
print("Значение интеграла с 100 точками (метод прямоугольников): {:10.10e}".format(res_slice_r_100))
print("Значение интеграла с 2000 точками (метод прямоугольников): {:10.10e}".format(res_slice_r_2000))
print("")


print("")
print("Представление интеграла с помощью циклов в формате f-строки:")
res_cycle_t_10 = trapezoid_cycle(integ, 0, 1, 10)
print(f"Значение интеграла с 10 точками (метод трапцеий): {res_cycle_t_10}")
res_cycle_t_100 = trapezoid_cycle(integ, 0, 1, 100)
print(f"Значение интеграла с 100 точками (метод трапцеий): {res_cycle_t_100}")
res_cycle_t_2000 = trapezoid_cycle(integ, 0, 1, 2000)
print(f"Значение интеграла с 2000 точками (метод трапцеий): {res_cycle_t_2000}")

res_cycle_r_10 = rectangles_cycle(integ, 0, 1, 10)
print(f"Значение интеграла с 10 точками (метод прямоугольников): {res_cycle_r_10}")
res_cycle_r_100 = rectangles_cycle(integ, 0, 1, 100)
print(f"Значение интеграла с 100 точками (метод прямоугольников): {res_cycle_r_100}")
res_cycle_r_2000 = rectangles_cycle(integ, 0, 1, 2000)
print(f"Значение интеграла с 2000 точками (метод прямоугольников): {res_cycle_r_2000}")
print("")
print("Представление интеграла с помощью циклов в формате форматированной строки:")
print("Значение интеграла с 10 точками (метод трапеций): {:10.10e}".format(res_slice_t_10))
print("Значение интеграла с 100 точками (метод трапеций): {:10.10e}".format(res_slice_t_100))
print("Значение интеграла с 2000 точками (метод трапеций): {:10.10e}".format(res_slice_t_2000))
print("Значение интеграла с 10 точками (метод прямоугольников): {:10.10e}".format(res_slice_r_10))
print("Значение интеграла с 100 точками (метод прямоугольников): {:10.10e}".format(res_slice_r_100))
print("Значение интеграла с 2000 точками (метод прямоугольников): {:10.10e}".format(res_slice_r_2000))

x=np.linspace(0,1,100)
y = integ(x)
plt.plot(x, y, label="cos(x)*sin(x)", color="blue")
plt.title("Интеграл ")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()



image = Image.open("rgb.png").convert('RGB')   #открытие изображений

rotate_image = image.copy()
rotate_image20 = rotate_image.rotate(20, expand=True)   #поворот изображения на 20 градусов
plt.imshow(rotate_image20)                  #отображение изображения при помощи matplotlib
plt.title('Поворот на 20 градусов')
plt.axis('off')
plt.show()

original_image = image.copy()           #копирование оригинального изображения
img_array = np.array(original_image)    #преобразорвание изображение в массив numpy
height, width, channels = img_array.shape   #определние колчичества пикселей по высоте и ширине и количество цветовых каналов

center_y = height // 2      #нахождение центра по y
center_x = width // 2       #нахождение центра по x
cross_size = 100            #длина креста
shift = 4                   #параметр для сдвига
color = np.array([0, 100, 200])
image_slices = image.copy()
img_array_slices = np.array(image_slices)

horiz_y = center_y + shift      #координата для горизонтальной линии
img_array_slices[horiz_y,center_x - cross_size: center_x + cross_size + 1, :3] = color      #присваивание пикселям нужного цвета для рисования

vert_x = center_x               #координата для вертикальной линии
img_array_slices[center_y - cross_size + shift: center_y + cross_size + shift + 1, vert_x, :3] = color

image_with_slices = Image.fromarray(img_array_slices)       #преобразование из массива numpy обратно в изображение

fig, axes = plt.subplots(1, 2, figsize=(12, 6))     #отображение результата
axes[0].imshow(np.array(original_image))
axes[0].set_title('Исходное изображение')
axes[0].axis('off')

axes[1].imshow(img_array_slices)
axes[1].set_title('Рисование креста')
axes[1].axis('off')
plt.show()

image = Image.open("rgb.png")

img_reorded = image.copy()
np_image = np.array(img_reorded)

shuffle = ['b', 'g', 'g']
channel_map = {'r': 0, 'g': 1, 'b': 2}
shuffle_indices = [channel_map[name] for name in shuffle]

np_image_transposed = np_image.transpose(2, 0, 1)  #транспонирование таким образом, чтобы цветовые каналы были на первом месте

np_image_ordered = np_image_transposed[shuffle_indices]  #выбор каналов в нужном порядке

img_np_reordered = np_image_ordered.transpose(1, 2, 0)  #транспонирование обратно

img_reordered = Image.fromarray(img_np_reordered)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(np.array(image))
axes[0].set_title('Исходное изображение')
axes[0].axis('off')

axes[1].imshow(img_np_reordered)
axes[1].set_title('После перестановки каналов')
axes[1].axis('off')
plt.show()


converted_img = image.transpose(Image.ROTATE_90)
plt.imshow(converted_img)
plt.title('Поворот на 90 градусов')
plt.axis('off')
plt.show()

image2 = Image.open("palitra.png").convert('RGBA')

np_image2 = np.array(image2)
color_filter_names = ['r', 'b']  #каналы, которые нужно обнулить
color_filter_indices = [channel_map[name] for name in color_filter_names]   #преобразование в цифры указанных цветов

for ch in color_filter_indices:     #цикл для обнуления нужных каналов
    np_image2[..., ch] = 0

result_filter_image = Image.fromarray(np_image2)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(image2)
axes[0].set_title('Изображение до обнуления каналов')
axes[0].axis('off')

axes[1].imshow(result_filter_image)
axes[1].set_title('Изображение после обнуления каналов')
axes[1].axis('off')
plt.show()


cat = Image.open("kytsya.jpg").convert("RGB")
watermark = Image.open("watermark.png").convert("RGB")

copy_cat = cat.copy()
np_cat = np.array(copy_cat)
copy_watermark = watermark.copy()
np_watermark = np.array(copy_watermark)

miny = min(np_cat.shape[0], np_watermark.shape[0])      #нахождение минимальной высоты и ширины между изображениями для корректного наложения
minx = min(np_cat.shape[1], np_watermark.shape[1])

result = np_cat.copy()

mask = np_watermark[0:miny, -minx:] < 200       #маска для наложения

result[0:miny, -minx:] = (result[0:miny, -minx:] * (1 - mask) + np_watermark[0:miny, -minx:] * mask)    #наложение маски

result_image = Image.fromarray(result.astype(np.uint8))
fig, axes = plt.subplots(1, 3, figsize=(12, 6))
axes[0].imshow(cat)
axes[0].set_title('Исходное изображение')
axes[0].axis('off')

axes[1].imshow(watermark)
axes[1].set_title('Водяной знак')
axes[1].axis('off')

axes[2].imshow(result_image)
axes[2].set_title('Результат')
axes[2].axis('off')
plt.show()


image_array = np.array(image) / 255.0

image1 = image_array.copy()
image2 = image_array.copy()
noise1 = np.random.rand(*image1.shape) - 0.5
noise1 = noise1 * 0.2
image_noised1 = image1 + noise1     #зашумление изображения
image_noised1 = np.clip(image_noised1, 0, 1)    #нормализация значений  от 0 до 1
noise2 = np.random.rand(*image2.shape) - 0.5
noise2 = noise2 * 0.4
image_noised2 = image2 + noise2
image_noised2 = np.clip(image_noised2, 0, 1)

image_rand1 = image_noised1.transpose((2, 0, 1))    #применение сглаживания
image_filt1 = np.zeros_like(image_rand1)
for i in range(3):
    image_filt1[i] = ndimage.gaussian_filter(image_rand1[i], 1)
image_filt1 = image_filt1.transpose((1, 2, 0))
image_filt1 = np.clip(image_filt1, 0, 1)

image_rand2 = image_noised2.transpose((2, 0, 1))
image_filt2 = np.zeros_like(image_rand2)
for i in range(3):
    image_filt2[i] = ndimage.gaussian_filter(image_rand2[i], 1)
image_filt2 = image_filt2.transpose((1, 2, 0))
image_filt2 = np.clip(image_filt2, 0, 1)

diff1 = image_filt1 - image_array       #подсчет ошибок
abs_diff1 = np.abs(diff1)
mean_error1 = np.mean(abs_diff1) * 100

diff2 = image_filt2 - image_array
abs_diff2 = np.abs(diff2)
mean_error2 = np.mean(abs_diff2) * 100

fig, axes = plt.subplots(2, 3, figsize=(12, 6))

axes[0,0].imshow(image_array)
axes[0,0].set_title('Исходное изображение')
axes[0,0].axis('off')

axes[0,1].imshow(image_noised1)
axes[0,1].set_title('Зашумленное (уровень 0.2)')
axes[0,1].axis('off')

axes[0,2].imshow(image_filt1)
axes[0,2].set_title('Сглаженное')
axes[0,2].axis('off')

axes[1,0].imshow(image_array)
axes[1,0].set_title('Исходное изображение')
axes[1,0].axis('off')

axes[1,1].imshow(image_noised2)
axes[1,1].set_title('Зашумленное (уровень 0.4)')
axes[1,1].axis('off')

axes[1,2].imshow(image_filt2)
axes[1,2].set_title('Сглаженное')
axes[1,2].axis('off')
plt.show()

print("Результаты:")
print(f"Уровень шума 0.2: средняя ошибка = {mean_error1:.2f}%")
print(f"Уровень шума 0.4: средняя ошибка = {mean_error2:.2f}%")



matrix = np.array([[9, 12, 3], [6, 3, 21], [3, 18, 30]])

n = matrix.shape[0]
rows = np.arange(n)
cols = n - 1 - np.arange(n)

result = matrix.astype(float)
divisors = matrix[rows, cols]
result /= np.where(divisors != 0, divisors, 1)[:, np.newaxis]

print(f"Матрица: \n"
      f"{matrix}")
print(f"Результат:\n"
      f"{result}")