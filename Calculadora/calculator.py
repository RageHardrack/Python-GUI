from tkinter import *
import parser

window = Tk()
window.title('Simple Calculator by Dan Colmenares')
window.config(bg='grey')

display = Entry(window, width=20, borderwidth=5, bg='white')
display.grid(row=0, column=0, columnspan=6, sticky=W+E)

button_width = 5
button_height = 2

counting = 0

# Functions
def get_numbers(n):
    global counting
    display.insert(counting, n)
    counting += 1

def get_operation(operator):
    global counting
    operator_length = len(operator)
    display.insert(counting, operator)
    counting += operator_length

def clear_display():
    display.delete(0, END)

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()
        display.insert(0, 'Error')

def calculate():
    display_state = display.get()
    try:
        math_expression = parser.expr(display_state).compile()
        result = eval(math_expression)
        clear_display()
        display.insert(0, result)
    except:
        clear_display()
        display.insert(0, 'Error')

# Numeric Buttons
buttonOne = Button(window, text='1', command=lambda: get_numbers(1), width=button_width, height=button_height).grid(row=4, column=0, sticky=W+E)
buttonTwo = Button(window, text='2', command=lambda: get_numbers(2), width=button_width, height=button_height).grid(row=4, column=1, sticky=W+E)
buttonThree = Button(window, text='3', command=lambda: get_numbers(3), width=button_width, height=button_height).grid(row=4, column=2, sticky=W+E)

buttonFour = Button(window, text='4', command=lambda: get_numbers(4), width=button_width, height=button_height).grid(row=3, column=0, sticky=W+E)
buttonFive = Button(window, text='5', command=lambda: get_numbers(5), width=button_width, height=button_height).grid(row=3, column=1, sticky=W+E)
buttonSix = Button(window, text='6', command=lambda: get_numbers(6), width=button_width, height=button_height).grid(row=3, column=2, sticky=W+E)

buttonSeven = Button(window, text='7', command=lambda: get_numbers(7), width=button_width, height=button_height).grid(row=2, column=0, sticky=W+E)
buttonEight = Button(window, text='8', command=lambda: get_numbers(8), width=button_width, height=button_height).grid(row=2, column=1, sticky=W+E)
buttonNine = Button(window, text='9', command=lambda: get_numbers(9), width=button_width, height=button_height).grid(row=2, column=2, sticky=W+E)
buttonZero = Button(window, text='0', command=lambda: get_numbers(0), width=button_width, height=button_height).grid(row=5, column=1, sticky=W+E)

# Operation Buttons
Button(window, text="AC", command=lambda: clear_display(), width=button_width, height=button_height).grid(row=5, column=0, sticky=W+E)
Button(window, text="0", command=lambda: get_numbers(0), width=button_width, height=button_height).grid(row=5, column=1, sticky=W+E)
Button(window, text="%", command=lambda: get_operation("%"), width=button_width, height=button_height).grid(row=5, column=2, sticky=W+E)

Button(window, text="+", command=lambda: get_operation("+"), width=button_width, height=button_height).grid(row=2, column=3, sticky=W+E)
Button(window, text="-", command=lambda: get_operation("-"), width=button_width, height=button_height).grid(row=3, column=3, sticky=W+E)
Button(window, text="*", command=lambda: get_operation("*"), width=button_width, height=button_height).grid(row=4, column=3, sticky=W+E)
Button(window, text="/", command=lambda: get_operation("/"), width=button_width, height=button_height).grid(row=5, column=3, sticky=W+E)

Button(window, text="BACK", command=lambda: undo(), width=button_width, height=button_height).grid(row=2, column=3, sticky=W+E, columnspan=4)
Button(window, text="exp", command=lambda: get_operation("**"), width=button_width, height=button_height).grid(row=3, column=4, sticky=W+E)
Button(window, text="^2", command=lambda: get_operation("**2"), width=button_width, height=button_height).grid(row=3, column=5, sticky=W+E)
Button(window, text='(', command=lambda: get_operation("("), width=button_width, height=button_height).grid(row=4, column=4, sticky=W+E)
Button(window, text=")", command=lambda: get_operation(")"), width=button_width, height=button_height).grid(row=4, column=5, sticky=W+E)
Button(window, text="=", command=lambda:calculate(), width=button_width, height=button_height).grid(row=5, column=4, sticky=W+E, columnspan=2)

window.mainloop()