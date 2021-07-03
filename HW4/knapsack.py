# TODO: Your name, Cornell NetID
# Hongyi Nie, hn327
import dynamic_programming

# DO NOT CHANGE THIS CLASS
class KnapsackCell:
    def __init__(self, include, value):
        self.include = include
        self.value = value
        self.validate()

    # Helper function so Python can print out objects of this type.
    def __repr__(self):
        return "(%d,%s)"%(self.include, self.value)

    # Ensure everything stored is the right type and size
    def validate(self):
        assert(type(self.include) == bool), "include should be an integer"
        assert(type(self.value) == int), "value should be an integer"

# Input: a dynamic programming table, cell index i and j, and the inputs items and W.
def fill_cell(table, i, j, items, W):
    # TODO: YOUR CODE HERE (remove the line below)
    if i == 0:
        return KnapsackCell(False, 0)
    if j == 0:
        return KnapsackCell(False, 0)
    if items[i-1][1] > j:
        v = table.get(i-1,j).value
        return KnapsackCell(False, v)
    else:
        a = table.get(i-1,j).value
        b = table.get(i-1,j - items[i-1][1]).value + items[i-1][0]
        if a >= b:
            return KnapsackCell(False, a)
        else:
            return KnapsackCell(True, b)

def cell_ordering(items, W):
    # TODO: YOUR CODE HERE (remove the line below)
    l = []
    for i in range(len(items)+1):
        for j in range(W+1):
            l.append((i,j))
    return l


# Returns a size-2 tuple (included_items, total_value).
# included_items are all the items that are chosen for the knapsack (i.e. the items that maximize total value while respecting the weight constraint)
# total_value is the total value of the included items (i.e. the max value that the knapsack can store respecting the weight constraint)
def knapsack_from_table(items, W, table):
    # TODO: YOUR CODE HERE (you can remove the lines below)
    included_items = []
    total_value = 0
    i = len(items)
    j = W
    while not table.get(i,j).include and i > 0:
        i = i - 1
    if i > 0:
        total_value = table.get(i,j).value
    while i > 0 and j > 0:
        while not table.get(i,j).include and i > 0:
            i = i - 1
        if i == 0:
            break
        included_items.append(items[i-1])
        j = j - items[i-1][1]
        i = i - 1
    return (included_items, total_value)

# Example usage
if __name__ == "__main__":
    import dynamic_programming

    items = [(3, 2), (4, 3), (5, 4), (6, 5)]
    W = 5

    D = dynamic_programming.DynamicProgramTable(len(items) + 1, W + 1, cell_ordering(items, W), fill_cell)
    D.fill(items = items, W = W)
    (included_items, total_value) = knapsack_from_table(items, W, D)
    print(included_items)
    print("value was %d"%total_value)
