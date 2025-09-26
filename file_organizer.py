import os
import shutil
import glob
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

categories = {
    "Images" : ["jpg","png","gif"],
    "Music" :  ["mp3","wav"],
    "Videos" : ["mp4","mkv"],
    "Documents" : ["doc","pdf","xlsx","txt"],
    "Archives" : ["zip","rar","tar","gz"],
    "Programs" : ["exe","msi","deb"]
}