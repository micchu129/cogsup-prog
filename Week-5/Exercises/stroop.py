from expyriment import design, control, stimuli, io, misc
from expyriment.misc import constants as consts

""" Global settings """
exp = design.Experiment(name="Stroop", background_colour= consts.C_WHITE)
# control.set_develop_mode()
control.initialize(exp)
exp.add_data_variable_names(["trial_block", "trial_number", "trial_type", "word_meaning", "text_color", "reaction_time", "accuracy"])
colors = ['red', 'blue', 'green', 'orange']

""" Stimuli """
def generate_word(trial_type):
    color_index = design.randomise.rand_int(0, len(colors)-1)
    if trial_type == 'mismatch':
        text_index = design.randomise.rand_int(0, len(colors)-1)
        while text_index == color_index: text_index = design.randomise.rand_int(0, len(colors)-1)
        text, color = colors[text_index], colors[color_index]
    else:
        text, color = colors[color_index], colors[color_index]
        
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
def present_feedback(accuracy):
    if accuracy == 1:
        stimuli.TextScreen("Corrrect! :D","The trial will continue in 1 second",heading_colour=consts.C_BLACK, text_colour=consts.C_BLACK).present()
        exp.clock.wait(1000)
    else:
        stimuli.TextScreen("Incorrrect! :c","The trial will continue in 1 second",heading_colour=consts.C_BLACK, text_colour=consts.C_BLACK).present()
        exp.clock.wait(1000)

""" Trial Function """
def run_trial():
    if design.randomise.coin_flip():
        trial_type = 'mismatch'
    else:
        trial_type = 'match'
    fixation = stimuli.FixCross()
    word, word_meaning, text_color = generate_word(trial_type)
    fixation.present(True, True)
    exp.clock.wait(500)
    word.present(True, True)
    t0 = exp.clock.time
    key, _ = exp.keyboard.wait(keys=[consts.K_f, consts.K_j])
    if trial_type == 'mismatch' and key == consts.K_j:
        accuracy = 1 
    elif trial_type == 'match' and key == consts.K_f:
        accuracy = 1 
    else:
        accuracy = 0
    rt = exp.clock.time - t0
    exp.data.add([[i+1, j+1, trial_type, word_meaning, text_color, rt, accuracy]])
    present_feedback(accuracy)

""" Experiment Control """

control.start(subject_id=1)

trial_block = range(2)

for i in trial_block:
    trials = range(10)
    present_instructions(i+1)
    for j in trials:
        run_trial()



control.end()