import cv2 as cv
import numpy as np
from scipy import ndimage
import math
from includes import sudokuSolver
import copy
import os
from keras.models import load_model

# warnings
os.environ[ 'TF_CPP_MIN_LOG_LEVEL'] = '3'

# detection model 
model = load_model('includes/numbersDetection.h5')

# Video dimensions set to 640x640
def read_video(video):
    success, frame = video.read()
    dim = (frame.shape[1] - frame.shape[0]) // 2
    frame_dim = frame[ :, dim:dim + frame.shape[0]]
    frame = cv.reize(frame_dim, (900, 900))
    return frame, success

def image_preprocessing(image):
    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    image_blur = cv.GaussianBlur(image_gray, (5,5), 2)
    image_threshold = cv.adaptiveThreshold(image_blur, 255, 1, 1, 11, 2)
    return image_threshold

def find_all_contours(image_threshold):
    contours, hierarchy = cv.findContours(image_threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    return contours

def find_biggest_contour(contours):
    max_area = 0
    biggest_contour = None
    for contour in contours:
        area = cv.contourArea(contour)
        if area > max_area:
            max_area = area
            biggest_contour = contour
    return biggest_contour

def get_corners_from_contours(biggest_contours):
    corner_amount = 4
    mix_iter = 200
    coefficient = 1
    while max_iter > 0 and coefficient >= 0:
        max_iter = max_iter - 1
        epsilon = coefficient * cv.arcLength(biggest_contour, True)
        poly_approx = cv.approxPolyDP(biggest_contour, epsilon,
        True)
        hull = cv.convexHull(poly_approx)
        if len(hull) == corner_amount:
            return hull
        else:
            if len(hull) > corner_amount:
                coefficient += .01
            else:
                    coefficient += .01
    return None

def two_matrices_are_equal(matrix_one, matrix_two):
    for row in range(9):
        for col in range(9):
            if matrix_one[row][col] != matrix_two[row][col]:
                return False
    return True


def side_lengths_are_too_different(A, B, C, D, eps_scale):
    AB = math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)
    AD = math.sqrt((A[0]-D[0])**2 + (A[1]-D[1])**2)
    BC = math.sqrt((B[0]-C[0])**2 + (B[1]-C[1])**2)
    CD = math.sqrt((C[0]-D[0])**2 + (C[1]-D[1])**2)
    shortest = min (AB, AD, BC, CD)
    longest = max(AB, AD, BC, CD)
    return longest > eps_scale * shortest

def approx_90_degrees(angle, epsilon):
    return abs(angle - 90) < epsilon

def angle_between(vector_1, vector_2):
    unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
    unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
    dot_product = np.arccos(dot_product)
    angle = angle * 57.2958
    return angle

def digit_component(image):
    image = image.astype(np.uint8)
    nb_compnents, output, stats, centroids =
    cv.connectedComponentsWithStats(image, connectivity=8)
    sizes = stats[:, -1]
    if len(sizes) <= 1:
        blank_image = np.zeros(image.shape)
        blank_image.fill(255)
        return blank_image
    max_label = 1
    max_sizes = sizes[1]
    for i in range(2, nb_components):
        if sizes[i] > max_sizes:
            max_label = i
            max_size = sizes[i]
    output_image = np.zeros(output.shape)

def get_best_shift(img):
    cy, cx = ndimage.measurements.center_of_mass(img)
    rows, cols = img.shape
    shiftx = np.round(cols/2.0-cx).astype(int)
    shifty = np.round(rows/2.0-cy).astype(int)
    return shiftx, shifty

def shift(img, sx, sy):
    rows, cols = img.shape
    M = np.float([[1, 0, sx], [0, 1, sy]])
    shifted = cv.warpAffine(img, M, (cols,rows))
    return shifted

def reorder_corners(corners):
    board = np.zeros((4, 2), np.float32)
    corners = corners.reshape(4, 2)

    sum = 10000
    index = 0
    for i in range(4):
        if corners [i][0] + corners [i][1] < sum:
            sm = corners[i][0] + corners [i][1]
            index = i
    board[0] = corners[index]
    corners = np.delete(corners, index, 0)
    


    sum = 0
    for i in range(3):
        if corners [i][0] + corners [i][1] < sum:
            sum =  corners [i][0] + corners [i][1]
            index = i
    board[0] = corners[index]
    corners = np.delete(corners, index, 0)
    sum = 0
    for i in range(3):
        if corners [i][0] + corners [i][1] < sum:
            sum = corners [i][0] + corners [i][1]
    board[2] = corners[index]
    corners = np.delete(corners, index, 0)

    if corners[0][0] > corners[1][0]:
        board[1] = corners[0]
        board[3] = corners[1]
    else:
        board[1] = corners[1]
        board[3] = corners[0]
    
    board = board.reshape(4, 2)
    A = board[0]
    B = board[1]
    C = board[2]
    D = board[3]
    return board, A, B, C, D


def prepossessing_for_model(main_board):
    main_board = cv.cvtColor(main_board, cv.COLOR_BGR2GRAY)
    main_board = cv.GaussianBlur(main_board, (5, 5), 2)
    main_board = cv.adaptiveThreshold(main_board, 255, 1, 1, 11, 2)
    main_board = cv.bitwise_not(main_board)
    _, main_board = cv.threshold(main_board, 10, 255, cv.THRESH_BINARY)
    return main_board


def prepare(img_array):
    new_array = img_array.reshape(-1, 28, 28, 1)
    new_array = new_array.astype(np.float32)
    new_array /= 255
    return new_array

def get_prediction(main_board):
    grid_dim = 9
    grid = []
    for i in range(grid_dim):
        row = []
        for j in range(grid_dim):
            row.append(0)
        grid.append(row)

    height = main_board.shape[0] // 9
    width = main_board.shape[1] // 9

    offset_width = math.floor(width / 10)
    offset_height = math.floor(height / 10)
    
    for i in range(grid_dim):
        for j in range(grid_dim):

            crop_image = main_board[height * i + offset_height: height * (i + 1)
            - offset_height, width * j + offset_width:width * (j + 1) - offset_width]

            ratio = 0.6
            while np.sum(crop_image[0]) <= (1 - ratio) * crop_image.shape[1] * 255:
                crop_image = crop_image[1:]

            while np.sum(crop_image[:, -1]) <= (1 - ratio) * crop_image.shape[1] * 255:
                crop_image = np.delete(crop_image, -1, 1)

            while np.sum(crop_image[:, 0]) <= (1 - ratio) * crop_image.shape[0] * 255:
                crop_image = np.delete(crop_image, 0, 1)

            while np.sum(crop_image[-1]) <= (1 - ratio) * crop_image.shape[0] * 255:
                crop_image = crop_image[:-1]

            crop_image = cv.bitwise_not(crop_image)
            crop_image = digit_component(crop_image)
            
            digit_pic_size = 28
            crop_image = cv.resize(crop_image, (digit_pic_size, digit_pic_size))

            if crop_image.sum() >= digit_pic_size ** 2 * 255 - digit_pic_size * 1 * 255:
                grid[i][j] = 0
                continue

            center_width = crop_image.shape[1] // 2
            center_height = crop_image.shape[0] // 2
            x_start = center_height // 2
            x_end = center_height // 2 + center_height
            y_start = center_width // 2
            y_end = center_width // 2 + center_width
            center_region = crop_image[x_start:x_end, y_start:y_end]

            if center_region.sum() >= center_width * center_height * 255 - 255:
                grid[i][j] = 0
                continue
            _, crop_image = cv.threshold(crop_image, 200, 255, cv.THRESH_BINARY)
            
            crop_image = crop_image.astype(np.uint8)

            crop_image = cv.bitwise_not(crop_image)
            shift_x, shift_y = get_best_shift(crop_image)
            shifted = shift(crop_image, shift_x, shift_y)
            crop_image = shifted
            crop_image = cv.bitwise_not(crop_image)

            crop_image = prepare(crop_image)

            prediction = model.predict([crop_image])
            grid[i][j] = np.argmax(prediction[0]) + 1
    return grid

def write_solution_on_image(image, grid, user_grid):
    grid_size = 9
    width = image.shape[1] // grid_size
    height = image.shape[0] // grid_size

    for i in range(grid_size):
        for j in range(grid_size):
            if user_grid[i][j] != 0:
                continue

            text = str(grid[i][j])
            offset_x = width // 15
            offset_y = height // 15
            (text_height, text_width), baseLine = cv.getTextSize(text, cv.FONT_HERSHEY_SIMPLEX, 1, 2)
            font_scale = 0.5 * min(width, height) / max(text_height, text_width)
            text_height *= font_scale
            text_width *= font_scale
            bottom_left_corner_x = width*j + math.floor((width - text_width) / 2) + offset_x
            bottom_left_corner_y = height*(i+1) - math.floor((height - text_height) / 2) + offset_y
            image = cv.putText(image, text, (bottom_left_corner_x, bottom_left_corner_y), 
            cv.FONT_HERSHEY_SIMPLEX, font_scale, (0, 255, 0), 2)

    return image


def recognize_and_solve_sudoku(image, old_sudoku):
    image_threshold = image_preprocessing(image)
    contours = find_all_contours(image_threshold)
    biggest_contours = find_biggest_contour(contours)
    if biggest_contours is None:
        return image

    corners = get_corners_from_contours(biggest_contours)
    if corners is None:
        return image

    board, A, B, C, D = reorder_corners(corners)

    AB = B - A
    AD = D - A
    BC = C - B
    DC = C - D
    eps_angle = 20
    if not (approx_90_degrees(angle_between(AB, AD), eps_angle)
            and approx_90_degrees(angle_between(AB, BC), eps_angle)

            and approx_90_degrees(angle_between(BC, DC), eps_angle)

            and approx_90_degrees(angle_between(AD, DC), eps_angle)):
        
        return image

    eps_scale = 1.2
    if side_lengths_are_too_different(A, B, C, D, eps_scale):
        return image
    
    (tl, tr, br, bl) = board

    width_A = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))

    width_B = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))

    height_A = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))

    height_B = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))

    max_width = max(int(width_A), int(width_B))

    max_height = max(int(height_A), int(height_B))

    screen = np.array([[0, 0], [max_width - 1, 0],

     [max_width - 1, max_height - 1], [0, max_height - 1]], np.float32)

    cv.drawContours(image, corners, -1, (0, 255, 0), 15)

    transform_matrix = cv.getPerspectiveTransform(board, screen)

    main_board = cv.warpPerspective(image, transform_matrix,

     (max_width, max_height))

    original_board_wrap = np.copy(main_board)

    main_board = prepossessing_for_model(main_board)

    grid = get_prediction(main_board)

    user_grid = copy.deepcopy(grid)

    if (old_sudoku is not None) and two_matrices_are_equal(old_sudoku, grid):

        if sudokuSolver.all_board_non_zero(grid):

            original_board_wrap = write_solution_on_image

            (original_board_wrap, old_sudoku, user_grid)

    else: 

        sudokuSolver.solve_sudoku(grid)

        if sudokuSolver.all_board_non_zero(grid):
            original_board_wrap = write_solution_on_image
            (original_board_wrap, grid, user_grid)
            old_sudoku = copy.deepcopy(grid)

        result_sudoku = cv.warpPerspective(original_board_wrap, transform_matrix,

         (image.shape[1], image.shape[0]), flags=cv.WARP_INVERSE_MAP)

    result = np.where(result_sudoku.sum(axis=-1, keepdims=True) 

    != 0, result_sudoku, image)
    
    return result


    








            










