import pytesseract
import easyocr
import cv2

reader = easyocr.Reader(['en'])

def main(image_path: str, tesseract_path: str, 
         init_column_y: int, init_column_x: int, 
         init_line_y: int, init_line_x: int):

    cols = list()
    rows = list()
    
    image = cv2.imread(image_path, 0)

    if image is None:
        return "Error when getting the image"
    
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    h_column = init_column_y + 230

    for x in range(init_column_x, init_column_x + 50*15, 50):
        w_column = x + 45
        cut_image = image[init_column_y:h_column, x:w_column]

        image_string = pytesseract.image_to_string(cut_image, config="--psm 6")
        image_list = image_string.split('\n')
        image_list.pop()
        image_numbers_list = [int(number) for number in image_list]

        if len(image_numbers_list) > 0:
            cols.append(image_numbers_list)

    w_line = init_line_x + 230

    for y in range(init_line_y, init_line_y + 50*15, 50):
        h_line = y + 45
        cut_image = image[y:h_line, init_line_x:w_line]
        threshold = cv2.threshold(cut_image, 200, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        image_string = reader.readtext(threshold, detail = 0)[0]
        image_numbers_list = [int(number) for number in image_string.split(' ')]

        if len(image_numbers_list) > 0:
            rows.append(image_numbers_list)

    result = {
        'cols': cols,
        'rows': rows
    }

    return result


if __name__ == '__main__':
    print(
        main(
            image_path = '/home/schlemuel/Imagens/Capturas de tela/Captura de tela de 2025-01-09 15-12-32.png',
            tesseract_path = r'/bin/tesseract',
            init_column_y = 20,
            init_column_x = 822,
            init_line_y = 260,
            init_line_x = 585
        )
    )
