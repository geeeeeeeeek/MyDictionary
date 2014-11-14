__author__ = 'Tong'


class Entity:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    def merge(self, entity):
        if entity.key != self.key:
            return -1
        if self.value != entity.value:
            self.value += "; " + entity.value

    def __str__(self):
        return self.key.__str__() + " : " + self.value.__str__()


class Node:
    def __init__(self, entity, color='RED'):
        self.color = color
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.entity = entity

    def is_leaf(self):
        return self.left_child == Node(None, 'BLACK') or self.right_child == Node(None, 'BLACK')

    def is_root(self):
        return not self.parent or self.parent is NIL

    def merge(self, node):
        self.entity.merge(node.entity)


NIL = Node(None, 'BLACK')


class RBTree:
    def __init__(self):
        self.size = 0
        self.root = NIL
        self.traversal = ""

    def insert(self, entity):
        z = Node(entity)
        y = NIL
        x = self.root
        while x is not NIL:
            y = x
            if z.entity.key < x.entity.key:
                x = x.left_child
            elif z.entity.key > x.entity.key:
                x = x.right_child
            else:
                x.merge(z)
                return
        z.parent = y
        if y is NIL:
            self.root = z
            self.root.parent = NIL
        elif z.entity.key < y.entity.key:
            y.left_child = z
        elif z.entity.key > y.entity.key:
            y.right_child = z
        else:
            y.merge(z)
            return
        z.left_child = NIL
        z.right_child = NIL
        self.__insert_fixup(z)
        self.size += 1

    def __successor(self, node):
        x = node
        if x.right_child is not NIL:
            z = x.right_child
            while z.left_child is not NIL:
                z = z.left_child
            return z
        y = x.parent
        while y is not NIL and x == y.right_child:
            x = y
            y = x.parent
        return y

    def __get_node(self, key, node=None):
        if not node:
            node = self.root
        if node.entity.key == key:
            return node
        if node.left_child is not NIL:
            result = self.__get_node(key, node.left_child)
            if result is not None:
                return result
        if node.right_child is not NIL:
            result = self.__get_node(key, node.right_child)
            if result is not None:
                return result

    def delete(self, key):
        if key == "r":
            a = 1
        z = self.__get_node(key)
        if not z:
            return -1
        if z.left_child is NIL or z.right_child is NIL:
            y = z
        else:
            y = self.__successor(z)
        if y.left_child is not NIL:
            x = y.left_child
        else:
            x = y.right_child
        x.parent = y.parent
        if y.parent is NIL:
            self.root = x
        elif y == y.parent.left_child:
            y.parent.left_child = x
        else:
            y.parent.right_child = x
        if y != z:
            z.entity = y.entity
        if y.color == 'BLACK':
            self.__delete_fixup(x, z)

    def __delete_fixup(self, x, z):
        while x is not self.root and x.color == 'BLACK':
            if x == x.parent.left_child:
                w = x.parent.right_child
                if w is NIL:
                    break
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.__rotate(x.parent, 'LEFT')
                    w = z.parent.right_child
                elif w.left_child.color == 'BLACK' and w.right_child.color == 'BLACK':
                    w.color = 'RED'
                    x = x.parent
                elif w.right_child.color == 'BLACK':
                    w.left_child.color = 'BLACK'
                    w.color = 'RED'
                    self.__rotate(w, 'RIGHT')
                    w = x.parent.right_child
                else:
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.right_child.color = 'BLACK'
                    self.__rotate(x.parent, 'LEFT')
                    x = self.root
            elif x == x.parent.right_child:
                w = x.parent.left_child
                if w is NIL:
                    break
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.__rotate(x.parent, 'RIGHT')
                    w = z.parent.left_child
                elif w.right_child.color == 'BLACK' and w.left_child.color == 'BLACK':
                    w.color = 'RED'
                    x = x.parent
                elif w.left_child.color == 'BLACK':
                    w.right_child.color = 'BLACK'
                    w.color = 'RED'
                    self.__rotate(w, 'LEFT')
                    w = x.parent.left_child
                else:
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.left_child.color = 'BLACK'
                    self.__rotate(x.parent, 'RIGHT')
                    x = self.root
        x.color = 'BLACK'

    def search(self, start_key, end_key=None, node=None, result=None):
        if end_key is None:
            end_key = start_key
        if node is None:
            node = self.root
        if node is NIL:
            return result
        if start_key <= node.entity.key <= end_key:
            if result:
                result.append(node.entity)
            else:
                result = [node.entity]
        if node.entity.key > start_key:
            result = self.search(start_key, end_key, node.left_child, result)
        if node.entity.key < end_key:
            result = self.search(start_key, end_key, node.right_child, result)
        if result:
            result.sort(key=lambda x: x.key)
        return result

    def preorder_traversal(self, node=None, child=0, level=0):
        if not node:
            node = self.root
            self.traversal = ""
        if node is NIL:
            self.traversal += "level=" + level.__str__() + " child=" + child.__str__() + " null\n"
        else:
            self.traversal += "level=" + level.__str__() + " child=" + child.__str__() + " " \
                              + node.entity.__str__() + "(" + node.color.__str__() + ")\n"
        if node is not NIL:
            level += 1
            self.preorder_traversal(node.left_child, 0, level)
            self.preorder_traversal(node.right_child, 1, level)

    def __rotate(self, node, direction):
        if direction is 'LEFT':
            x = node
            y = x.right_child
            x.right_child = y.left_child
            y.left_child.parent = x
            y.parent = x.parent
            if x.is_root():
                self.root = y
            elif x == x.parent.left_child:
                x.parent.left_child = y
            else:
                x.parent.right_child = y
            y.left_child = x
            x.parent = y
        if direction is 'RIGHT':
            x = node
            y = x.left_child
            x.left_child = y.right_child
            y.right_child.parent = x
            y.parent = x.parent
            if x.is_root():
                self.root = y
            elif x == x.parent.right_child:
                x.parent.right_child = y
            else:
                x.parent.left_child = y
            y.right_child = x
            x.parent = y

    def __insert_fixup(self, node):
        z = node
        while z.parent.color == 'RED':
            if z.parent is z.parent.parent.left_child:
                y = z.parent.parent.right_child
                if y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                elif z is z.parent.right_child:
                    z = z.parent
                    self.__rotate(z, 'LEFT')
                else:
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.__rotate(z.parent.parent, 'RIGHT')
            elif z.parent is z.parent.parent.right_child:
                y = z.parent.parent.left_child
                if y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                elif z is z.parent.left_child:
                    z = z.parent
                    self.__rotate(z, 'RIGHT')
                else:
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.__rotate(z.parent.parent, 'LEFT')
        self.root.color = 'BLACK'

    def __str__(self):
        self.preorder_traversal()
        try:
            file_handler = open('./batch/preorder.txt', 'w', -1, "utf-8")
            file_handler.write(self.traversal)
        except FileNotFoundError:
            return -1
        return 1