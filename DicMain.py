from tkinter.simpledialog import SimpleDialog
import DicTest

__author__ = 'Tong'

from tkinter import *
from tkinter.filedialog import askopenfilename
from core import dal


def init():
    global window_main, txt_result, string_en, string_ch, query, gs

    window_main = Tk()
    window_main.wm_minsize(width=620, height=380)
    window_main.title("En-ch Dictionary")

    string_en = StringVar()
    string_ch = StringVar()
    query = StringVar()
    gs = StringVar()

    lbl_file_path = Label(window_main, width=20, height=2, text="Select a supported batch...",
                          font=("Microsoft YaHei", 10))
    lbl_file_path.place(x=0, y=0)

    btn_import_add = Button(window_main, command=do_import_add, text="Add", width=5, height=1,
                            font=("Microsoft YaHei", 10))
    btn_import_add.place(x=200, y=5)
    btn_import_del = Button(window_main, command=do_import_del, text="Del", width=5, height=1,
                            font=("Microsoft YaHei", 10))
    btn_import_del.place(x=260, y=5)

    lbl_en = Label(window_main, width=10, height=2, text="English", font=("Microsoft YaHei", 10))
    lbl_en.place(x=0, y=50)
    lbl_ch = Label(window_main, width=10, height=2, text="Chinese", font=("Microsoft YaHei", 10))
    lbl_ch.place(x=0, y=80)
    txt_en = Entry(window_main, width=26, textvariable=string_en, font=("Microsoft YaHei", 10))
    txt_en.place(x=100, y=60)
    txt_ch = Entry(window_main, width=26, textvariable=string_ch, font=("Microsoft YaHei", 10))
    txt_ch.place(x=100, y=90)
    btn_add = Button(window_main, text="Add", command=do_add, width=17, height=1, font=("Microsoft YaHei", 10))
    btn_add.place(x=18, y=125)
    btn_del = Button(window_main, text="Delete", command=do_delete, width=17, height=1, font=("Microsoft YaHei", 10))
    btn_del.place(x=168, y=125)

    rad_bt = Radiobutton(window_main, text="B Tree", width=5, height=1, variable=gs, value="BTree",
                         command=do_gs_switch,
                         font=("Microsoft YaHei", 10))
    rad_bt.place(x=350, y=10)
    rad_rbt = Radiobutton(window_main, text="Red-Black tree", width=10, height=1, variable=gs, value="RBTree",
                          command=do_gs_switch,
                          font=("Microsoft YaHei", 10))
    rad_rbt.place(x=480, y=10)
    gs.set("RBTree")

    lbl_search = Label(window_main, width=26, height=2, text="Type 'WORD' or 'A >> B' to search",
                       font=("Microsoft YaHei", 10))
    lbl_search.place(x=349, y=47)
    txt_search = Entry(window_main, width=24, textvariable=query, font=("Microsoft YaHei", 10))
    txt_search.place(x=350, y=90)
    btn_search = Button(window_main, command=do_search, text="Search", width=23, font=("Microsoft YaHei", 10))
    btn_search.place(x=350, y=125)
    btn_voc_test = Button(window_main, command=do_voc_test, text="Voc\nTest", width=5, height=3,
                          font=("Microsoft YaHei", 10))
    btn_voc_test.place(x=550, y=88)

    frame = Frame(window_main, width=800, height=100)
    frame.pack()
    frame.place(x=20, y=170)
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)
    txt_result = Text(frame, width=70, height=10, font=("Microsoft YaHei", 10), wrap=WORD,
                      yscrollcommand=scrollbar.set)
    txt_result.pack()
    scrollbar.config(command=txt_result.yview)

    window_main.mainloop()


def do_import_add():
    file = askopenfilename()
    flag = dal.__file_input_util("INSERT", file)
    if flag == 1:
        SimpleDialog(window_main,
                     text='Insertion succeeded:)',
                     buttons=['Got it']).go()
    else:
        SimpleDialog(window_main,
                     text='Insertion failed:(', buttons=['Got it']).go()


def do_import_del():
    file = askopenfilename()
    flag = dal.__file_input_util("DELETE", file)
    if flag == 1:
        SimpleDialog(window_main,
                     text='Deletion succeeded:)',
                     buttons=['Got it']).go()
    else:
        SimpleDialog(window_main,
                     text='Deletion failed:(',
                     buttons=['Got it']).go()


def do_add():
    if string_en.get() and string_ch.get():
        dal.insert(string_en.get(), string_ch.get())
        SimpleDialog(window_main,
                     text='Insertion succeeded:)',
                     buttons=['Got it']).go()
    else:
        SimpleDialog(window_main,
                     text='Insertion failed:(',
                     buttons=['Got it']).go()


def do_delete():
    if string_en.get():
        dal.delete(string_en.get())
        SimpleDialog(window_main,
                     text='Deletion succeeded:)',
                     buttons=['Got it']).go()
    else:
        SimpleDialog(window_main,
                     text='Deletion failed:(',
                     buttons=['Got it']).go()


def do_search():
    if query.get():
        flag = query.get().find(" >> ")
        if flag == -1:
            result = dal.search(query.get(), query.get())
        else:
            start_key = query.get()[:flag]
            end_key = query.get()[flag + 4:]
            result = dal.search(start_key, end_key)
        txt_result.delete(0.0, END)
        if result:
            txt_result.insert(END, result)
        else:
            txt_result.insert(END, "::Word '" + query.get() + "' is not in the dictionary!")
    else:
        SimpleDialog(window_main,
                     text="'Type 'WORD' or 'A >> B' to search'",
                     buttons=['Got it']).go()


def do_gs_switch():
    dal.gs = gs.get()


def do_voc_test():
    window_main.destroy()
    DicTest.init()