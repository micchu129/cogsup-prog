from expyriment import design, control, stimuli, io, misc
from expyriment.misc import constants as consts

## Clarifications:
"""
I had already completed the assignment the week before.
I have chosen to continue using my code as I am familiar with its functions
and am able to manipulate its content as I wish.

I have integrated from the assignment codes that improve upon my code.

thank you for your understanding
"""

""" Global settings """
exp = design.Experiment(name="Stroop", background_colour= consts.C_WHITE)
# control.set_develop_mode()
control.initialize(exp)
exp.add_data_variable_names(["trial_block", "trial_number", "trial_type", "word_meaning", "text_color", "reaction_time", "correct"])

COLORS = ['red', 'blue', 'green', 'orange']

TOTAL_N_TRIALS = None
N_BLOCKS = 2
N_TRIALS_IN_BLOCK = 3

""" Stimuli """
fixation = stimuli.FixCross()
fixation.preload()

def generate_word(trial_type):
    color_index = design.randomise.rand_int(0, len(COLORS)-1) # select a color
    if trial_type == 'mismatch':
        text_index = design.randomise.rand_int(0, len(COLORS)-1) # if mismatch, select a different number for text
        while text_index == color_index: text_index = design.randomise.rand_int(0, len(COLORS)-1) # if numbers match, keep selecting
        text, color = COLORS[text_index], COLORS[color_index]
    else:
        text, color = COLORS[color_index], COLORS[color_index]
        
    trial_stim = stimuli.TextLine(text,text_size=30, text_colour=misc.Colour(color))
    return trial_stim, text, color

""" Functions """
def present_instructions(trial_block):
    stimuli.TextScreen(f"Stroop Test Trial Block {trial_block}","When the trials begins, you will be presented one of the following words:\nred, blue, green, orange\nand the word will be colored with one of the four colors.\n\nPress any key to continue instructions", heading_colour=consts.C_BLACK, text_colour=consts.C_BLACK).present()
    exp.keyboard.wait()
    stimuli.TextScreen(f"Stroop Test Trial Block {trial_block}","If the color of the word matches the written text, press the 'F' key.\nIf the color of the word does not match the written text, press the 'J' key.\nNote: Orange color can look a little yellow.\n\nPress any key to continue instructions", heading_colour=consts.C_BLACK, text_colour=consts.C_BLACK).present()
    exp.keyboard.wait()
    stimuli.TextScreen(f"Stroop Test Trial Block {trial_block}",f"The entire test will be split into 2 trial blocks, each with 10 trials (words presented)\nYou are currently on Trial Block {trial_block}, which means there are {(3-trial_block)*10} trials left.\n\nPress 'G' to begin trials", heading_colour=consts.C_BLACK, text_colour=consts.C_BLACK).present()
    exp.keyboard.wait(keys = [consts.K_g])

def present_feedback(correct):
    if correct == 1:
        stimuli.TextScreen("Corrrect! :D","The trial will continue in 1 second",heading_colour=consts.C_BLACK, text_colour=consts.C_BLACK).present()
        exp.clock.wait(1000)
    else:
        stimuli.TextScreen("Incorrrect! :c","The trial will continue in 1 second",heading_colour=consts.C_BLACK, text_colour=consts.C_BLACK).present()
        exp.clock.wait(1000)

def present_fixation(wait_time): 
    t0 = exp.clock.time
    fixation.present()
    t1 = exp.clock.time
    dt = t1 - t0
    exp.clock.wait(wait_time - dt)

def decide_trial_type():
    if design.randomise.coin_flip():
        trial_type = 'mismatch'
    else:
        trial_type = 'match'
    return trial_type

def present_stimuli(word, trial_type):
    word.present()
    key, rt = exp.keyboard.wait(keys=[consts.K_f, consts.K_j])
    correct = key == consts.K_f if trial_type == "match" else key == consts.K_j
    return correct, rt

""" Trial Function """
def run_trial():
    trial_type = decide_trial_type()
    word, word_meaning, text_color = generate_word(trial_type)
    present_fixation(500) # wait time is input
    correct, rt = present_stimuli(word, trial_type)
    exp.data.add([[i, j, trial_type, word_meaning, text_color, rt, correct]])
    present_feedback(correct)

""" Experiment Control """

control.start(subject_id=1)

trial_block = range(1, N_BLOCKS+1)

for i in trial_block:
    trials = range(1, N_TRIALS_IN_BLOCK+1)
    present_instructions(i)
    for j in trials:
        run_trial()

control.end()