# TODO: Hongyi Nie, hn327

import dynamic_programming

# DO NOT CHANGE THIS CLASS
class DiffingCell:
    def __init__(self, s_char, t_char, cost):
        self.cost = cost
        self.s_char = s_char
        self.t_char = t_char
        self.validate()

    # Helper function so Python can print out objects of this type.
    def __repr__(self):
        return "(%d,%s,%s)"%(self.cost, self.s_char, self.t_char)

    # Ensure everything stored is the right type and size
    def validate(self):
        assert(type(self.cost) == int), "cost should be an integer"
        assert(type(self.s_char) == str), "s_char should be a string"
        assert(type(self.t_char) == str), "t_char should be a string"
        assert(len(self.s_char) == 1), "s_char should be length 1"
        assert(len(self.t_char) == 1), "t_char should be length 1"

# Input: a dynamic programming table,  cell index i and j, the input strings s and t, and a cost function cost.
# Should return a DiffingCell which we will place at (i,j) for you.
def fill_cell(table, i, j, s, t, cost):
    # TODO: YOUR CODE HERE

    #start point
    if i == 0 and j == 0:
        return DiffingCell('-','-',0)

    # x: right
    if i > 0 and j == 0:
        newcost = cost(s[i-1],'-') + table.get(i-1,0).cost
        return DiffingCell(s[i-1],'-',newcost)

    # y: down
    if i == 0 and j > 0:
        newcost = cost('-',t[j-1]) + table.get(0,j-1).cost
        return DiffingCell('-',t[j-1],newcost)

    else:
        cost_list = [table.get(i, j-1).cost + cost('-', t[j-1]), table.get(i-1, j-1).cost + cost(s[i-1], t[j-1]), table.get(i-1, j).cost + cost(s[i-1], '-')]
        # left
        if cost_list.index(min(cost_list)) == 0:
            return DiffingCell('-', t[j-1] , cost_list[0])
        # diagonal
        elif cost_list.index(min(cost_list)) == 1:
            return DiffingCell(s[i-1], t[j-1] , cost_list[1])
        # up
        elif cost_list.index(min(cost_list)) == 2:
            return DiffingCell(s[i-1], '-' , cost_list[2])



# Input: n and m, represents the sizes of s and t respectively.
# Should return a list of (i,j) tuples, in the order you would like fill_cell to be called
def cell_ordering(n,m):
    # TODO: YOUR CODE HERE
    return [(i, j) for i in range(n+1) for j in range(m+1)]

# Returns a size-3 tuple (cost, align_s, align_t).
# cost is an integer cost.
# align_s and align_t are strings of the same length demonstrating the alignment.
# See instructions.pdf for more information on align_s and align_t.
def diff_from_table(s, t, table):
    # TODO: YOUR CODE HERE
    i = len(s)
    j = len(t)

    s_cell = table.get(i,j).s_char
    t_cell = table.get(i,j).t_char
    align_s = table.get(i,j).s_char
    align_t = table.get(i,j).t_char
    cost_now = table.get(i,j).cost

    while i > 0 or j > 0:

        # right
        if (s_cell != '-' and t_cell == '-'):
            i -= 1

        # down
        elif (s_cell == '-' and t_cell != '-'):
            j -= 1

        # diagnonal
        elif (s_cell != '-' and t_cell != '-'):
            i -= 1
            j -= 1

        s_cell = table.get(i, j).s_char
        t_cell = table.get(i, j).t_char
        align_s += s_cell
        align_t += t_cell

    return (cost_now, align_s[-2::-1], align_t[-2::-1])

# Example usage
if __name__ == "__main__":
    # Example cost function from instructions.pdf
    def costfunc(s_char, t_char):
        if s_char == t_char: return 0
        if s_char == 'a':
            if t_char == 'b': return 5
            if t_char == 'c': return 3
            if t_char == '-': return 2
        if s_char == 'b':
            if t_char == 'a': return 1
            if t_char == 'c': return 4
            if t_char == '-': return 2
        if s_char == 'c':
            if t_char == 'a': return 5
            if t_char == 'b': return 5
            if t_char == '-': return 1
        if s_char == '-':
            if t_char == 'a': return 3
            if t_char == 'b': return 3
            if t_char == 'c': return 3

    import dynamic_programming
    s = "acb"
    t = "baa"
    D = dynamic_programming.DynamicProgramTable(len(s) + 1, len(t) + 1, cell_ordering(len(s), len(t)), fill_cell)
    D.fill(s = s, t = t, cost=costfunc)
    (cost, align_s, align_t) = diff_from_table(s,t, D)
    print(align_s)
    print(align_t)
    print("cost was %d"%cost)
