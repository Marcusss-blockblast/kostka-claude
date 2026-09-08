let min_sides = 4
let max_sides = 9
let sides = 6
function show_current() {
    basic.showNumber(sides)
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    sides = sides - 1
    if (sides < min_sides) {
        sides = min_sides
    }
    
    show_current()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    sides = sides + 1
    if (sides > max_sides) {
        sides = max_sides
    }
    
    show_current()
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    let result = Math.randomRange(1, sides)
    basic.showNumber(result)
})
show_current()
