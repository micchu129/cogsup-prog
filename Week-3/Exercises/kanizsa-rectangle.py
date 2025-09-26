from expyriment import design, control, stimuli, misc 


# Get Color List
# print(misc.Colour.get_colour_names())

# Global settings
# control.set_develop_mode()
background_colour= misc.constants.C_GREY


exp = design.Experiment(name = "Kaniza Rectangle", background_colour = background_colour) 
control.initialize(exp) 

screen_w, screen_h = exp.screen.size
base_recangle_width = screen_w//4 
base_circle_radius = screen_w//20
rectangle_position = (0, 0)

# print(misc.Colour.get_colour_names()) # get color list in expyriment... not that useful

## troubleshooting prints
# print("size:", exp.screen.size)
# print("square_length: ", square_length)

## helper functions

def generate_circle(scaling_factor=1, circle_position = (0,0), circle_color = None): 
    return stimuli.Circle(scaling_factor*base_circle_radius, colour= circle_color, line_width=None, position= circle_position, anti_aliasing=None)

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

def calc_ratio(ratio=(int,int)):
    return ratio[0]/ratio[1]

def calc_rectangle_size(ratio, rec_scale):
    w = base_recangle_width * rec_scale
    h = w/ratio
    return (w,h)

"""
Stimuli and design (trial and block structures)
"""

## primary function

# The aspect ratio of the rectangle. 
    # implemented as a tuple here 
    # hopefully easier for user input and the math is calculated in the helper function
    # example: if scale_factor = 1, and ratio is 2:1
        # width of rectangle = 25% screen width
        # height of rectangle = 12.5% screen width
# The scaling factor for the rectangle.
    # higher number scales to bigger rectangle, scale_factor * base_rectangle_width
    # when scale_factor is 1, rectangle width will be 25% of screen width 
# The scaling factor for the circles.
    # same concept as above, base_radius defined as 5% of screen width but adjustable in settings

def kanizsa_rectangle(aspect_ratio=(2,1), rectangle_scaling_factor=1, circle_scaling_factor=1):
    ratio = calc_ratio(aspect_ratio)
    rectangle_size = calc_rectangle_size(ratio, rectangle_scaling_factor)
    colors = [misc.Colour('black'),misc.Colour('white'),misc.Colour('black'),misc.Colour('white')]

    central_rectangle = stimuli.Rectangle(rectangle_size, colour=background_colour, position=rectangle_position)
    
    corners = calc_square_corners(central_rectangle)

    circles = [generate_circle(scaling_factor=circle_scaling_factor, circle_position = pos, circle_color=color) for pos, color in zip(corners,colors)]

    shapes = circles.copy()

    shapes.append(central_rectangle)

    return shapes

# test = kanizsa_rectangle(aspect_ratio=(2,1), rectangle_scaling_factor=1, circle_scaling_factor=1)
# print(test)
# print(type(test))


"""
Experiment operations Below
"""
control.start() 

# test_circle.present(clear=True, update= True) # confirming helper function works
# central_square.colour = misc.Colour('black') # testing through changing colors just to make sure square works

exp.screen.clear()

for shape in kanizsa_rectangle(aspect_ratio=(4,3), rectangle_scaling_factor=2, circle_scaling_factor=2):
    shape.present(clear= False, update = False)

exp.screen.update()



exp.keyboard.wait()
control.end()