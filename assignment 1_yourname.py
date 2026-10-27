# Name: Yuyang Ge
# Assignment One

"""Run with Python 3: python "assignment 1_yourname.py"."""

import colorsys
import re
import turtle


def move_pen(pen, x, y):
    """Move without leaving a line."""
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


def draw_square(pen, length):
    for side in range(4):
        pen.forward(length)
        pen.left(90)


def draw_triangle(pen, length):
    for side in range(3):
        pen.forward(length)
        pen.left(120)


def draw_star(pen, length):
    for side in range(5):
        pen.forward(length)
        pen.right(144)


def write_label(pen, x, y, text, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.color(color)
    pen.write(text, align="center", font=("Arial", size, "normal"))


def turtle_drawing():
    """Draw three shapes and a growing rainbow square pattern."""
    screen = turtle.Screen()
    screen.setup(width=1000, height=820)
    screen.title("Assignment One | Prism Garden | Yuyang Ge")
    screen.bgcolor("#081421")
    screen.colormode(1.0)
    screen.tracer(0)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(3)

    write_label(pen, 0, 337, "P R I S M   G A R D E N", 25, "#f0f7ff")
    write_label(pen, 0, 307,
                "Three simple shapes. A spectrum of possibilities.",
                11, "#93afc7")

    # Each basic shape is drawn using a structured for loop.
    pen.color("#50e3c2")
    move_pen(pen, -330, 208)
    pen.setheading(0)
    draw_square(pen, 56)
    write_label(pen, -302, 180, "SQUARE / 4 SIDES", 10, "#50e3c2")

    pen.color("#ffcf70")
    move_pen(pen, -33, 208)
    pen.setheading(0)
    draw_triangle(pen, 66)
    write_label(pen, 0, 180, "TRIANGLE / 3 SIDES", 10, "#ffcf70")

    pen.color("#ff86bc")
    move_pen(pen, 266, 250)
    pen.setheading(0)
    draw_star(pen, 73)
    write_label(pen, 302, 180, "STAR / 5 POINTS", 10, "#ff86bc")

    # The outer loop changes colour, side length and orientation.
    # draw_square() supplies the inner loop: four sides per square.
    for step in range(60):
        hue = step / 60
        color = colorsys.hsv_to_rgb(hue, 0.78, 1.0)
        length = 45 + 2 * step
        pen.color(color)
        pen.pensize(1.5)
        move_pen(pen, 0, -88)
        pen.setheading(step * 6)
        draw_square(pen, length)
        screen.update()

    move_pen(pen, 0, -88)
    pen.dot(9, "#ffffff")
    write_label(pen, 0, -352, "60 SQUARES  /  60 COLOURS  /  6-DEGREE ROTATION",
                11, "#d4e5f3")
    write_label(pen, 0, -379, "Click the drawing window to return to the menu.",
                10, "#93afc7")
    screen.update()
    screen.exitonclick()


def get_answer(question):
    """Match complete words; if several match, use the first branch below."""
    # Lowercase handles 'HKU' and 'hku'; tokenising removes punctuation.
    # Matching complete words prevents 'chair' from accidentally matching 'ai'.
    words = re.findall(r"[a-z0-9]+", question.lower())

    if "hku" in words:
        return "HKU stands for The University of Hong Kong."
    elif "robot" in words or "robots" in words:
        return ("A robot is a programmable machine that can sense its "
                "surroundings and perform physical tasks.")
    elif "jetson" in words:
        return ("Jetson Nano is an NVIDIA computer for running AI "
                "applications on an edge device.")
    elif "ai" in words:
        return ("AI means Artificial Intelligence: computer systems "
                "performing tasks such as learning and recognising patterns.")
    elif "human" in words or "humans" in words:
        return ("Humans are people who can think, learn, feel emotions "
                "and create new ideas.")
    elif "hello" in words or "hi" in words:
        return "Hello! Ask me about HKU, robot, jetson, ai or human."
    elif "help" in words:
        return "Keywords: HKU, robot, jetson, ai, human. Type exit to return."
    else:
        return ("Sorry, I do not recognise that topic. "
                "Try HKU, robot, jetson, ai or human.")


def qa_bot():
    """Keep answering questions until the user types exit or quit."""
    print("\n=== Question Answering Bot ===")
    print("Ask about HKU, robot, jetson, ai or human.")
    print("Type exit or quit to return to the menu.")

    while True:
        question = input("\nYou: ").strip()
        if question.lower() in ("exit", "quit"):
            print("Bot: Goodbye!")
            break
        elif question == "":
            print("Bot: Please enter a question.")
        else:
            print("Bot:", get_answer(question))


def calculator():
    """Optional task from the slides: a four-operation calculator."""
    print("\n=== Simple Calculator (optional) ===")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    operator = input("Choose operation (+, -, *, /): ").strip()
    if operator == "+":
        print("Result:", num1 + num2)
    elif operator == "-":
        print("Result:", num1 - num2)
    elif operator == "*":
        print("Result:", num1 * num2)
    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print("Result:", num1 / num2)
    else:
        print("Invalid operation. Choose +, -, * or /.")


def main():
    while True:
        print("\n=== Assignment One - Yuyang Ge ===")
        print("1. Turtle Drawing")
        print("2. QA Bot")
        print("3. Simple Calculator (optional)")
        print("0. Exit")
        choice = input("Choose 1, 2, 3 or 0: ").strip()

        if choice == "1":
            turtle_drawing()
        elif choice == "2":
            qa_bot()
        elif choice == "3":
            calculator()
        elif choice == "0":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 0.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nProgram ended.")
    except turtle.Terminator:
        print("\nDrawing window closed. Run the file again to restart.")
