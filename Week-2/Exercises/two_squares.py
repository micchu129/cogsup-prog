from expyriment import design, control, stimuli
control.set_develop_mode()

exp = design.Experiment(name = "Two Squares")

control.initialize(exp)

square_1 = stimuli.Rectangle((50,50), (0,0,255))
square_2 = stimuli.Rectangle((50,50), (255,255,255))

square_1.position = (125, 0)
square_2.position = (-125, 0)

control.start(subject_id=1)

square_1.present(clear=True, update=False)
square_2.present(clear=False, update=True)

exp.keyboard.wait()
control.end()