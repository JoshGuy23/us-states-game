import pandas
import turtle


def setup_screen(image):
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    screen.addshape(image)
    return screen


def main():
    image = "blank_states_img.gif"
    screen = setup_screen(image)
    turtle.shape(image)
    screen.exitonclick()


main()
