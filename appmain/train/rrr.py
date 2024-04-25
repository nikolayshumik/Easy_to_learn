from docx import Document
from bs4 import BeautifulSoup
import base64

def convert_docx_to_html(docx_file_path):
    # Открываем файл .docx
    doc = Document(docx_file_path)

    # Создаем объект BeautifulSoup для хранения HTML
    html_content = BeautifulSoup(features="html.parser")

    # Создаем контейнер для содержимого документа
    body = html_content.new_tag('body')
    html_content.append(body)

    # Проходим по всем элементам документа (параграфам и изображениям) и сохраняем порядок
    for element in doc.element.body:
        if element.tag.endswith('p'):
            # Элемент - параграф
            element_tag = html_content.new_tag('p')
            element_tag.string = element.text
            body.append(element_tag)
        elif element.tag.endswith('graphic'):
            # Элемент - изображение
            image_data = element.graphicData.pic.blipFill.blip.embed
            image_stream = doc.part.related_parts[image_data].blob
            image_base64 = base64.b64encode(image_stream).decode('utf-8')

            # Создаем HTML-тег для изображения
            element_tag = html_content.new_tag('img')

            # Устанавливаем атрибуты src и alt для тега изображения
            element_tag['src'] = f'data:image/png;base64,{image_base64}'
            element_tag['alt'] = 'Image'

            # Добавляем HTML-тег в контейнер body
            body.append(element_tag)

    # Возвращаем HTML-контент в виде строки
    return str(html_content)

# Путь к вашему файлу .docx
docx_file_path = r'D:\КОЛЯМБА\НикитаДиплом\кинематика\теория\кинематика теория.docx'

# Преобразуем содержимое .docx в HTML
html_content = convert_docx_to_html(docx_file_path)

# Выводим HTML-контент
print(html_content)
