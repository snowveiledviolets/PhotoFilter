#!/usr/bin/env python3
#PhotoFilter.py

'''
Author: Wren Kohler
PhotoFilter.py
'''

import sys
import random

from PIL import Image

def open_image(filename):
    #Opens image and converts to RGB
    image = Image.open(filename)
    if image == None:
        print("Specified input file " + filename + " cannot be opened.")
        return Image.new("RGB", (400, 400))
    else:
        print(str(image.size) + " = " + str(len(image.getdata()))
              + " total pixels.")
        return image.convert("RGB")

def show_img(photo):
    #Returns photo with no changes
    return photo

def apply_filter(photo,filter_type):
    #Applies the filter passed to it
    pixels = [filter_type(p) for p in photo.getdata()]
    nim = Image.new("RGB", photo.size)
    nim.putdata(pixels)
    return nim

def apply_brighten(pixel):
    #Brightens picture by 10%
    (r, g, b) = pixel
    return (int(r * 1.1), int(g * 1.1), int(b * 1.1))

def apply_darken(pixel):
    #Darkens picture by 10%
    (r, g, b) = pixel
    return (int(r * .9), int(g * .9), int(b * .9))

def apply_gray(pixel):
    #Makes photo grayscale
    (r, g, b) = pixel
    gray = int((r + g + b) / 3)
    return (gray, gray, gray)

def apply_sepia(pixel):
    #Makes photo sepia toned
    (r, g, b) = pixel
    out_red = int((r * .393) + (g *.769) + (b * .189))
    out_green = int((r * .349) + (g *.686) + (b * .168))
    out_blue = int((r * .272) + (g *.534) + (b * .131))
    return (out_red, out_green, out_blue)

def apply_invert(pixel):
    #Inverts photo
    (r, g, b) = pixel
    return (255 - r, 255 - g, 255 - b)

def apply_solar(pixel):
    #Make photo solarized
    (r, g, b) = pixel
    (out_red, out_green, out_blue) = (r, g, b)
    if r < 128:
        out_red = 255 - r
    if g < 128:
        out_green = 255 - g
    if b < 128:
        out_blue = 255 - b
    return (out_red, out_green, out_blue)

def apply_purple(pixel):
    #Makes everything purplescaled
    (r, g, b) = pixel
    out_red = int((r * .495) + (g * .185) + (b * .613))
    out_green = int((r * .313) + (g * 0) + (b * .512))
    out_blue = int((r * .545) + (g * .252) + (b * .465))
    return (out_red, out_green, out_blue)

def apply_fuchsia(pixel):
    #Makes image fuchsia toned
    (r, g, b) = pixel
    out_red = int((r * .600) + (g * .600) + (b * .600))
    out_green = int((r * .200) + (g * .200) + (b * .200))
    out_blue = int((r * .500) + (g * .500) + (b * .500))
    return (out_red, out_green, out_blue)

def apply_watermelon(pixel):
    #Pinks and lighter colors, like a watermelon
    (r, g, b) = pixel
    out_red = int((r * .212) + (g * .242) + (b * .888))
    out_green = int((r * .454) + (g * .222) + (b * .165))
    out_blue = int((r * .765) + (g * .444) + (b * .111))
    return (out_red, out_green, out_blue)

def apply_frosted_grape(pixel):
    #Ligth blue-purples, frosted
    (r, g, b) = pixel
    out_red = int((r * .495) + (g * .185) + (b * .613))
    out_green = int((r * .253) + (g* .671) + (b * .312))
    out_blue = int((r * .545) + (g * .252) + (b * .425))
    return (out_red, out_green, out_blue)

def apply_purple_chard(pixel):
    #Makes main part of image green, purple other parts
    (r, g, b) = pixel
    out_red = int((r * .212) + (g * .512) + (b * .333))
    out_green = int((r * .712) + (g * .123) + (b * .444))
    out_blue = int((r * .315) + (g * .416) + (b * .262))
    return (out_red, out_green, out_blue)

def apply_dampen(pixel):
    #Dampens the photo
    (r, g, b) = pixel
    out_red = int((r * .4) + (g * .2) + (b * .2))
    out_green = int((r * .2) + (g * .4) + (b * .2))
    out_blue = int((r * .2) + (g * .2) + (b* .4))
    return (out_red, out_green, out_blue)

def apply_dark_chill(pixel):
    #Darkens tone, adds slightly purple mask
    (r, g, b) = pixel
    out_red = int((r * .113) + (g * .621) + (b * .241))
    out_green = int((r * .414) + (g * .133) + (b * .311))
    out_blue = int((r * .161) + (g * .336) + (b * .616))
    return (out_red, out_green, out_blue)

def apply_sandblast(pixel):
    #Orange mask, takes out greens
    (r, g, b) = pixel
    out_green = int((r * .413) + (g * 0) + (b * .512))
    return (r, out_green, b)

def apply_posterize(pixel):
    #Applies posterize filter to photo
    (r, g, b) = pixel
    if r >= 0 and r <= 63:
        out_red = 50
    elif r >= 64 and r <= 127:
        out_red = 100
    elif r >= 128 and r <= 191:
        out_red = 150
    else:
        out_red = 200
    if g >= 0 and g <= 63:
        out_green = 50
    elif g >= 64 and g <= 127:
        out_green = 100
    elif g >= 128 and g <= 191:
        out_green = 150
    else:
        out_green = 200
    if b >= 0 and b <= 63:
        out_blue = 50
    elif b >= 64 and b <= 127:
        out_blue = 100
    elif b >= 128 and b <= 191:
        out_blue = 150
    else:
        out_blue = 200
    return (out_red, out_green, out_blue)

def apply_middle_rectangle(photo):
    #Makes middle rectangle in photo have certain effect
    (width, height) = photo.size
    (width_rec, height_rec) = (int(width / 4), int(height / 4))
    nim = photo.copy()
    pix = nim.load()
    nim2 = photo.copy()
    pixels = nim2.load()
    for y in range(height):
        for x in range(width):
            (r, g, b) = pix[x, y]
            if (x >= width_rec and x <= (width_rec * 3) and
                y >= height_rec and y <= (height_rec * 3)):
                pixels[x, y] = apply_dark_chill(pix[x, y])
            else:
                pixels[x, y] = pix[x, y]
    return nim2

def apply_red(pixel):
    #Apply red mask
    (r, g, b) = pixel
    return (r, 0, 0)

def apply_green(pixel):
    #Apply green mask
    (r, g, b) = pixel
    return (0, g, 0)

def apply_blue(pixel):
    #Apply blue mask
    (r, g, b) = pixel
    return (0, 0, b)

def apply_four_squares(photo):
    #Splits photo in 4 rectangles: red, green, blue, gray
    (width, height) = photo.size
    (width_rec, height_rec) = (int(width / 2), int(height / 2))
    nim = photo.copy()
    pix = nim.load()
    nim2 = photo.copy()
    pixels = nim2.load()
    for y in range(height):
        for x in range(width):
            (r, g, b) = pix[x, y]
            if (x >= 0 and x <= width_rec and y >= 0 and y <= height_rec):
                pixels[x, y] = apply_red(pix[x, y])
            elif (x >= width_rec and x <= (width_rec * 2)
                    and y >= 0 and y <= height_rec):
                pixels[x, y] = apply_green(pix[x, y])
            elif (x >= 0 and x <= width_rec and y >= height_rec
                    and y <= (height_rec * 2)):
                pixels[x, y] = apply_blue(pix[x, y])
            else:
                pixels[x, y] = apply_gray(pix[x, y])
    return nim2

def apply_flip(photo, flip_type):
    #Flips photo based on what is passed to it
    (width, height) = photo.size
    nim = photo.copy()
    pix = nim.load()
    nim2 = photo.copy()
    pixels = nim2.load()
    if flip_type == 'v':
        for x in range(width):
            for y in range(height):
                (r, g, b) = pix[x, y]
                pixels[x, height - 1 - y] = pix[x, y]
    elif flip_type == 'h':
        for y in range(height):
            for x in range(width):
                (r, g, b) = pix[x, y]
                pixels[width - 1 - x, y] = pix[x, y]
    return nim2

def apply_mirror(photo, mirror_type):
    #Mirrors photo based on what is passed to it
    (width, height) = photo.size
    nim = photo.copy()
    pix = nim.load()
    pixels = pix
    if mirror_type == 'y':
        for y in range(height):
            for x in range(width):
                (r, g, b) = pix[x, y]
                pixels[width - 1 - x, y]=pix[x, y]
    elif mirror_type == 'x':
        for x in range(width):
            for y in range(height):
                (r, g, b) = pix[x, y]
                pix[x, height - 1 - y]=pixels[x, y]
    return nim

def print_effects():
    #Print the available effects
    effect_dict = {'[0]' : 'Show No Additional Effect',
                        '[1]' : 'Brighten',
                        '[2]' : 'Darken',
                        '[3]' : 'Grayscale',
                        '[4]' : 'Sepia',
                        '[5]' : 'Invert',
                        '[6]' : 'Solarize',
                        '[7]' : 'Pure Purple',
                        '[8]' : 'Fuchsia',
                        '[9]' : 'Watermelon',
                        '[10]' : 'Frosted Grape',
                        '[11]' : 'Purple Chard',
                        '[12]' : 'Dampen',
                        '[13]' : 'Dark Chill',
                        '[14]' : 'Sandblast',
                        '[15]' : 'Posterize',
                        '[16]' : 'Middle Rectangle',
                        '[17]' : 'Four Squares',
                        '[18]' : 'Flip',
                        '[19]' : 'Mirror',
                        '[20]' : 'Random'
    }
    print()
    print('Enter Number'.ljust(15) + 'Effect'.ljust(15))
    print('-'.ljust(15, '-') + '-'.ljust(25, '-'))
    for k, v in effect_dict.items():
        print(k.ljust(15) + v.ljust(15))
    print()

def execute_list(image):
    #Asks for desired effect and goes on to apply it
    filter_type = 'x'
    while filter_type.isdigit() == False:
        print('Enter effect #, h for list of possible effects, q to quit: ')
        filter_type = input()
        if filter_type == 'q':
            sys.exit()
        elif filter_type == 'h':
            print_effects()
    filter_type = int(filter_type)
    if filter_type == 20:
        filter_type = random.randint(1, 19)
    if filter_type == 0:
        image = show_img(image)
    elif filter_type == 1: #Brighten
        image = apply_filter(image, apply_brighten)
    elif filter_type == 2: #Darken
        image =apply_filter(image, apply_darken)
    elif filter_type == 3: #Grayscale
        image = apply_filter(image, apply_gray)
    elif filter_type == 4: #Sepia
        image = apply_filter(image, apply_sepia)
    elif filter_type == 5: #Inversion
        image = apply_filter(image, apply_invert)
    elif filter_type == 6: #Solarize
        image = apply_filter(image, apply_solar)
    elif filter_type == 7: #Pure Purple
        image = apply_filter(image, apply_purple)
    elif filter_type == 8: #Fuchsia
        image = apply_filter(image, apply_fuchsia)
    elif filter_type == 9: #Watermelon
        image = apply_filter(image, apply_watermelon)
    elif filter_type == 10: #Frosted Grape
        image = apply_filter(image, apply_frosted_grape )
    elif filter_type == 11: #Purple Chard
        image = apply_filter(image, apply_purple_chard)
    elif filter_type == 12: #Dampen
        image = apply_filter(image, apply_dampen)
    elif filter_type == 13: #Dark Chill
        image = apply_filter(image, apply_dark_chill)
    elif filter_type ==14: #Sandblast
        image = apply_filter(image, apply_sandblast)
    elif filter_type == 15: #Posterize
        image = apply_filter(image, apply_posterize)
    elif filter_type == 16: #Middle Rectangle
        image = apply_middle_rectangle(image)
    elif filter_type == 17: #Four Squares
        image = apply_four_squares(image)
    elif filter_type == 18: #Flip
        flip_type = input('Flip type: v - vertical, h - horizontal. (v/h) ')
        while flip_type != 'v' and flip_type != 'h':
            flip_type = input('Flip type: v - vertical, h - horizontal. (v/h) ')
        image = apply_flip(image, flip_type)
    elif filter_type == 19: #Mirror
        mirror_type = input('Mirror axis: x axis, y axis. (x/y) ')
        while mirror_type != 'x' and mirror_type != 'y':
            mirror_type = input('Mirror axis: x axis, y axis. (x/y) ')
        image = apply_mirror(image, mirror_type)
    else:
        print('Invalid response')
    return image

def save(photo):
    #Prompts to save image
    save = input('Do you want to save image? (y/n) ')
    while (save != 'y') and (save != 'n'):
        save = input('Do you want to save image? (y/n) ')
    if save == 'y':
        new_name = input('Please enter filename to save under: ')
        photo.save(new_name + '.jpg')

def execute_run(imgName):
    #Starts program and keeps it going until told to stop
    im = open_image(imgName)
    print_effects()
    while True:
        im = execute_list(im)
        im.show()
        should_continue = input('Do you want to keep editing image? (y/n) ')
        while (should_continue != 'y') and (should_continue != 'n'):
            should_continue = input('Please enter (y/n)')
        if should_continue == 'n':
            break
    save(im)

if __name__ == '__main__':
    #Passes a picture to be run in the program
    if len(sys.argv) < 2:
        print('Usage: py PhotoFilter [imagename]')
        sys.exit()
    execute_run(sys.argv[1])
