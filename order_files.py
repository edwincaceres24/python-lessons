#Import moduls
import os
import shutil
from dotenv import load_dotenv 

load_dotenv()

download_rutes =os.getenv('downloadpath')
ext_text= ['.docx','.txt','.doc','.pdf','.pptx']
ext_img=['.png','.jpg','.jpeg','.gif',]
ext_video=['.mov','.mp4']
ext_sfk=['.sfk']


def listDir():
    for file in os.listdir(download_rutes): 
        file_name, ext = os.path.splitext(file) 
        order(file, ext)

def order (file, ext):
    for i in ext_text: 
        if ext == i:
            shutil.move(download_rutes + file, download_rutes + 'Text')
            print('Se ha movido el archivo ' + str(file) + ' a la carpeta Text')
    for i in ext_img:
        if ext == i:
            shutil.move(download_rutes + file, download_rutes + 'Images')
            print('Se ha movido el archivo ' + str(file) + ' a la carpeta Images')
    for i in ext_video:
        if ext == i:
            shutil.move(download_rutes + file, download_rutes + 'Videos')
            print('Se ha movido el archivo ' + str(file) + ' a la carpeta Videos')

    if  ext !='' and ((ext in (ext_video + ext_img + ext_sfk + ext_text))==False):
        shutil.move(download_rutes + file, download_rutes + 'Other')
        print('Este archivo ' + file + ' no tiene ninguna de la extensiones mencionadas. Se movió a la carpeta "Other')

listDir()


