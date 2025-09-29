from expyriment import design, control, stimuli, misc 

"""
notes for later.... 
ith row, j column

differnce center position of each would be square_length//2 + gap + square_length//2 
                                = square_length + gap
top to bottom also 

 size
 color of the squares, 
 
 the space between them, 
  the number of rows and number of columns, 
 
 and the screen background color

 difficult question is to determine the location of the top left square.
 screen height divided by rows
 total height from top of first square to the bottom of the bottom square =
 rows * (square size + gap) - gap

 
 screen width divided by columns
 total width from left of first square to the right of the far right square =
 columns * (square size + gap) - gap

i suppose we could get the corners by doing something similar
    top left (total height//2, -total width//2)
    bottom left (-total height//2, -total width//2)
    top right (total height//2, total width//2)
    bottom right (-total height//2, total width//2)

"""

# Get Color List
# print(misc.Colour.get_colour_names())

# Global settings
# control.set_develop_mode()


## I know you dont recommend this, but it's easier to change window mode to check fullscreen
control.defaults.initialise_delay = 0
control.defaults.window_mode = False
control.defaults.fast_quit = True
control.defaults.auto_create_subject_id = True

exp = design.Experiment(name = "Kaniza Square") 
control.initialize(exp) 

screen_w, screen_h = exp.screen.size

## troubleshooting prints
# print("size:", exp.screen.size)

## helper functions

def generate_square(square_size, square_color, position):
    return stimuli.Rectangle(square_size, square_color, position=position)

def calculate_first_pos(rows, coloumns, square_length, gap_size):
    half_length = square_length/2.0
    #calculate total height of all rows + gaps
    height = rows * (square_length + gap_size) - gap_size
    #calculate total width of all columns + gaps
    width = coloumns * (square_length + gap_size) - gap_size
    #calculate top left square center (x, y)
    x0 = -width/2.0 + half_length
    y0 = height/2.0 - half_length
    return (x0, y0)


"""
Stimuli and design (trial and block structures)
"""
def hermann_grid(square_length = int, square_color = 'str', gap_size = int, rows = int, columns = int, bg_color = 'str'):
    square_size = (square_length, square_length)
    first_pos = calculate_first_pos(rows, columns, square_length, gap_size)
    step = square_length + gap_size

    background = stimuli.BlankScreen(misc.Colour(bg_color))
    background.present(clear=False, update=False)

    x0, y0 = first_pos
    for r in range(rows):            # go row by row (top -> bottom)
        y = y0 - r * step            # down is negative y
        for c in range(columns):     # left -> right
            x = x0 + c * step
            square = generate_square(square_size, square_color, (x, y))
            square.present(clear=False, update=False)
    
"""
Experiment operations Below
"""
control.start() 


exp.screen.clear()

hermann_grid(square_length = 250, square_color = 'black', gap_size = 75, rows = 4, columns = 8, bg_color = 'white')

exp.screen.update()



exp.keyboard.wait()
control.end()