from expyriment import design, control, stimuli, misc 
# control.set_develop_mode()

# Get Color List
# print(misc.Colour.get_colour_names())

# Global settings
exp = design.Experiment() 
control.initialize(exp) 
screen_w, screen_h = exp.screen.size
square_length = int(screen_w*.05)
square_size = (square_length, square_length)
distance_from_edge = square_length//2

# print(misc.Colour.get_colour_names()) # get color list in expyriment... not that useful

## troubleshooting prints
# print("size:", exp.screen.size)
# print("square.length = 0.05 of width:", square_length)
# print(positions) # confirming positions are correct
# print(squares) # checking the list of squares to see what it contains

## helper functions

def generate_red_square(square_position = (int,int)): 
    return stimuli.Rectangle(square_size, misc.Colour("red"), 1, None , None , square_position)

# test_square = generate_red_square((0,0)) # testing the generate_red_square func

def calc_center_position(corner):
    x = corner[0]
    y = corner[1]

    if x < 0:
        x += distance_from_edge
    else:
        x -= distance_from_edge

    if y < 0:
        y += distance_from_edge
    else:
        y -= distance_from_edge 
    
    return (x,y)

"""
Stimuli and design (trial and block structures)
"""

## calculating corners
corners = [] #top_left, bottom_left, top_right, bottom_right
for i in (-screen_w, screen_w):
    for j in (screen_h, -screen_h):
        corners.append((i//2,j//2)) #i had missed the //2 earlier

## calculating final positions using helper function
positions = [calc_center_position(corner) for corner in corners]

## generate squares
squares = [generate_red_square(pos) for pos in positions]

## hard coded errorneous coordinates used for trouble shooting
""" 
top_left_sq = generate_red_square((-780,580))
bottom_left_sq = generate_red_square((-780,-580))
top_right_sq  = generate_red_square((780,580))
bottom_right_sq = generate_red_square((780,-580))
"""

"""
Experiment operations Below
"""
control.start() 
# test_square.present(clear=True, update= True) # confirming helper function works

exp.screen.clear()

for square in squares:
    square.present(clear= False, update = False)

exp.screen.update()

# top_left_sq.present(clear= True, update = False)
# bottom_left_sq.present(clear= False, update = False)
# top_right_sq.present(clear= False, update = False)
# bottom_right_sq.present(clear= False, update = True)

exp.keyboard.wait()
control.end()