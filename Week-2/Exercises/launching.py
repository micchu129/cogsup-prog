from expyriment import design, control, stimuli
control.set_develop_mode()

exp = design.Experiment(name = "Two Squares")

control.initialize(exp)

#define squares
square_red = stimuli.Rectangle((50,50), (255,0,0))
square_green = stimuli.Rectangle((50,50), (0,255,0))

#set position of square, red is left
square_red.position = (-400, 0)
square_green.position = (0, 0)

#global speed?
speed = 5

control.start(subject_id=1)

square_red.present(clear=True, update=False)
square_green.present(clear=False, update=True)


def time_steps(pixels_per_tick, distance):
    """Return how many ticks it takes to cover `distance`
    given a speed in pixels per tick.
    """
    if pixels_per_tick <= 0:
        raise ValueError("Speed must be > 0")
    return int(distance / pixels_per_tick)

for i in range(time_steps(speed, 350)):
    square_red.move((speed,0))
    square_red.present(clear = True, update=False)
    square_green.present(clear = False, update = True)

for i in range(time_steps(speed, 400)):
    square_green.move((speed,0))
    square_red.present(clear = True, update=False)
    square_green.present(clear = False, update = True)

exp.keyboard.wait()
control.end()