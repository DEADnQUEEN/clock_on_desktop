import datetime
import time
import tkinter
import os


back = '#333333'
fg = '#ffffff'
possible_pos = ['nw', 'n', 'ne', 'w', 'center', 'e', 'sw', 's', 'se']


def clock_app(pos: str in possible_pos):
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


try:
    from screeninfo import get_monitors
except ImportError:
    os.system('pip install screeninfo')
    from screeninfo import get_monitors

for i in get_monitors():
    if i.is_primary:
        res_x = i.width
        res_y = i.height
        break
else:
    raise Exception('monitors')

app = tkinter.Tk()
app.overrideredirect(True)
app.resizable(width=False, height=False)

btn_size = 200
window_size = btn_size * 3


width = int(round((res_x - window_size) / 2))
height = int(round((res_y - window_size) / 2))


app.geometry(f'{window_size}x{window_size}+{width}+{height}')

for i in range(int(len(possible_pos) ** (1 / 2))):
    for j in range(int(len(possible_pos) ** (1 / 2))):
        print(f'btn{i}{j} - {possible_pos[i * (int(len(possible_pos) ** (1 / 2))) + j]}')
        poss = f'{possible_pos[i * (int(len(possible_pos) ** (1 / 2))) + j]}'
        btn = tkinter.Button(app,
                             borderwidth=0,
                             text='HERE',
                             relief='flat',
                             anchor=poss,
                             background=back,
                             fg=fg,
                             font=('Arial Black', round(btn_size * 0.15)),
                             command=lambda poss=poss: clock_app(poss)
                             )
        btn.place(y=i * btn_size, x=j * btn_size, height=btn_size, width=btn_size)

app.mainloop()
