from expyriment import design, control, stimuli, misc

"""Globals"""
fps = 60
gap_ratio = 0.25 # currently set relative to diameter
tag_ratio = 0.3 # size of tag relative to size of circles
frames = 30
circle_radius = 60
high_isi = 18

"""helpers"""

def load(stims):
    for stim in stims:
        stim.preload()

def present_for(stims, frames=int):
    exp.screen.clear()
    t0 = exp.clock.time
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
    colors = ['yellow', 'red', 'green', 'yellow']
    tags = [stimuli.Circle(circle_radius*tag_ratio, colour= misc.Colour(color)) for color in colors]
    for i, circle in enumerate(circles):
        tags[i].plot(circle)

def run_trial(circle_radius = int, isi = int, color_tags = False):
    stimuli.TextLine(f"Circle Radius: {circle_radius} | ISI: {isi} ~ {isi*1000/fps}ms| Color Tags: {color_tags}", text_colour= misc.Colour('black')).present()
    exp.keyboard.wait()
    circles = make_circles(circle_radius)
    if color_tags:
        add_tags(circles)
    while True:
        present_for(circles[:3],frames)
        if isi: present_for([], isi)
        present_for(circles[1:],frames)
        if isi: present_for([], isi)
        if exp.keyboard.check(misc.constants.K_SPACE):
            break


""" Test functions """
exp = design.Experiment(background_colour=misc.Colour('grey'))

control.set_develop_mode()
control.initialize(exp)

run_trial(circle_radius,0,False)
run_trial(circle_radius,high_isi,False)
run_trial(circle_radius,high_isi,True)

control.end()