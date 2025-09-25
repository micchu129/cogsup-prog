from expyriment import design, control, stimuli, misc 


# Get Color List
# print(misc.Colour.get_colour_names())

# Global settings
# control.set_develop_mode()


exp = design.Experiment(name = "Kaniza Square", background_colour= misc.constants.C_GREY) 
control.initialize(exp) 

screen_w, screen_h = exp.screen.size
square_length = screen_w//4
circle_radius = screen_w//20
square_position = (0, 0)

square_size = (square_length, square_length)
distance_from_edge = square_length//2

# print(misc.Colour.get_colour_names()) # get color list in expyriment... not that useful

## troubleshooting prints
# print("size:", exp.screen.size)
# print("square_length: ", square_length)

## helper functions

def generate_circle(circle_position = (0,0), circle_color = None): 
    return stimuli.Circle(circle_radius, colour= circle_color, line_width=None, position= circle_position, anti_aliasing=None)

# test_circle = generate_circle(circle_color = misc.Colour('black'))

## calculating corners of a given square relative to its absolute position
def calc_square_corners(square):
    w,h = square.size
    x,y = square.absolute_position
    corners = []
    for i in (-w, w):
        for j in (h, -h):
            corners.append((x+i//2,y+j//2))
    
    return corners #top_left, bottom_left, top_right, bottom_right

"""
Stimuli and design (trial and block structures)
"""
## hard coding colors cuz this seems most efficient?
colors = [misc.Colour('black'),misc.Colour('white'),misc.Colour('black'),misc.Colour('white')]

## initialize central square
central_square = stimuli.Rectangle(square_size, colour=misc.constants.C_GREY, position=square_position)
# print("corners: ", calc_square_corners(central_square)) # 

## list of corners of central square
corners = calc_square_corners(central_square)

## generate circles
circles = [generate_circle(pos, color) for pos, color in zip(corners,colors)]

"""
Experiment operations Below
"""
control.start() 

# test_circle.present(clear=True, update= True) # confirming helper function works
# central_square.colour = misc.Colour('black') # testing through changing colors just to make sure square works

exp.screen.clear()

for circle in circles:
    circle.present(clear= False, update = False)

central_square.present(clear = False, update= False)

exp.screen.update()



exp.keyboard.wait()
control.end()