# using D3vd/Meme_Api put it as json file
import requests
import os 
import time
import urllib.request
import urllib.parse


def loop():
    # This is grabbing a random meme from https://github.com/D3vd/Meme_Api
    r = requests.get("https://meme-api.herokuapp.com/gimme")
    packages_json = r.json()
    package_url = packages_json['url']


    # Checking if meme.jpg exists, if not, download it, and if it does, then delete it.
    try:
        if os.path.exists("meme.jpg"):
            os.remove("meme.jpg")
            time.sleep(0.5)
            urllib.request.urlretrieve(package_url, "meme.jpg")
        else:
            urllib.request.urlretrieve(package_url, "meme.jpg")

        
        # 
        if (os.path.exists("meme.jpg")):
            print("meme found")
        else: 
            urllib.request.urlretrieve(package_url, "meme.jpg")
        from PIL import Image
        from random import randint
        # Putting the meme on the .mp4 file.
        rand = randint(1,9999)
        im = Image.open("meme.jpg")
        im.convert('RGB').save('meme.jpg')
        im.thumbnail((300, 2500))
        im.save("meme.jpg")
    except:
        print("Error opening meme.jpg")
        # check if there is a meme.jpg file.
        if (os.path.exists("meme.jpg")):
            im.close()
            time.sleep(0.5)
            os.remove("meme.jpg")
            loop()
        else:
            time.sleep(0.5)
            loop()

    # Saving as a .mp4 file
    os.system(f"ffmpeg -i video.mp4 -i meme.jpg -filter_complex overlay=0:0 meme{rand}.mp4")

    # delete the meme.jpg
    os.remove("meme.jpg")

#call the function 15 times.
for i in range(15):
    if os.path.exists("meme.jpg"):
        os.remove("meme.jpg")
        time.sleep(0.25)
        loop()
    else: 
        loop()
        time.sleep(1)