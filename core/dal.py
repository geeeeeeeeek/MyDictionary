import random

__author__ = 'Tong'
from core import B_Tree, RB_Tree


def init():
    global bt, rbt, gs
    bt = B_Tree.BTree()
    rbt = RB_Tree.RBTree()
    gs = "BTree"
    __file_input_util("INSERT", './batch/1_initial.txt')
    gs = "RBTree"
    __file_input_util("INSERT", './batch/1_initial.txt')


def __file_input_util(type, path):
    try:
        file_handler = open(path, 'a+', -1, "utf-8")
        file_handler.seek(0)
        # discard the first line
        file_handler.readline()
        lines = file_handler.readlines()
        file_handler.close()
        if type == "INSERT":
            for i in range(int(len(lines) / 2)):
                key = lines[2 * i][:-1]
                value = lines[2 * i + 1][:-1]
                insert(key, value)
        if type == "DELETE":
            for line in lines:
                key = line[:-1]
                rbt.delete(key)
                delete(key)
    except FileNotFoundError:
        return -1
    return 1


def __file_output_util(string):
    try:
        file_handler = open('./batch/1_initial.txt', 'a+', -1, "utf-8")
        file_handler.write(string)
    except FileNotFoundError:
        return -1
    return 1


def insert(key, value):
    if gs == "BTree":
        bt.insert(B_Tree.Entity(key, value))
    else:
        rbt.insert(RB_Tree.Entity(key, value))


def delete(key):
    if gs == "BTree":
        bt.delete(key)
    else:
        rbt.delete(key)


def search(start_key, end_key):
    if gs == "BTree":
        result = bt.search(start_key, end_key)
    else:
        result = rbt.search(start_key, end_key)
    string = ""
    if result:
        for each in result:
            string += each.__str__() + "\n"
        return string
    else:
        return None


def update_voc_test():
    start_key = 'a'
    end_key = random.choice('qwertyuiopsdfghjklzxcvbnm')
    if gs == "BTree":
        result = bt.search(start_key, end_key)
    else:
        result = rbt.search(start_key, end_key)
    word = result[random.randint(0, len(result))]
    options = []
    while len(options) < 3:
        entity = result[random.randint(0, len(result))]
        if entity.key != word.key:
            options.append(entity.value)
        else:
            continue
    options.insert(random.randint(0, 3), word.value)
    return word.key, word.value, options[0], options[1], options[2], options[3]