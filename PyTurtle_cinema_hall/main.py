import turtle

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
HALL_HEADER = 75
FONT_SIZE = 12
INDENTION = 10

ROW = 10
COLUMN = 12

main_screen = turtle.Screen()
main_screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
main_screen.setworldcoordinates(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
main_screen.title('Cinema')
main_screen.bgcolor('MintCream')

main_pen = turtle.Turtle()
main_pen.hideturtle()
main_pen.speed(0)
main_pen.penup()

main_text = turtle.Turtle()
main_text.hideturtle()
main_text.speed(0)
main_text.penup()

screen_pen = turtle.Turtle()
screen_pen.hideturtle()
screen_pen.color('MintCream')
screen_pen.speed(0)
screen_pen.penup()

seats = {}

cell_width = main_screen.window_width() / COLUMN
cell_height = (main_screen.window_height() - HALL_HEADER) / ROW
seat_radius = (cell_height / 2) * 0.8

x = cell_width / 2
y = (cell_height / 2) - seat_radius


for row in range(ROW):
    for col in range(COLUMN):
        seats[(x, y)] = False
        x += cell_width
    x = cell_width / 2
    y += cell_height

def write_seats_count():
    main_screen.tracer(False)
    main_text.clear()
    main_text.setposition (INDENTION, (main_screen.window_height() - (FONT_SIZE * 2)) )
    main_text.pendown()
    free_seats = len(seats) - sum(seats.values())
    main_text.write(f"Free seats: {free_seats}", font=('Roboto', FONT_SIZE, 'italic'))
    main_text.penup()

    main_text.setposition (INDENTION, (main_screen.window_height() - (FONT_SIZE * 4)) )
    main_text.pendown()
    sold_seats = sum(seats.values())
    main_text.write(f"Sold seats: {sold_seats}", font=('Roboto', FONT_SIZE, 'italic'))
    main_text.penup()
    main_screen.tracer(True)

def draw_seat(x, y, color = 'lightSeaGreen'): 
    main_pen.setposition(x, y)
    main_pen.pendown()
    main_pen.begin_fill()
    main_pen.circle(seat_radius)
    main_pen.fillcolor(color)
    main_pen.end_fill()
    main_pen.penup()


def draw_screen(): 
    main_screen.tracer(False)
    screen_pen.setposition(INDENTION, (main_screen.window_height() - HALL_HEADER + INDENTION * 2))
    screen_pen.pendown()
    screen_pen.begin_fill()
    screen_pen.forward(main_screen.window_width() - INDENTION * 2)
    screen_pen.right(90)
    screen_pen.forward(INDENTION)
    screen_pen.right(90)
    screen_pen.forward(main_screen.window_width() - INDENTION * 2)
    screen_pen.right(90)
    screen_pen.forward(INDENTION)
    screen_pen.fillcolor('steel blue')
    screen_pen.end_fill()
    screen_pen.penup()

    screen_pen.setposition((main_screen.window_width() / 2) - FONT_SIZE, (main_screen.window_height() - HALL_HEADER + (INDENTION * 2) - FONT_SIZE * 0.85))
    screen_pen.pendown()
    screen_pen.write("Screen", font=('Roboto', int(FONT_SIZE / 2), 'bold'))
    screen_pen.penup()
    main_screen.tracer(True)


def get_seat(x, y):
    for _x, _y in seats:
        distance = ((x - _x)**2 + (y - (_y + seat_radius))**2)**0.5
        if distance <= seat_radius:
            return _x, _y

def left_click_handler(x, y): 
    seat = get_seat(x, y)
    if seat:
        draw_seat(*seat, 'light grey')
        seats[seat] = True
        write_seats_count()

def right_click_handler(x, y): 
    seat = get_seat(x, y)
    if seat:
        draw_seat(*seat)
        seats[seat] = False
        write_seats_count()

main_screen.tracer(False)
for seat in seats:
    draw_seat(*seat)
main_screen.tracer(True)

draw_screen()
write_seats_count()
main_screen.onclick(left_click_handler)
main_screen.onclick(right_click_handler, btn = 3)
main_screen.mainloop()