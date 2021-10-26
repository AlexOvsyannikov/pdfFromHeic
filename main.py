import datetime
import os
from wand.image import Image as wImage
from PIL import Image

path = './photos/'
path_to_save = './generated/'


def name_pages(path):
    files = os.listdir(path)
    files.sort()
    print(files)
    page_num = 1
    print("Converting HEIC to JPG")
    for file in files:
        if file.endswith('.HEIC'):
            new_path_to_file = path + str(page_num) + '.JPG'
            os.rename(path + file, new_path_to_file)
            img = wImage(filename=new_path_to_file)
            img.format = 'jpg'
            img.save(filename=new_path_to_file)
            img.close()
            print(new_path_to_file + ' done')
            page_num += 1
    print("All photos are in JPG now")
    return page_num


def convert_to_pdf(path, path_to_save, pdf_name):
    total_num_of_pages = name_pages(path)
    image_list = []
    first_image = Image.open(path + '1.JPG')
    print("Starting converting to pdf")
    for page in range(2, total_num_of_pages):
        print(f"Working with page {page}")
        _name = str(page) + '.JPG'
        image_list.append(Image.open(path + _name).convert('RGB'))

    first_image.save(path_to_save + f'{pdf_name}.pdf',
                     save_all=True,
                     append_images=image_list)
    print("DONE")


def clear_photo_directory(path):
    files = os.listdir(path)
    for file in files:
        if file.endswith('.JPG'):
            os.remove(path+file)
    print("All photos deleted")


if __name__ == '__main__':
    pdf_name = input('Введи название pdf файла: ')
    convert_to_pdf(path, path_to_save, pdf_name)
    clear_photo_directory(path)