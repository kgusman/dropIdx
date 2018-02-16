# Constants are defined below
MINIMUM_DEGREE = 4


import queue


class BTree:
    # Class that represents a B-tree
    #
    # Attributes:
    #   min_degree  Minimum number of keys a node can contain
    #   root        Root node of this B-tree

    class Node:
        # Class that represents nodes within a B-tree
        #
        # Attributes:
        #   leaf        Boolean value that is True if this node is a leaf
        #   keys        Keys of items internal to this node
        #   pointers    Pointers to items (indexes of items in the list)
        #   children    Pointers to children nodes of this node

        def __init__(self, leaf=False):
            self.leaf = leaf
            self.keys = []
            self.pointers = []
            self.children = []

    def __init__(self):
        self.root = self.Node(True)
        self.min_degree = MINIMUM_DEGREE

    def split_child(self, x, i, y):
        # A fundamental operation used during insertion is the splitting
        # of a full node 'y' (having 2 * 'min_degree' - 1 keys) around
        # its median key 'y.keys[min_degree]' into two nodes having
        # 'min_degree' - 1 keys each.
        #
        # Arguments:
        #   x   A nonfull node
        #   i   An index of 'y' in children list of 'x'
        #   y   A full child of 'x'

        z = self.Node(y.leaf)

        x.keys.insert(i, y.keys[self.min_degree - 1])
        x.pointers.insert(i, y.pointers[self.min_degree - 1])
        x.children.insert(i + 1, z)

        z.keys = y.keys[self.min_degree:2 * self.min_degree - 1]
        z.pointers = y.pointers[self.min_degree:2 * self.min_degree - 1]
        y.keys = y.keys[0:self.min_degree - 1]
        y.pointers = y.pointers[0:self.min_degree - 1]

        if not y.leaf:
            z.children = y.children[self.min_degree:2 * self.min_degree]
            y.children = y.children[0:self.min_degree]

    def insert_nonfull(self, x, k, p):
        # The auxiliary recursive procedure 'insert_nonfull(self, x, k)'
        # inserts key 'k' into node 'x', which is assumed to be nonfull
        # when the procedure is called.
        #
        # Arguments:
        #   x   A nonfull node
        #   k   A key that is to be inserted into 'x'
        #   p   A pointer that is to be inserted into 'x'

        if x.leaf:
            if not x.keys or x.keys[-1] < k:
                x.keys.append(k)
                x.pointers.append(p)
            else:
                for i, key in enumerate(x.keys):
                    if key > k:
                        x.keys.insert(i, k)
                        x.pointers.insert(i, p)
                        break
        else:
            for i, key in enumerate(reversed(x.keys)):
                if k > key:
                    i = x.keys.index(key) + 1
                    y = x.children[i]

                    if self.is_node_full(y):
                        self.split_child(x, i, y)
                        key = x.keys[i]

                        if k > key:
                            i += 1
                            y = x.children[i]

                    self.insert_nonfull(y, k, p)
                    break

    def insert(self, item, p):
        # One of the main procedure that is used to insert
        # a key and its corresponding pointer value
        # into this tree.
        #
        # Arguments:
        #   item    An item that is to be inserted into this tree
        #   p       A corresponding pointer that is to be inserted into this tree

        r = self.root
        k = item.key

        if self.is_node_full(r):
            s = self.Node()
            s.children.append(r)

            self.root = s

            self.split_child(s, 0, r)
            self.insert_nonfull(s, k, p)
        else:
            self.insert_nonfull(r, k, p)

    def is_node_full(self, x):
        # The auxiliary function that helps to check
        # whether a node is full.
        #
        # Arguments:
        #   x   A node

        return len(x.keys) == (2 * self.min_degree - 1)

    def remove(self, item, x=None):
        # One of the main procedure that is used to remove a
        # key from this tree. Note that the tree might become
        # unbalanced after removal of a key from a lead node.
        #
        # Arguments:
        #   item   An item that is to be removed from this tree
        #   x      A node that contains the key of an item

        def remove_predecessor_key(x):
            if not x.leaf:
                remove_predecessor_key(x.children[-1])
            else:
                return x.keys.pop(), x.pointers.pop()

        def remove_successor_key(x):
            if not x.leaf:
                remove_successor_key(x.children[0])
            else:
                return x.keys.pop(0), x.pointers.pop(0)

        def merge(k, p, y, z):
            y.keys.append(k)
            y.pointers.append(p)

            y.keys = y.keys + z.keys
            y.pointers = y.pointers + z.pointers
            y.children = y.children + z.children

            return y

        def root(k, x):
            for i, key in enumerate(x.keys):
                if k < key:
                        return i, x.children[i]

            if k > x.keys[-1]:
                    return -1, x.children[-1]

        if x is None:
            x = self.root

        if self.root.children:
            self.root = self.root.children[0]

        if not x.leaf:
            if item.key in x.keys:
                t = x.keys.index(item.key)
                y = x.children[t]
                z = x.children[t + 1]

                if len(y.keys) >= self.min_degree:
                    new_k, new_p = remove_predecessor_key(y)

                    x.keys[t] = new_k
                    x.pointers[t] = new_p

                    return item
                elif len(z.keys) >= self.min_degree:
                    new_k, new_p = remove_successor_key(z)

                    x.keys[t] = new_k
                    x.pointers[t] = new_p

                    return item
                else:
                    y = merge(x.keys.pop(t), x.pointers.pop(t), y, z)
                    del x.children[t + 1]

                    return self.remove(item, y)
            else:
                i, r = root(item.key, x)

                y = x.children[i - 1] if i != 0 else None
                z = x.children[i + 1] if i != -1 else None

                if len(r.keys) == self.min_degree - 1:
                    if y is not None and len(y.keys) >= self.min_degree:
                        r.keys.insert(0, x.keys.pop(i - 1))
                        r.pointers.insert(0, x.pointers.pop(i - 1))
                        if not y.leaf:
                            r.children.insert(0, y.children.pop())

                        x.keys.insert(i - 1, y.keys.pop())
                        x.pointers.insert(i - 1, y.pointers.pop())
                    elif z is not None and len(z.keys) >= self.min_degree:
                        r.keys.append(x.keys.pop(i))
                        r.pointers.append(x.pointers.pop(i))
                        if not r.leaf:
                            r.children.append(z.children.pop(0))

                        x.keys.insert(i, z.keys.pop(0))
                        x.pointers.insert(i, z.pointers.pop(0))
                    else:
                        if i != 0:
                            r = merge(x.keys.pop(i - 1), x.pointers.pop(i), y, r)
                            del x.children[i]
                        else:
                            r = merge(x.keys.pop(i), x.pointers.pop(i), r, z)
                            del x.children[i + 1]

                return self.remove(item, r)
        else:
            if item.key in x.keys:
                t = x.keys.index(item.key)
                del x.keys[t]
                del x.pointers[t]

                return item
            else:
                return None

    def search(self, item, x=None):
        # One of the main procedure that is used to find a
        # pointer corresponding to the given item.
        #
        # Arguments:
        #   x      A node
        #   item   An item that is to be found in this tree

        if x is None:
            x = self.root

        i = 0
        for key in x.keys:
            if item.key < key:
                break
            elif item.key == key:
                return x.pointers[i]

            i += 1

        if x.leaf:
            return None
        else:
            return self.search(item, x.children[i])
