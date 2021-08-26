

import requests as rq
import praw
import random
import ctypes
from wallpaper import set_wallpaper, get_wallpaper
import platform
import os
import time
import PIL
from PIL import Image


def get_pic():

	reddit = praw.Reddit(client_id = "",
							client_secret = "",
							username = "",
							password = "",
							user_agent = "")

								#your chosen subreddit
	subreddit = reddit.subreddit("wallpaper")
								#your chosen subreddit
	top = subreddit.top(limit = 1000)

	posts = []

	for post in top:
		posts.append(post)

	chosenpost = random.choice(posts)

	image = chosenpost.url


	return(image)

def check_res():


    
    img = PIL.Image.open("post.jpg")
    
    
    wid, hgt = img.size
    
    
    return(str(wid) + "x" + str(hgt))


def set_wallpaper():
    get_wallpaper()
    #Check the operating system
    system_name = platform.system().lower()
    path = ''
    if system_name =='linux':
        path = os.getcwd()+'/post.jpg'
        command = "gsettings set org.gnome.desktop.background picture-uri file:" + path
        os.system(command)
    elif system_name == 'windows':
        path = os.getcwd()+'\\post.jpg'
        ctypes.windll.user32.SystemParametersInfoW(20,0,path,0)

while True:


	image = get_pic()

	r = rq.get(image)


	with open("post.jpg", "wb") as f:
		f.write(r.content)

	res = check_res()

	if res == "1920x1080": #config this to your screen's resolution


		set_wallpaper()
		print("set wallpaper!")
		time.sleep(43200)
	
