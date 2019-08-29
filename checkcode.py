import requests
import shutil
import tesserocr
from PIL import Image

res = requests.get("http://hgsm.oicp.net:88/CheckCode.aspx", stream=True, verify=False)
f = open('check.jpg', 'wb')
shutil.copyfileobj(res.raw, f)
f.close()
im = Image.open("check.jpg", "r")
code = tesserocr.image_to_text(im)
while not(code.strip().isdigit()):
    res = requests.get("http://hgsm.oicp.net:88/CheckCode.aspx", stream=True, verify=False)
    f = open('check.jpg', 'wb')
    shutil.copyfileobj(res.raw, f)
    f.close()
    im = Image.open("check.jpg", "r")
    code = tesserocr.image_to_text(im)
code = code.strip()
print(code)

