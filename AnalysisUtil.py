import time

__author__ = 'Tong'

from core.B_Tree import BTree, Entity
from core.RB_Tree import RBTree, Entity


def btt():
    bt = BTree()
    # ##### 1. insert into trees the data in the file 1_initial.txt ######
    file_handler = open('batch/1_initial.txt', 'a+', -1, "utf-8")
    file_handler.seek(0)
    # discard the first line
    file_handler.readline()
    lines = file_handler.readlines()
    file_handler.close()
    entities_to_init = []
    for i in range(int(len(lines) / 2)):
        key = lines[2 * i][:-1]
        value = lines[2 * i + 1][:-1]
        entities_to_init.append(Entity(key, value))

    file_handler = open('batch/2_delete.txt', 'a+', -1, "utf-8")
    file_handler.seek(0)
    # discard the first line
    file_handler.readline()
    lines = file_handler.readlines()
    file_handler.close()
    entities_to_delete = []
    for l in lines:
        entities_to_delete.append(l[:-1])

    file_handler = open('batch/3_insert.txt', 'a+', -1, "utf-8")
    file_handler.seek(0)
    # discard the first line
    file_handler.readline()
    lines = file_handler.readlines()
    file_handler.close()
    entities_to_insert = []
    for i in range(int(len(lines) / 2)):
        key = lines[2 * i][:-1]
        value = lines[2 * i + 1][:-1]
        entities_to_insert.append(Entity(key, value))

    file_handler = open('batch/4_search.txt', 'a+', -1, "utf-8")
    file_handler.seek(0)
    # discard the first line
    file_handler.readline()
    lines = file_handler.readlines()
    file_handler.close()
    entities_to_search = []
    for l in lines:
        entities_to_search.append(l[:-1])

    time1 = []
    for i, e in enumerate(entities_to_init):
        if i % 200 == 0:
            time1.append(time.clock())
        bt.insert(e)

    time2 = []
    for i, e in enumerate(entities_to_delete):
        if i % 200 == 0:
            time2.append(time.clock())
        bt.delete(e)

    time3 = []
    for i, e in enumerate(entities_to_insert):
        if i % 200 == 0:
            time3.append(time.clock())
        bt.insert(e)

    time4 = []
    for i, e in enumerate(entities_to_search):
        time4.append(time.clock())
        bt.search(e)

    time5 = []
    time5.append(time.clock())
    bt.search("b", "h")
    time5.append(time.clock())

    return time1, time2, time3, time4, time5


def rbtt():
    rbt = RBTree()
    # ##### 1. insert into trees the data in the file 1_initial.txt ######
    file_handler = open('batch/1_initial.txt', 'a+', -1, "utf-8")
    file_handler.seek(0)
    # discard the first line
    file_handler.readline()
    lines = file_handler.readlines()
    file_handler.close()
    entities_to_init = []
    for i in range(int(len(lines) / 2)):
        key = lines[2 * i][:-1]
        value = lines[2 * i + 1][:-1]
        entities_to_init.append(Entity(key, value))

    file_handler = open('batch/2_delete.txt', 'a+', -1, "utf-8")
    file_handler.seek(0)
    # discard the first line
    file_handler.readline()
    lines = file_handler.readlines()
    file_handler.close()
    entities_to_delete = []
    for l in lines:
        entities_to_delete.append(l[:-1])

    file_handler = open('batch/3_insert.txt', 'a+', -1, "utf-8")
    file_handler.seek(0)
    # discard the first line
    file_handler.readline()
    lines = file_handler.readlines()
    file_handler.close()
    entities_to_insert = []
    for i in range(int(len(lines) / 2)):
        key = lines[2 * i][:-1]
        value = lines[2 * i + 1][:-1]
        entities_to_insert.append(Entity(key, value))

    file_handler = open('batch/4_search.txt', 'a+', -1, "utf-8")
    file_handler.seek(0)
    # discard the first line
    file_handler.readline()
    lines = file_handler.readlines()
    file_handler.close()
    entities_to_search = []
    for l in lines:
        entities_to_search.append(l[:-1])

    time1 = []
    for i, e in enumerate(entities_to_init):
        if i % 200 == 0:
            time1.append(time.clock())
        rbt.insert(e)

    time2 = []
    for i, e in enumerate(entities_to_delete):
        if i % 200 == 0:
            time2.append(time.clock())
        rbt.delete(e)

    time3 = []
    for i, e in enumerate(entities_to_insert):
        if i % 200 == 0:
            time3.append(time.clock())
        rbt.insert(e)

    time4 = []
    for i, e in enumerate(entities_to_search):
        time4.append(time.clock())
        rbt.search(e)

    time5 = []
    time5.append(time.clock())
    rbt.search("b", "h")
    time5.append(time.clock())

    return time1, time2, time3, time4, time5


def analysis():
    time1, time2, time3, time4, time5 = btt()
    print(time1)
    print(time2)
    print(time3)
    print(time4)
    print(time5)
    print()
    time1, time2, time3, time4, time5 = rbtt()
    print(time1)
    print(time2)
    print(time3)
    print(time4)
    print(time5)

analysis()