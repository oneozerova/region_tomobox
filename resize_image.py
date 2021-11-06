from PIL import Image

img = Image.open('unicorn_other_side.out.jpg')
new_img = img.resize((80, 80))
new_img.save("80p_unicorn_other_side.jpg", "JPEG", optimize=True)
