import pygame as pg
import sys
import time
from pygame.locals import *

# Stores the "x" or "o" value as character.
XO = "x"

# Stores the winner's value at any instance of code.
winner = None

# Checks to see if the game is a draw.
draw = None

# Sets the width of the game window.
width = 400

# Sets the height of the game window.
height = 400

# Sets the background color of the game window.
white = (255, 255, 255)

# Sets the color of the lines on the gameboard.
line_color = (0, 0, 0)

# Sets up a three-by-three (3x3) board in canvas.
board = [[None] * 3, [None] * 3, [None] * 3]

# Initializes the pygame window.
pg.init()

# Sets the frames-per-second (fps).
fps = 30

# Tracks the time.
CLOCK = pg.time.Clock()

# Builds the infrastructure of the display.
screen = pg.display.set_mode((width, height + 100), 0, 32)

# Sets the name for the game window.
pg.display.set_caption("Tic-Tac-Toe")

# Loads images as python objects.
initiating_window = pg.image.load("cover.png")
x_image = pg.image.load("X.png")
o_image = pg.image.load("O.png")

# Resizes the images.
initiating_window = pg.transform.scale(initiating_window, (width, height + 100))
x_image = pg.transform.scale(x_image, (80, 80))
o_image = pg.transform.scale(o_image, (80, 80))

def game_initiating_window():

    # Displays over the screen.
    screen.blit(initiating_window, (0, 0))

    # Updates the display.
    pg.display.update()
    time.sleep(3)
    screen.fill(white)

    # Draws vertical lines.
    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)

    # Draws horizontal lines.
    pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)
    draw_status()

def draw_status():

    # Brings in the global variable draw.
    global draw

    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " won!"
    if draw:
        message = "Game draw!"

    # Sets a font object.
    font = pg.font.Font(None, 30)

    # Sets the font properties.
    text = font.render(message, 1, (255, 55, 255))

    # Creates a small block at the bottom of the main window and sends the
    # rendered message.
    screen.fill((0, 0, 0,), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width / 2, 500 - 50))
    screen.blit(text, text_rect)
    pg.display.update()

def check_win():

    global board, winner, draw

    # Checks for winning rows.
    for row in range(0, 3):
        if ((board[row][0] == board[row][1] == board[row][2] and (board[row][0] is not None))):
            winner = board[row][0]
            pg.draw.line(screen, (250, 0, 0),
                         (0, (row + 1) * height / 3 - height / 6),
                         (width, (row + 1) * height / 3 - height / 6),
                         4)
            break

    # Checks for winning columns.
    for col in range(0, 3):
        if ((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner = board[0][col]
            pg.draw.line(screen, (250, 0, 0), ((col + 1) * width / 3 - width / 6, 0),
                         ((col + 1) * width / 3 - width / 6, height), 4)
            break

    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):

        # Checks to make sure the game was won from left to right.
        winner = board[0][0]
        pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)

    if (all([all(row) for row in board]) and winner is None):
        draw = True

    draw_status()

def drawXO(row, col):

    global board, XO

    # Pastes the image to the first (1st) row, at the x coordinate of
    # 30 from the left mergin.
    if row == 1:
        position_x = 30

    # Pastes the image to the second (2nd) row, at the x coordinate of
    # 30 from the game line.
    if row == 2:
        position_x = width / 3 + 30

    if row == 3:
        position_x = width / 3 * 2 + 30

    if col == 1:
        position_y = 30

    if col == 2:
        position_y = height / 3 + 30

    if col == 3:
        position_y = height / 3 * 2 + 30

    board[row - 1][col - 1] = XO

    if (XO == "x"):

        screen.blit(x_image, (position_y, position_x))
        XO = "o"

    else:
        screen.blit(o_image, (position_y, pisition_x))
        XO = "x"
    pg.display.update()

def user_click():

    x, y = pg.mouse.get_pos()

    if (x < width / 3):
        col = 1

    elif (x < width / 3 * 2):
        col = 2

    elif (x < width):
        col = 3

    else:
        col = None

    if (y < height / 3):
        row = 1

    elif (y < height / 3 * 2):
        row = 2

    elif (y < height):
        row = 3

    else:
        row = None

    if (row and col and board[row - 1][col - 1] is None):
        global XO

        drawXO(row, col)
        check_win()


def reset_game():
    global board, winner, XO, draw

    time.sleep(3)
    XO = "x"
    draw = False
    game_initiating_window()
    winner = None
    board = [[None] * 3, [None] * 3, [None] * 3]


game_initiating_window()

while (True):
    for event in pg.event.get():

        if event.type == QUIT:
            pg.quit()
            sys.exit()

        elif event.type is MOUSEBUTTONDOWN:
            user_click()

            if (winner or draw):
                reset_dame()

    pg.display.update()
    CLOCK.tick(fps)
