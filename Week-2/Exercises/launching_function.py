from expyriment import design, control, stimuli
control.set_develop_mode()

#global variables
Speed = 6

exp = design.Experiment(name="Launching Function")
control.initialize(exp)

#helper
def time_steps(pixels_per_tick, distance):
    """Return how many ticks it takes to cover `distance` at `pixels_per_tick`."""
    if pixels_per_tick <= 0:
        raise ValueError("Speed must be > 0")
    return int(distance / float(pixels_per_tick))

def reset_positions():
    red.position   = (-400, 0)
    green.position = (0,0)

def present():
    # initializes positions
    red.present(clear=True, update=False)
    green.present(clear=False, update=True)

def launching_function(
                    temporal_gap_ms=0,
                    spatial_gap_px=0,
                    green_speed_factor=1.0):
    """
    Display one horizontal launching event:

    - temporal_gap_ms: delay (ms) after red stops & before green starts
    - spatial_gap_px : positive gap to *leave* between red & green at "contact"
    - green_speed_factor: 1.0 = same speed; >1.0 = faster (triggering)
    """
    # Show starting positions briefly
    present()
    exp.clock.wait(1000)

    # red moves towards green for contact
    for i in range(time_steps(Speed, 350-spatial_gap_px)):
        red.move((Speed,0))
        red.present(clear = True, update=False)
        green.present(clear = False, update = True)

    # Optional temporal delay (disrupt time)
    if temporal_gap_ms > 0:
        exp.clock.wait(temporal_gap_ms)

    # --- GREEN moves to the right for *the same distance the red just traveled* ---
    green_speed = Speed * float(green_speed_factor)
    for i in range(time_steps(green_speed, 350)):
        green.move((green_speed,0))
        red.present(clear = True, update=False)
        green.present(clear = False, update = True)

    # Hold the final frame
    exp.clock.wait(1000)

#initializing squares
red   = stimuli.Rectangle((50,50), (255,0,0))
green = stimuli.Rectangle((50,50), (0,255,0))

control.start(subject_id=1)

# 1) Michottean launching (no gaps, same speed)
reset_positions()
launching_function(
                temporal_gap_ms=0,
                spatial_gap_px=0,
                green_speed_factor=1.0)

# 2) Launching with a temporal gap
reset_positions()
launching_function(
                temporal_gap_ms=1500,
                spatial_gap_px=0,
                green_speed_factor=1.0)

# 3) Launching with a spatial gap
reset_positions()
launching_function(
                temporal_gap_ms=0,
                spatial_gap_px=50,
                green_speed_factor=1.0)

# 4) Triggering
reset_positions()
launching_function(
                temporal_gap_ms=0,
                spatial_gap_px=0,
                green_speed_factor=4.0)

control.end()