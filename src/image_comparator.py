import sys, os, subprocess, string
from PIL import Image

# def merge_images(file1, file2):
#     """Merge two images into one, displayed side by side
#     :param file1: path to first image file
#     :param file2: path to second image file
#     :return: the merged Image object
#     """
#     image1 = Image.open(file1)
#     image2 = Image.open(file2)
#
#     (width1, height1) = image1.size
#     (width2, height2) = image2.size
#
#     result_width = width1 + width2
#     result_height = max(height1, height2)
#
#     result = Image.new('RGB', (result_width, result_height))
#     result.paste(im=image1, box=(0, 0))
#     # result.paste(im=image2, box=(width1, 0))
#     # result.save('/Users/adityanisal/')
#     result().show

# merge_images('/Users/adityanisal/Dropbox/temp/7dc60533-f48c-45d3-9a6c-ff040af280ce/screenshots/fc4352d4-a7ee-4b94-87bc-ff7526b4c961.png', '/Users/adityanisal/Dropbox/temp/7dd9c6a4-8aca-48fd-af4a-62324596799a/screenshots/bc1a7003-7881-498e-8792-68ea51e15dc9.png')
import subprocess
subprocess.call('/usr/local/bin/convert +append /Users/adityanisal/Dropbox/temp/7dc60533-f48c-45d3-9a6c-ff040af280ce/screenshots/fc4352d4-a7ee-4b94-87bc-ff7526b4c961.png /Users/adityanisal/Dropbox/temp/7dd9c6a4-8aca-48fd-af4a-62324596799a/screenshots/bc1a7003-7881-498e-8792-68ea51e15dc9.png /Users/adityanisal/alibabachor.png', shell=True)
