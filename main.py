import pandas
import turtle


def setup_screen(image):
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    screen.addshape(image)
    return screen


def set_text():
    writer = turtle.Turtle()
    writer.penup()
    writer.hideturtle()
    writer.color("black")
    return writer


def game(screen):
    data = pandas.read_csv("50_states.csv")
    state_list = data.state.to_list()
    writer = set_text()
    answer_state = ""

    states_guessed = 0
    guess_list = []
    while len(guess_list) < 50:
        answer_state = screen.textinput(title=f"{len(guess_list)}/50 States Correct",
                                        prompt="What's another state's name?")

        if answer_state is not None:
            answer_state = answer_state.title()

        if answer_state is None or answer_state == "Quit":
            break

        if answer_state in state_list and answer_state not in guess_list:
            data_index = data[data.state == answer_state].x.index
            x_pos = data[data.state == answer_state].x[data_index].item()
            y_pos = data[data.state == answer_state].y[data_index].item()
            writer.goto(x=x_pos, y=y_pos)
            writer.write(arg=answer_state)
            guess_list.append(answer_state)
    file_name = "states_to_learn.csv"
    miss_list = []
    if len(guess_list) < 50:
        for state in state_list:
            if state not in guess_list:
                miss_list.append(state)
    states_missed = {
        "States Missed: ": miss_list
    }
    output = pandas.DataFrame(states_missed)
    output.to_csv(file_name)



def main():
    image = "blank_states_img.gif"
    screen = setup_screen(image)
    turtle.shape(image)
    game(screen)
    screen.exitonclick()


main()
