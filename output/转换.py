from PIL import Image
def convert_png_to_pbm(png_file, pbm_file):
    with Image.open(png_file) as img:
        img = img.convert('1')
        img.save(pbm_file)
for i in range(1,3287):
    convert_png_to_pbm(str(i)+'.png', str(i)+'.pbm')
    print('save image:'+str(i))
