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

download_dir = "Downloads"
summary = {}

for category,extensions in categories.items():
    files = []
    for ext in extensions:
        files.extend(glob.glob(os.path.join(download_dir,f"*.{ext}")))
    os.makedirs(category,exist_ok=True)
    logging.info(f"Found {len(files)} {category.lower()} files.The transfer started!")

    for file in files:
        try:
            shutil.move(file,os.path.join(category,os.path.basename(file)))
        except Exception as e:
            print(f"Something went wrong! {e}")
            logging.error(e)
    print(f"All files moved to folder: {category}")
    summary[category] = len(files)