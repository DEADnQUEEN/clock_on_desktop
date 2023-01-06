import datetime
import time
import tkinter


back = '#333333' #backgrond color
fg = '#ffffff' #color of text
possible_pos = ['nw', 'n', 'ne', 'w', 'center', 'e', 'sw', 's', 'se']
font = 'JetBrains Mono'
bd = 1

rgb_code = [f'{i}' for i in range(10)]
rgb_code.extend([j for j in 'abcdef'])
print(rgb_code)

main_bg = []
primary_bg = []
text_color_buttons = []

with open('words.txt', 'r') as text:
    text = text.readlines()
    for i in range(len(text)):
        text[i] = text[i].rstrip('\n')


def borderizer(x: int, y: int, w: int, h: int, border=bd):
    if x <= border:
        x = border

    if y <= border:
        y = border

    if w <= border:
        w = 0

    if h <= border:
        h = 0

    lbl = tkinter.Label(window, background=fg)
    lbl.place(x=x - border, y=y - border, width=w + (2 * border), height=h + (2 * border))

    return lbl


def color_btn():
    return tkinter.Button(window,
                          text='colorize'.upper(),
                          background=back,
                          fg='white',
                          borderwidth=0,
                          command=lambda: color())


def entry_place():
    return tkinter.Entry(window,
                         font=(font, 16),
                         justify='left',
                         background='white',
                         foreground='#333333')


def color():
    global back, fg, main_bg, primary_bg

    if len(entry_main_color.get()) == 6:
        for f in entry_main_color.get().lower():
            if f not in rgb_code:
                break
        else:
            back = f'#{entry_main_color.get().lower()}'
            for k in main_bg:
                k.config(background=back)

    if len(entry_primary_color.get()) == 6:
        for f in entry_primary_color.get().lower():
            if f not in rgb_code:
                break
        else:
            fg = f'#{entry_primary_color.get().lower()}'
            for k in primary_bg:
                k.config(background=fg)

            for k in text_color_buttons:
                k.config(foreground=fg)


def clock_app(pos: str in possible_pos):
    res_x = app.winfo_screenwidth()
    res_y = app.winfo_screenheight()

    app.destroy()
    print(pos)

    clock = tkinter.Tk()
    clock.overrideredirect(True)
    clock.resizable(width=False, height=False)
    clock.attributes("-topmost", True)

    lbl = tkinter.Label(clock,
                        text=f'{datetime.datetime.now().time().strftime("%H:%M:%S")}',
                        anchor=pos,
                        background=back,
                        fg=fg,
                        font=('Arial Black', 15))
    quiter = tkinter.Button(clock,
                            borderwidth=0,
                            text='close',
                            relief='flat',
                            anchor=pos,
                            background=back,
                            fg=fg,
                            font=('Arial Black', 15),
                            command=lambda: clock.destroy())

    w_size = 100
    h_size = 60

    if pos in ['nw', 'n', 'ne']:
        y = 0
    elif pos in ['w', 'center', 'e']:
        y = round((res_y - h_size) / 2)
    elif pos in ['sw', 's', 'se']:
        y = res_y - h_size
    else:
        raise Exception('?????????????????')

    if pos in ['nw', 'w', 'sw']:
        x = 0
    elif pos in ['n', 'center', 's']:
        x = round((res_x - w_size) / 2)
    elif pos in ['ne', 'e', 'se']:
        x = res_x - w_size
    else:
        raise Exception('!!!!!!!!!!!!!!!!!!!!!!!!!!')

    lbl.place(x=0, y=0, width=w_size, height=round(h_size / 2))
    quiter.place(x=0, y=round(h_size / 2), width=w_size, height=round(h_size / 2))

    clock.geometry(f'{w_size}x{h_size}+{x}+{y}')

    while True:
        time.sleep(1)
        lbl.config(text=f'{datetime.datetime.now().time().strftime("%H:%M:%S")}')
        clock.update()


app = tkinter.Tk()
app.overrideredirect(True)
app.resizable(width=False, height=False)
app.geometry(f'1000x600+{int(app.winfo_screenwidth() / 2 - 500)}+{int(app.winfo_screenheight() / 2 - 300)}')
title_bar = tkinter.Frame(app,
                          relief='flat',
                          background=back,
                          bd=2)
main_bg.append(title_bar)
close = tkinter.Button(app,
                       bg='#ed4245',
                       text='X',
                       font=(font, 14),
                       borderwidth=0,
                       border=None,
                       anchor='center',
                       command=lambda: app.destroy()
                       )

title_bar.place(x=0, y=0, width=1000, height=40)
close.place(x=960, y=0, width=40, height=40)

window = tkinter.Frame(app,
                       background=back)
window.place(x=0, y=40, width=1000, height=600)
main_bg.append(window)

#borders
btn_border_line = borderizer(x=549, y=149, w=302, h=302)
top_border_line = borderizer(x=0, y=0, w=1000, h=bd)

primary_bg.extend([top_border_line, btn_border_line])

#buttons of places
for i in range(3):
    for j in range(3):
        btn = tkinter.Button(window,
                             text=f'{text[0]}\n{text[1]}'.upper(),
                             bd=0,
                             background=back,
                             foreground='white',
                             anchor=possible_pos[3 * i + j],
                             font=(font, 16),
                             command=lambda i=i, j=j: clock_app(possible_pos[3 * i + j]))
        main_bg.append(btn)
        text_color_buttons.append(btn)

        btn.place(x=550 + (100 * j), y=150 + (100 * i), width=100, height=100)


#main color entry
entry_main_color = entry_place()
entry_main_color.place(x=100, y=193, width=100, height=20)
btn_main_color = color_btn()
main_bg.append(btn_main_color)
text_color_buttons.append(btn_main_color)
btn_main_color.place(x=262, y=193, width=100, height=20)

#primary color entry
entry_primary_color = entry_place()
entry_primary_color.place(x=100, y=273, width=100, height=20)
btn_primary_color = color_btn()
main_bg.append(btn_primary_color)
text_color_buttons.append(btn_primary_color)
btn_primary_color.place(x=262, y=273, width=100, height=20)

app.mainloop()
