from expyriment import design, control, stimuli, misc
control.set_develop_mode()

exp = design.Experiment(name = "Labeled Shapes & function")

control.initialize(exp)

def generate_shape(sides = int, side_length = int, color = str, position = (int,int)): 
    return stimuli.Shape(position, misc.Colour(color), anti_aliasing=None, vertex_list=misc.geometry.vertices_regular_polygon(sides, side_length), debug_contour_colour=None)

purple_triangle = generate_shape(sides = 3, side_length = 50, color = 'purple', position = (-125,0))
yellow_hexagon = generate_shape(sides = 6, side_length = 25, color = 'yellow', position = (125,0))

line_1 = stimuli.Line((-125,43.30/2), (-125,43.30/2+50.), 3, colour=misc.Colour('white'), anti_aliasing=None)
line_2 = stimuli.Line((125,43.30/2), (125,43.30/2+50.), 3, colour=misc.Colour('white'), anti_aliasing=None)

purple_triangle_text = stimuli.TextLine('triangle', (-125,43.30/2+70.), text_font=None, text_size=None, text_bold=None, text_italic=None, text_underline=None, text_colour=misc.Colour('white'), background_colour=None, max_width=None)
yellow_hexagon_text = stimuli.TextLine('hexagon', (125,43.30/2+70.), text_font=None, text_size=None, text_bold=None, text_italic=None, text_underline=None, text_colour=misc.Colour('white'), background_colour=None, max_width=None)

control.start(subject_id=1)

purple_triangle.present(clear=True, update=False)
yellow_hexagon.present(clear=False, update=False)
line_1.present(clear=False, update=False)
line_2.present(clear=False, update=False)
purple_triangle_text.present(clear=False, update=False)
yellow_hexagon_text.present(clear=False, update=True)

exp.keyboard.wait()
control.end()