import pytesseract
import cv2
import numpy as np
import imutils

print_image_column = True
print_image_line = True

def spaces(imagem_sem_espacos):
    add = list()
    have_0 = False
    consecutive_no_0 = 0

    for column in range(len(imagem_sem_espacos[0])):
        actual_column = imagem_sem_espacos[:, column]
        all_background = True

        for num in actual_column:
            if num == 0:
                have_0 = True
                all_background = False
                consecutive_no_0 = 0
                break

        if all_background and have_0:
            consecutive_no_0 += 1

        if consecutive_no_0 > 10:
            consecutive_no_0 = 0
            add.append(column)

    return add

def adding_spaces(imagem_para_adicionar_espacos, adicionar):
    space = 50

    for i in range(len(adicionar)):
        first_part_image = imagem_para_adicionar_espacos[:, 0:(adicionar[i] + round(space*i) + 1)]
        last_part_image = imagem_para_adicionar_espacos[:, (adicionar[i] + round(space*i) + 1):]
        first_part_image = np.pad(first_part_image, ((0,0),(0,space)), mode='constant', constant_values=255)

        imagem_para_adicionar_espacos = np.concatenate((first_part_image, last_part_image), axis=1)

    return imagem_para_adicionar_espacos

def main(image_path: str, tesseract_path: str, 
         init_column_y: float, init_column_x: float, 
         init_line_y: float, init_line_x: float,
         square_edge: float, window_size: tuple,
         num_of_columns: int, num_of_lines: int):

    cols = list()
    rows = list()
    
    image = cv2.imread(image_path, 0)

    if image is None:
        return "Error when getting the image"
    
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    h_column = round(init_column_y + (0.221354167 * window_size[1]))

    for mult in range(15):
        x = round(init_column_x + square_edge*mult)
        w_column = round(x + square_edge)
        cut_image = image[round(init_column_y):h_column, x:w_column]
        bigger_image = imutils.resize(cut_image, width=90)

        final_image = cv2.threshold(bigger_image, 90, 230, 0)[1]
        
        image_string = pytesseract.image_to_string(final_image, config="--psm 6 -c tessedit_char_whitelist='0123456789 '")
        image_list = image_string.split('\n')

        if print_image_column:
            print(image_list)
            cv2.imshow('coluna', final_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        image_list.pop()
        image_numbers_list = [int(number) for number in image_list]

        if len(image_numbers_list) > 0:
            cols.append(image_numbers_list)

    w_line = round(init_line_x + (0.124450952 * window_size[0]))
    
    for mult in range(15):
        y = round(init_line_y + square_edge * mult)
        h_line = round(y + square_edge)
        cut_image = image[y:h_line, round(init_line_x):w_line]
        bigger_image = imutils.resize(cut_image, height=90)
        threshold = cv2.threshold(bigger_image, 90, 230, 0)[1]

        spaces_in_image = spaces(threshold)
        final_image = adding_spaces(threshold, spaces_in_image)

        image_string = pytesseract.image_to_string(final_image, config=f"--psm 7 -c tessedit_char_whitelist='0123456789 '")
        slash_n_list = image_string.split('\n')

        if print_image_line:
            print(slash_n_list)
            cv2.imshow('linha', final_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        slash_n_list.pop()
        number_list = slash_n_list[0].split()
        image_numbers_list = [int(number) for number in number_list]

        if len(image_numbers_list) > 0:
            rows.append(image_numbers_list)

    result = {
        'cols': cols,
        'rows': rows
    }

    return result
