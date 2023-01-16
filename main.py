import os
import subprocess

profile_username = input('What\'t is username you want?: ')
is_private = input('This profile is private? (Y/n):')

if is_private == 'Y':
    username = input('Please type your username: ')
    password = input('Please type your password: ')
    # TODO: Find api for check and login for instagram or facebook
    # It will have authenticate or security code

url = f"https://www.instagram.com/{profile_username}/"

# Create a directory to save the images
if not os.path.exists("instagram_images"):
    os.makedirs("instagram_images")

if not os.path.exists("instagram_images/%s" % profile_username):
    os.makedirs("instagram_images/%s" % profile_username)
subprocess.run(["python3", "-m", "pip", "install", "instaloader"])
subprocess.run(["instaloader", profile_username, " --no-posts ", "--stories"])
