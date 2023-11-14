import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=205)


miles_entry = tkinter.Entry(width=10)
miles_entry.grid(column=1, row=0)

my_label = tkinter.Label(text="Miles", font=("Arial", 12, "normal"))
my_label.grid(column=2, row=0)


result = 0


def button_clicked():
    result = 1.609 * int(miles_entry.get())
    label3["text"] = str(result)


button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=2)

label2 = tkinter.Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = tkinter.Label(text=result, font=("Arial", 12, "normal"))
label3.grid(column=1, row=1)

label4 = tkinter.Label(text="Km")
label4.grid(column=2, row=1)
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(2, 3, 4, 5))

window.mainloop()
