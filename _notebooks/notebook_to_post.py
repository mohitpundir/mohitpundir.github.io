import sys, re
import subprocess
import os

path = '/home/pi/dev/mohitpundir.github.io'
nb_name = str(sys.argv[1])
nb_name = nb_name.split('.')[0]

nb_path = path + '/_notebooks/' + str(sys.argv[1])

process = subprocess.Popen(["jupyter", "nbconvert", "--to", "markdown", nb_path],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           universal_newlines=True)

yaml = "---\ntitle: TITLE\nmathjax: true\ncategories: jeykll update\ntags:\n- tag\n---\n\n"

markdown_path = path + '/_notebooks/' + str(nb_name) + '.md'
print(markdown_path)
with open(markdown_path, 'r') as file:
    filedata = file.read()

filedata = re.sub(r"!\[png\]\(", "<img src=\"/assets/images/", filedata)
filedata = re.sub(".png\)", ".png\">", filedata)
filedata = yaml + filedata
with open(markdown_path, 'w') as file:
    file.write(filedata)

post_path = path + '/_posts/'
process = subprocess.Popen(["mv", markdown_path, post_path])

images_path = path + '/assets/images/'
nb_images_path = path + '/_notebooks/' + nb_name + '_files'
if os.path.exists(nb_images_path):
    process = subprocess.Popen(["mv", nb_images_path, images_path])   
