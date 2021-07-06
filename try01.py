import tkinter as tk

def show_output():
    number = int(number_input.get())
    if number ==0:
        output_label.configure(text='ได้ 0 ไง')
        return

    output = ''
    for i in range(1,13):
        output += str(number) + ' x ' + str(i)
        output += ' = '+ str(number*i) + '\n'

    output_label.configure(text=output)

window = tk.Tk()

window.iconbitmap('Multiplication table.ico')
window.option_add("*Font","consola 18")
background_image = tk.PhotoImage(file= 'Untitled-2.png')
background_label = tk.Label( image= background_image)
background_label.place(relwidth=1,relheight=1)

window.title('Multiplication table')
window.minsize(width=400, height=650)

title_lable = tk.Label(master=window, text='สูตรคุณแม่',width=15)
title_lable.pack(pady=30)

number_input = tk.Entry(master=window)
number_input.pack()

go_botton = tk.Button(master=window,text='ได้แก่', command=show_output, width=15)
go_botton.pack(pady=10)

output_label = tk.Label(master=window)
output_label.pack(pady=50)

window.mainloop()
