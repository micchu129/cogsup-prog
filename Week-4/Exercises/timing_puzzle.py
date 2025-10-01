from expyriment import design, control, stimuli

exp = design.Experiment(name="timing puzzle")

# control.set_develop_mode()

"""manual parameters for ease of use for fullscreen mode"""
control.defaults.initialise_delay = 0
control.defaults.window_mode = False
control.defaults.fast_quit = True
control.defaults.auto_create_subject_id = True

def draw(stims):
    # Clear the back buffer 
    exp.screen.clear() 
    # Draw to back buffer 
    for stim in stims: 
        stim.present(clear=False, update=False) 
    # Swap the buffers 
    exp.screen.update()

control.initialize(exp)

fixation = stimuli.FixCross()
text = stimuli.TextLine("Fixation removed")

# fixation.preload() # trying preload 
# (got similar results to without preload ~0.005-.007 delay)

t0 = exp.clock.time

fixation.present()

dt = exp.clock.time - t0

exp.clock.wait(1000 - dt)

t1 = exp.clock.time
text.present()
dt1 = exp.clock.time - t1
fix_duration = (t1 - t0)/1000

exp.clock.wait(1000-dt1)

units = "second" if fix_duration == 1.0 else "seconds"
duration_text = f"Fixation was present on the screen for {fix_duration} {units}"

text2 = stimuli.TextLine(duration_text)
text2.present()
exp.clock.wait(2000)

control.end()