from tkinter import *

window = Tk()
window.minsize(width=300, height=150)
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)
enter_value_label = Label(text="Enter value:", font=12)
enter_value_label.grid(row=0, column=0)


def label_maker(text, row, column, font_l=12, ):
    labels = Label(text=text, font=font_l)
    labels.grid(row=row, column=column)


def calculate(miles):
    answer_l = float(miles) * 1.60934
    label_maker(text=answer_l, row=1, column=1)

    if answer_l == 1:
        label_maker(text='km', row=1, column=2)
    else:
        label_maker(text='kms', row=1, column=2)


label_maker(text="miles", row=0, column=2)

miles_entry = Entry(width=9)
miles_entry.grid(row=0, column=1)

label_maker(text="The Answer:", row=1, column=0)

calculate_button = Button(text="calculate", font=12, command=lambda: calculate(miles_entry.get()))
calculate_button.grid(row=2, column=1)

window.mainloop()
