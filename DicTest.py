from tkinter.simpledialog import SimpleDialog
import DicMain

__author__ = 'Tong'

from tkinter import *
from core import dal


def init():
    global window_test, word, answer, option_a, option_b, option_c, option_d
    window_test = Tk()

    word = StringVar()
    answer = StringVar()
    option_a = StringVar()
    option_b = StringVar()
    option_c = StringVar()
    option_d = StringVar()

    window_test.wm_minsize(width=430, height=240)
    window_test.title("Vocabulary Test")
    lbl_word = Label(window_test, textvariable=word, width=40, height=1,
                     font=("Microsoft YaHei", 10))
    lbl_word.place(x=10, y=5)
    btn_a = Button(window_test, command=do_a, textvariable=option_a, width=50, height=1,
                   font=("Microsoft YaHei", 10))
    btn_a.place(x=10, y=35)
    btn_b = Button(window_test, command=do_b, textvariable=option_b, width=50, height=1,
                   font=("Microsoft YaHei", 10))
    btn_b.place(x=10, y=70)
    btn_c = Button(window_test, command=do_c, textvariable=option_c, width=50, height=1,
                   font=("Microsoft YaHei", 10))
    btn_c.place(x=10, y=105)
    btn_d = Button(window_test, command=do_d, textvariable=option_d, width=50, height=1,
                   font=("Microsoft YaHei", 10))
    btn_d.place(x=10, y=140)
    btn_back = Button(window_test, command=do_main, text="Back", width=50, height=1,
                      font=("Microsoft YaHei", 10))
    btn_back.place(x=10, y=180)
    callback = dal.update_voc_test()
    word.set(callback[0])
    answer.set(callback[1])
    option_a.set(callback[2])
    option_b.set(callback[3])
    option_c.set(callback[4])
    option_d.set(callback[5])
    window_test.mainloop()


def do_a():
    if answer.get() == option_a.get():
        callback = dal.update_voc_test()
        word.set(callback[0])
        answer.set(callback[1])
        option_a.set(callback[2])
        option_b.set(callback[3])
        option_c.set(callback[4])
        option_d.set(callback[5])
        window_test.mainloop()
        SimpleDialog(window_test, text='Bingo',
                     buttons=['Okay']).go()
    else:
        SimpleDialog(window_test, text='Bad luck',
                     buttons=['Okay']).go()


def do_b():
    if answer.get() == option_b.get():
        callback = dal.update_voc_test()
        word.set(callback[0])
        answer.set(callback[1])
        option_a.set(callback[2])
        option_b.set(callback[3])
        option_c.set(callback[4])
        option_d.set(callback[5])
        window_test.mainloop()
        SimpleDialog(window_test, text='Bingo',
                     buttons=['Okay']).go()
    else:
        SimpleDialog(window_test, text='Bad luck',
                     buttons=['Okay']).go()


def do_c():
    if answer.get() == option_c.get():
        callback = dal.update_voc_test()
        word.set(callback[0])
        answer.set(callback[1])
        option_a.set(callback[2])
        option_b.set(callback[3])
        option_c.set(callback[4])
        option_d.set(callback[5])
        window_test.mainloop()
        SimpleDialog(window_test, text='Bingo',
                     buttons=['Okay']).go()
    else:
        SimpleDialog(window_test, text='Bad luck',
                     buttons=['Okay']).go()


def do_d():
    if answer.get() == option_d.get():
        callback = dal.update_voc_test()
        word.set(callback[0])
        answer.set(callback[1])
        option_a.set(callback[2])
        option_b.set(callback[3])
        option_c.set(callback[4])
        option_d.set(callback[5])
        window_test.mainloop()
        SimpleDialog(window_test, text='Bingo',
                     buttons=['Okay']).go()
    else:
        SimpleDialog(window_test, text='Bad luck',
                     buttons=['Okay']).go()


def do_main():
    window_test.destroy()
    DicMain.init()
