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
    def __init__(self):
        self.parent = None
        self.entities = []
        self.children = []

    def add_child(self, node):
        node.parent = self
        self.children.append(node)
        self.children.sort(key=lambda x: x.entities[0].key)

    def del_child(self, node):
        self.children.remove(node)

    def add_entity(self, entity):
        self.entities.append(entity)
        self.entities.sort(key=lambda x: x.key)

    def del_entity(self, entity):
        self.entities.remove(entity)

    def find(self, key):
        for entity in self.entities:
            if key == entity.key:
                return entity

    def delete(self, key):
        for index, entity in enumerate(self.entities):
            if key == entity.key:
                self.entities.remove(entity)
                return index
        return -1

    def is_leaf(self):
        return not self.children


class BTree:
    def __init__(self, degree=5):
        self.root = None
        self.min_children = degree
        self.max_children = degree * 2
        self.min_entities = degree - 1
        self.max_entities = degree * 2 - 1
        self.size = 0
        self.traversal = ""

    def insert(self, entity):
        if self.root:
            node = self.root
            # find a place to insert a node
            while 1:
                # Each node has entities no more than 'branch'
                # Notice that here we don't need to cater for the lower bound of entity number
                # since it will never generate a child until self is full
                # Similarly, the number of children is controlled by the entity number and no need to take care of it.
                if len(node.entities) == self.max_entities:
                    node = self.__split_node(node)
                if node.is_leaf():
                    for i, e in enumerate(node.entities):
                        if entity.key == e.key:
                            e.merge(entity)
                            return
                    node.add_entity(entity)
                    self.size += 1
                    return
                for i, e in enumerate(node.entities):
                    if entity.key < e.key:
                        # continue to find the right position to insert iteratively
                        node = node.children[i]
                        break
                    elif entity.key == e.key:
                        # if the inserted entity shares a key that already existed in the tree, merge the two
                        e.merge(entity)
                        return
                else:
                    # insert to the rightmost place, if entity's key is the largest
                    node = node.children[-1]
        else:
            # initialize the tree
            self.root = Node()
            self.root.add_entity(entity)

    def __get_node(self, key):
        # get the node by key, only used when deletion
        if not self.root:
            return None, 999
        node = self.root
        while not node.is_leaf():
            for i, e in enumerate(node.entities):
                if e.key > key:
                    node = node.children[i]
                    break
                elif e.key == key:
                    return node, i
            else:
                node = node.children[-1]
        for i, e in enumerate(node.entities):
            if e.key == key:
                return node, i
        return None, 999

    def __successor(self, node):
        while not node.is_leaf():
            node = node.children[0]
        return node.entities[0]

    def __predecessor(self, node):
        while not node.is_leaf():
            node = node.children[-1]
        if len(node.entities) == 0:
            a = 2
        return node.entities[-1]

    def search(self, start_key, end_key=None, node=None, result=None):
        # initialize parameters
        if node is None:
            node = self.root
        if end_key is None:
            end_key = start_key
        if result is None:
            result = []
        if end_key < node.entities[0].key and not node.is_leaf():
            result = self.search(start_key, end_key, node.children[0], result)
            return result
        if start_key > node.entities[-1].key and not node.is_leaf():
            result = self.search(start_key, end_key, node.children[-1], result)
            return result
        # Here are several situations:
        # 0. start_key < every entity.key, search leftmost child
        # 1. end_key > every entity.key, search rightmost child
        # 2. start_key < entity.key < end_key, we need to take the entity and search both adjacent children.
        # 3. start_key == entity.key or end_key == entity.key, take the entity.
        flag = False
        for index, entity in enumerate(node.entities):
            if start_key < entity.key < end_key:
                result.append(entity)
                if not node.is_leaf():
                    result = self.search(start_key, end_key, node.children[index], result)
                    flag = True
            elif entity.key > end_key and flag is True:
                result = self.search(start_key, end_key, node.children[index], result)
                flag = False
                return result
            elif end_key == entity.key:
                result.append(entity)
                if not node.is_leaf():
                    result = self.search(start_key, end_key, node.children[index], result)
                return result
            elif start_key == entity.key:
                result.append(entity)
                if index + 1 < len(node.entities):
                    flag = True
                else:
                    result = self.search(start_key, end_key, node.children[index + 1], result)
                    return result
            elif entity.key < start_key and index + 1 < len(node.entities) and node.entities[index + 1].key > end_key:
                if not node.is_leaf():
                    result = self.search(start_key, end_key, node.children[index + 1], result)
                return result
        if node.entities[-1].key < end_key:
            if not node.is_leaf():
                result = self.search(start_key, end_key, node.children[-1], result)
        # return in ascending order
        result.sort(key=lambda x: x.key)
        return result

    def __split_node(self, node):
        # split the node into two part, the middle be the parent
        mid = int(len(node.entities) / 2)
        right_node = Node()
        for entity in node.entities[mid + 1:]:
            right_node.add_entity(entity)
        for child in node.children[mid + 1:]:
            right_node.add_child(child)

        parent_entity = node.entities[mid]
        node.entities = node.entities[:mid]
        node.children = node.children[:mid + 1]

        parent = node.parent
        if parent:
            parent.add_entity(parent_entity)
            parent.add_child(right_node)
        else:
            self.root = Node()
            self.root.add_entity(parent_entity)
            self.root.add_child(node)
            self.root.add_child(right_node)
        return node.parent

    def preorder_traversal(self, node=None, level=0):
        if not node:
            node = self.root
            self.traversal = "level=0 child=0 /"

        for entity in node.entities:
            self.traversal += entity.__str__() + "/"

        if not node.is_leaf():
            for index, child in enumerate(node.children):
                self.traversal += "\nlevel=" + (level + 1).__str__() + " child=" + index.__str__() + " /"
                self.preorder_traversal(child, level + 1)

    def delete(self, key, node=None):
        node = node if node else self.root
        is_in = False
        i = -1
        for i, e in enumerate(node.entities):
            if e.key == key:
                # in the node
                is_in = True
                break
            elif e.key > key:
                # not in the node
                is_in = False
                break
        else:
            i += 1
        if is_in:
            if node.is_leaf():
                node.delete(key)
                self.size -= 1
            else:
                self.__del_in(node, i, key)
        else:
            if node.is_leaf():
                return
            else:
                self.__del_not_in(node, i, key)

    def __del_in(self, node, i, key):
        left = node.children[i]
        right = node.children[i + 1]
        if len(left.entities) > self.min_entities:
            pred_entity = self.__predecessor(left)
            node.del_entity(node.entities[i])
            node.add_entity(pred_entity)
            self.delete(pred_entity.key, left)
        elif len(right.entities) > self.min_entities:
            succ_entity = self.__successor(right)
            node.del_entity(node.entities[i])
            node.add_entity(succ_entity)
            self.delete(succ_entity.key, right)
        else:
            # node = self.__merge(node, i, left, right)
            left.add_entity(node.entities[i])
            for e in right.entities:
                left.add_entity(e)
            for c in right.children:
                left.add_child(c)
            node.del_entity(node.entities[i])
            node.del_child(right)
            self.delete(key, left)

    def __del_not_in(self, node, i, key):
        # deal with specific case that node has only one entity
        if len(node.entities) == 1:
            left = node.children[0]
            right = node.children[1]
            if left and right and len(left.entities) == len(right.entities) == self.min_entities:
                # node = self.__merge_root(node, left, right)
                for e in left.entities + right.entities:
                    node.add_entity(e)
                for c in left.children + right.children:
                    node.add_child(c)
                node.del_child(left)
                node.del_child(right)
                self.delete(key, node)
                return
        # if in the child node
        child = node.children[i]
        if len(child.entities) == self.min_entities:
            left = node.children[i - 1] if i - 1 > -1 else None
            right = node.children[i + 1] if i + 1 < len(node.children) else None
            if left and len(left.entities) > self.min_entities:
                child.add_entity(node.entities[i - 1])
                node.del_entity(node.entities[i - 1])
                node.add_entity(left.entities[-1])
                if not child.is_leaf():
                    child.add_child(left.children[-1])
                    left.del_child(left.children[-1])
                left.del_entity(left.entities[-1])
            elif right and len(right.entities) > self.min_entities:
                child.add_entity(node.entities[i])
                node.del_entity(node.entities[i])
                node.add_entity(right.entities[0])
                if not child.is_leaf():
                    child.add_child(right.children[0])
                    right.del_child(right.children[0])
                right.del_entity(right.entities[0])
            elif right and len(right.entities) == self.min_entities:
                child.add_entity(node.entities[i])
                for e in right.entities:
                    child.add_entity(e)
                if not child.is_leaf():
                    for c in right.children:
                        child.add_child(c)
                node.del_child(right)
                node.del_entity(node.entities[i])
            elif left and len(left.entities) == self.min_entities:
                child.add_entity(node.entities[i - 1])
                for e in left.entities:
                    child.add_entity(e)
                if not child.is_leaf():
                    for c in left.children:
                        child.add_child(c)
                node.del_child(left)
                node.del_entity(node.entities[i - 1])
        self.delete(key, child)

    def __str__(self):
        self.preorder_traversal()
        try:
            file_handler = open('./batch/preorder.txt', 'w', -1, "utf-8")
            file_handler.write(self.traversal)
        except FileNotFoundError:
            return -1
        return 1