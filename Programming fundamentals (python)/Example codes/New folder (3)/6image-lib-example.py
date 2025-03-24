# https://pythonexamples.org/python-pillow/
from PIL import Image

def newImg():
    img = Image.new('RGB', (30, 40))
    img.putpixel((25, 30), (255, 0, 0))
    img.rectangle((200, 125, 300, 200), fill=(255, 0, 0), outline=(0, 255, 0))
    #img.save(r'C:\Users\idrees\Desktop\sqr.png')

    return img

newImg().show()
newImg().resize((750, 900)).show()
newImg().rotate(45).show()

filename = "Idrees.jpg"
with Image.open(filename) as img:
    img.load()

print(type(img))

print(isinstance(img, Image.Image))

#img.show()
img.rotate(15).show()



'''

Python Imaging library

python -m pip install Pillow


https://realpython.com/image-processing-with-the-python-pillow-library/

'''