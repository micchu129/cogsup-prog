from expyriment import design, control, stimuli, misc 
control.set_develop_mode()

# Get Color List
# print(misc.Colour.get_colour_names())

# Global settings
exp = design.Experiment() 
control.initialize(exp) 
screen_w, screen_h = exp.screen.size
square_length = int(screen_w*.05)
square_size = (square_length, square_length)

# print(misc.Colour.get_colour_names())

# global var

    #corners
corners = [] #top_left, bottom_left, top_right, bottom_right
for i in (-screen_w, screen_w):
    for j in (screen_h, -screen_h):
        corners.append((i,j))

"""
Stimuli and design (trial and block structures)
"""
#helper functions

def generate_red_square(square_position = (int,int)): 
    return stimuli.Rectangle(square_size, misc.Colour('Red'), 1, None , None , square_position)

def calc_position(corner):
    return ()
    pass


"""
Experiment operations Below
"""
control.start() 
 
control.end()