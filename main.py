min_sides = 4
max_sides = 9
sides = 6


def show_current():
    basic.show_number(sides)


def on_button_pressed_a():
    global sides
    sides = sides - 1
    if sides < min_sides:
        sides = min_sides
    show_current()
input.on_button_pressed(Button.A, on_button_pressed_a)


def on_button_pressed_b():
    global sides
    sides = sides + 1
    if sides > max_sides:
        sides = max_sides
    show_current()
input.on_button_pressed(Button.B, on_button_pressed_b)


def on_button_pressed_ab():
    result = Math.random_range(1, sides)
    basic.show_number(result)
input.on_button_pressed(Button.AB, on_button_pressed_ab)


show_current()
