from expyriment import design, control, stimuli, io
from expyriment.misc import constants as consts

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour= consts.C_WHITE, foreground_colour= consts.C_BLACK)
# control.set_develop_mode()
control.initialize(exp)
exp.add_data_variable_names(["test_eye", "final_radius", "final_x",  "final_y"])
quartile = exp.screen.size[0]//4


""" Stimuli """
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    return c

""" Functions """
def size_change(stim, key):
    radius0 = stim.radius
    pos0 = stim.position
    if key == consts.K_1:
        circle = make_circle(radius0*1.1, pos0)
        return circle
    elif key == consts.K_2:
        circle = make_circle(radius0*.9, pos0)
        return circle

def move_stim(stim, key):
    radius0 = stim.radius
    (x0,y0) = stim.position
    move_distance = radius0//3
    if key == consts.K_UP:
        circle = make_circle(radius0, (x0+move_distance,y0))
        return circle
    elif key == consts.K_DOWN:
        circle = make_circle(radius0, (x0-move_distance,y0))
        return circle
    elif key == consts.K_LEFT:
        circle = make_circle(radius0, (x0,y0-move_distance))
        return circle
    elif key == consts.K_RIGHT:
        circle = make_circle(radius0, (x0,y0+move_distance))
        return circle

def present_instructions(test_eye, cover_eye):
    headings = [f"Blindspot Test Instructions {i+1} - {test_eye} EYE" for i in range(4)]
    stimuli.TextScreen(headings[0],"When the trial begins, you will be presented a circle stimulus and a fixation cross.\n\nPress any key to continue instructions").present()
    exp.keyboard.wait()
    stimuli.TextScreen(headings[1], f"When the trial begins, please cover your {cover_eye} eye, and stare at the fixation cross on the {cover_eye} side of the screen.\n\nPress any key to continue instructions").present()
    exp.keyboard.wait()
    stimuli.TextScreen(headings[2],"You can adjust the circle stimulus by pressing the following keys:\n1 - Makes circle smaller\n2- Makes circle bigger\nArrow keys - moves circle in respective direction.\n\nPress any key to continue instructions").present()
    exp.keyboard.wait()
    stimuli.TextScreen(headings[3],"While staring at the fixation, keep your head still.\nAdjust the circle's location and size until it enters your blindspot.\nPress space after it enters your blind spot to complete the trial\n\nPress space when you are ready to begin the trial").present()
    exp.keyboard.wait(keys = [consts.K_SPACE])


""" Trial Function """
def run_trial(test_side):
    init_radius = 75

    if test_side == 'L' or test_side == 'LEFT':
        test_eye, cover_eye = "LEFT", "RIGHT", 
        present_instructions(test_eye, cover_eye)
        fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[quartile, 0])
        circle = make_circle(init_radius, (-quartile,0))
    elif test_side == 'R' or test_side == 'RIGHT':
        test_eye, cover_eye = "RIGHT", "LEFT"
        present_instructions(test_eye, cover_eye)
        fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[-quartile, 0])
        circle = make_circle(init_radius, (quartile,0))
    else:
        stimuli.TextScreen("Invalid Input Detected","Please pick either 'L' (left eye) or 'R' (right eye) | Press any key to exit").present()
        exp.keyboard.wait()
        control.end()
        exit()
    
    
    fixation.present(True, False)
    circle.present(False, True)

    while True:
        radius0 = circle.radius
        (x0,y0) = circle.position
        pos0 = circle.position
        key, time = exp.keyboard.wait(keys = [consts.K_1, consts.K_2, consts.K_UP, consts.K_DOWN, consts.K_LEFT, consts.K_RIGHT, consts.K_SPACE])
        if key == consts.K_SPACE:
            break
        elif key == consts.K_1 or key == consts.K_2:
            if key == consts.K_1:
                circle = make_circle(radius0*.9, pos0)
            elif key == consts.K_2:
                circle = make_circle(radius0*1.1, pos0)
        else: 
            move_distance = radius0//3
            if key == consts.K_UP:
                circle = make_circle(radius0, (x0,y0+move_distance))
            elif key == consts.K_DOWN:
                circle = make_circle(radius0, (x0,y0-move_distance))
            elif key == consts.K_LEFT:
                circle = make_circle(radius0, (x0-move_distance,y0))
            elif key == consts.K_RIGHT:
                circle = make_circle(radius0, (x0+move_distance,y0))
        fixation.present(True, False)
        circle.present(False, True)
    
    exp.data.add([test_eye, radius0, x0,  y0])

""" Experiment Control """

input_box = io.TextInput("Please enter which eye you would like to test for: either 'L' for 'left eye' or 'R' for 'right eye'")
user_input = input_box.get() 
test_side = "".join(user_input.split()).capitalize() # catch just in case user inputs blank spaces or not capitalizes the testing side

control.start(subject_id=1)

run_trial(test_side)
    
control.end()