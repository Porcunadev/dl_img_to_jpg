import urllib.request
from datetime import datetime

current_time = datetime.now()

def dl_img_to_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url,full_path)

name = input('Hello, what is your name?')
url = input('Enter image URL to download:')
file_name = input('Enter file name to save as:')

dl_img_to_jpg(url,'images/', file_name)

print(f"Thank you {name} for using our services. LOG DATE = {current_time}") 

