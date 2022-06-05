import pytesseract as pytesseract
from PyPDF2 import PdfReader
import fitz
import os, sys
# Путь для подключения tesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
import numpy as np
# Открыть папку
path = "C:/Users/ACER_GAMING/Desktop/Новая папка"
dirs = os.listdir( path )
# перечислить все файлы и папки
for file in dirs:
   #открытия файла
   file_path = (path+"/"+file)
   pdf_file = fitz.open(file_path)
   # Чтение места, где сохранить файл
   location = "C:/Users/ACER_GAMING/Desktop/всё"
   #поиск количества страниц в pdf
   number_of_pages = len(pdf_file)
   #итерация по каждой странице в pdf
   for current_page_index in range(number_of_pages):
     # итерация по каждому изображению на каждой странице PDF
     for img_index,img in enumerate(pdf_file.get_page_images(current_page_index)):
           xref = img[0]
           image = fitz.Pixmap(pdf_file, xref)
           # если это чёрно-белое или цветное изображение
           if image.n < 5:
               image.save("{}/image{}-{}.png".format(location,current_page_index, img_index))
           # если это CMYK: конвертируем в RGB
           else:
               new_image = fitz.Pixmap(fitz.csRGB, image)
               new_image.writePNG("{}/image{}-{}.png".foramt(location, current_page_index, img_index))
           # получаем строку
           config = r'--oem 3 --psm 6'
           print(pytesseract.image_to_string(r"C:\Users\ACER_GAMING\Desktop\всё\image0-0.png", config=config))
