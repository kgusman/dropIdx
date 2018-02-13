# Constants are defined below
MINIMUM_DEGREE = 100


class BtreeIndex:
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
        # A fundamental operation used during insertion is the splitting of a full node 'y'
        # (having 2 * 'min_degree' - 1 keys) around its median key 'y.keys[min_degree]' into
        # two nodes having 'min_degree' - 1 keys each.
        #
        # Arguments:
        #   x   A nonfull node
        #   i   An index of 'y' in children list of 'x'
        #   y   A full child of 'x'

        z = self.Node(y.leaf)

        z.keys = y.keys[self.min_degree:2 * self.min_degree - 1]
        z.pointers = y.pointers[self.min_degree:2 * self.min_degree - 1]
        y.keys = y.keys[0:self.min_degree - 1]
        y.pointers = y.pointers[0:self.min_degree - 1]

        if not y.leaf:
            z.children = y.children[self.min_degree:2 * self.min_degree]
            y.children = y.children[0:self.min_degree - 1]

        x.keys.insert(i, y.keys[self.min_degree - 1])
        x.pointers.insert(i, y.pointers[self.min_degree - 1])
        x.children.insert(i + 1, z)

    def insert_nonfull(self, x, k, p):
        # The auxiliary recursive procedure 'insert_nonfull(self, x, k)' inserts key 'k' into node 'x',
        # which is assumed to be nonfull when the procedure is called.
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
                    i = len(x.keys) - i
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
        # One of the main procedure that is used to insert a key and its corresponding pointer value
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

            self.split_child(s, 0, r)
            self.insert_nonfull(s, k.key, p)
        else:
            self.insert_nonfull(r, k, p)

    def is_node_full(self, x):
        # The auxiliary function that helps to check whether a node is full
        #
        # Arguments:
        #   x   A node

        return len(x.children) == (2 * self.min_degree - 1)

    def search(self, item, x=None):
        # One of the main procedure that is used to find a pointer corresponding to the given item.
        #
        # Arguments:
        #   x      A node
        #   item   An item that is to be found in this tree

        if not x:
            x = self.root

        for i, key in enumerate(x.keys):
            if key > item.key:
                return self.search(x.children[i], item)
            elif key == item.key:
                return x.pointers[i]

        if x.leaf:
            return None
