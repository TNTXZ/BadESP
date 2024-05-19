from PIL import Image
w = input("宽度 ")
h = input("高度 ")
def resize_pbm(input_file, output_file, size):
    with Image.open(input_file) as img:
        resized_img = img.resize(size)
        resized_img.save(output_file)
for i in range(1,3285):
    resize_pbm(str(i)+'.pbm', str(i)+'.pbm', (int(w), int(h)))
    print('成功执行文件'+str(i)+'.pbm')
