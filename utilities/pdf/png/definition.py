import os
from pdf2image import convert_from_path

CURRENT_DIRECTORY = os.getcwd()


class PDFConversor:
    def __init__(self):
        self.dir = os.getcwd()
        print(CURRENT_DIRECTORY)

    def convert_pdf_to_images(self, pdf_path):
        images = convert_from_path(pdf_path)
        for index, image in enumerate(images):
            image.save(f'{pdf_path}-{index}.png')


    def to_png(self):
        CURRENT_FILE = 'example-invoice.pdf'
        pdf_file = os.path.join(CURRENT_DIRECTORY, f"utilities\pdf\png\{CURRENT_FILE}")
        print(CURRENT_DIRECTORY)
        self.convert_pdf_to_images(pdf_file)
