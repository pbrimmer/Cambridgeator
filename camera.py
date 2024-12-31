from PIL import Image

img = Image.open('outdoor-christmas.jpg')
pixels = img.load() 
width, height = img.size

colmax = 16777215

for y in range(height):      # this row
    for x in range(width):   # and this row was exchanged
        r, g, b = pixels[x, y]
        
        # in case your image has an alpha channel
        # r, g, b, a = pixels[x, y]

        print(x, y, f"#{r:02x}{g:02x}{b:02x}",float(int(f"{r:02x}{g:02x}{b:02x}",16))/colmax)

print('---')
print(int('000000',16))
print(int('FFFFFF',16))
