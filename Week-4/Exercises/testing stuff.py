from expyriment import design, control, stimuli, misc

exp = design.Experiment(background_colour=misc.Colour('grey'))

control.set_develop_mode()
control.initialize(exp)

circle = stimuli.Circle(50, misc.Colour('blue'), position=(-100,100))
tag = stimuli.Circle(20, misc.Colour('red'))

exp.screen.clear()
tag.plot(circle)
circle.present(clear=False, update= False)

exp.screen.update()

exp.keyboard.wait()

circle.move((30,30))
circle.present()


exp.keyboard.wait()  



control.end()