from expyriment import design, control, stimuli
control.set_develop_mode()

exp = design.Experiment(name = "Two Squares")

control.initialize(exp)

#define squares
square_red = stimuli.Rectangle((50,50), (255,0,0))
square_green = stimuli.Rectangle((50,50), (0,255,0))

square_1.position = (125, 0)
square_2.position = (-125, 0)

control.start(subject_id=1)

square_1.present(clear=True, update=False)
square_2.present(clear=False, update=True)

exp.clock.wait(1000) #presents position for 1 second

def time_steps(pixels_per_tick, distance):
    """Return how many ticks it takes to cover `distance`
    given a speed in pixels per tick.
    """
    if pixels_per_tick <= 0:
        raise ValueError("Speed must be > 0")
    return int(distance / pixels_per_tick)

#square_red covers distance between itself and green (factoring in 'radius) and stops upon 'contact'
for i in range(time_steps(speed, 350)):
    square_red.move((speed,0))
    square_red.present(clear = True, update=False)
    square_green.present(clear = False, update = True)

#square_green moves upon 'collision' distance variable in timesteps function can be altered to determine how far it travels after contact. set to 350 according to instrucitons
for i in range(time_steps(speed, 350)):
    square_green.move((speed,0))
    square_red.present(clear = True, update=False)
    square_green.present(clear = False, update = True)

#display for 1 second
exp.clock.wait(1000)

control.end()