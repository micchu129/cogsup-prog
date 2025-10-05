from expyriment import design, control, stimuli, misc

"""Globals"""
fps = 60 #fps defined by moniter hz
gap_ratio = 0.25 # defines gap between circles, currently set relative to diameter
tag_ratio = 0.3 # size of tags relative to size of circles
frames_displayed = 30 #controls how long the stimuli is displayed for 
circle_radius = 60 #self explanatory?
high_isi = 18 #defining a high isi scenario to be used for both trial 2 and 3 (can be custom per trial)

"""helpers"""

def load(stims):
    for stim in stims:
        stim.preload()

def present_for(stims, frames=fps): # default presentation = 1 second
    t0 = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(False, False)
    exp.screen.update()
    dt = exp.clock.time - t0
    time = frames*1000/fps #msec/frame
    exp.clock.wait(time - dt)
    exp.screen.clear()

def make_circles(circle_radius = int):
    circle_diameter = circle_radius*2
    gap = circle_diameter * gap_ratio
    screen_w = exp.screen.size[0]
    total_length = circle_diameter*4 + gap*3 # diameter of 4 circles + 3 gaps, based on the gap ratio in global (radius or diameter * ratio #not decided yet)
    positions = []
    x0 = -total_length//2+ circle_radius
    if total_length > screen_w or x0 < -screen_w//2:
        print("Total Length is wider than screen, please adjust parameters")
        control.end()
    for i in range(4):
        positions.append((x0,0))
        x0 += circle_diameter+gap
    circles = [stimuli.Circle(circle_radius, misc.Colour("blue"), position=pos) for pos in positions]

    return circles

def add_tags(circles):
    colors = ['yellow', 'red', 'green', 'yellow'] # define the list of colors to be used for tags, simpler to hardcode
    tags = [stimuli.Circle(circle_radius*tag_ratio, colour= misc.Colour(color)) for color in colors] # create tags based on global circle_radius and amount of colors, attempted to write this for per set of circles but had trouble accessing value (not applicable in my implementation either)
    for i, circle in enumerate(circles):
        tags[i].plot(circle) #plots each tag onto each circle with equivalent index. i realize this breaks if #colors != #circles but 

def run_trial(circle_radius = int, isi = int, color_tags = False):
    stimuli.TextLine(f"Circle Radius: {circle_radius} | ISI: {isi} ~ {isi*1000/fps}ms| Color Tags: {color_tags}", text_colour= misc.Colour('black')).present() #all in one line for compactness, displays the conditions of the coming trial (could be used as a verbose debug)
    exp.keyboard.wait()
    circles = make_circles(circle_radius)
    if color_tags:
        add_tags(circles)
    while True:
        present_for(circles[:3],frames_displayed) # displays first 3 circles for global defined duration
        if isi: present_for([], isi) # checks if isi != 0, if not zero, then display nothing for ici frames
        present_for(circles[1:],frames_displayed) # displayed last 3 circles for defined duration
        if isi: present_for([], isi) # same as 2 lines above
        if exp.keyboard.check(misc.constants.K_SPACE): #end loop when space is pressed
            break


""" experiment design """
exp = design.Experiment(background_colour=misc.Colour('grey'))

control.set_develop_mode()
control.initialize(exp)

run_trial(circle_radius,0,False)
run_trial(circle_radius,high_isi,False)
run_trial(circle_radius,high_isi,True)

control.end()