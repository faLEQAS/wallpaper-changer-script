#change wallpaper don't touch 

import requests as rq
import praw
import random
import ctypes
from wallpaper import set_wallpaper, get_wallpaper
import platform
import os
import time


def get_pic():

	reddit = praw.Reddit(client_id = "",
							client_secret = "",
							username = "",
							password = "",
							user_agent = "")

	subreddit = reddit.subreddit("wallpaper")

	top = subreddit.top(limit = 100)

	posts = []

	for post in top:
		posts.append(post)

	chosenpost = random.choice(posts)

	image = chosenpost.url


	return(image)
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


	set_wallpaper()

	time.sleep(43200)

	print("set wallpaper!")
