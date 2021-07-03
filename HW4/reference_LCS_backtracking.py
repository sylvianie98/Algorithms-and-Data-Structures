# The following file is a reference implementation of the LCS problem discussed during the lecture.
# The goal is to help you familiarize with the Dynamic Programming framework provided in this assignment.

import dynamic_programming

# DO NOT CHANGE THIS CLASS
class LCSCell:
    def __init__(self, i, j, length):
        self.i = i
        self.j = j
        self.length = length
        self.validate()

    # Helper function so Python can print out objects of this type.
    def __repr__(self):
        return "(%s,%d)"%(self.i, self.j, self.length)

    # Ensure everything stored is the right type and size
    def validate(self):
        assert(type(self.i) == int), "i should be an integer"
        assert(type(self.j) == int), "j should be an integer"
        assert(type(self.length) == int), "length should be an integer"

# Input: a dynamic programming table, cell index i and j, and the input strings s and t.
def fill_cell(table, i, j, s, t):
    cells = []
    if i==0 or j==0:
        return LCSCell(0, 0, 0)

    if s[i-1] == t[j-1]:
       return LCSCell(i-1, j-1, table.get(i-1, j-1).length + 1)

    if table.get(i-1, j).length > table.get(i, j-1).length:
      return LCSCell(i-1, j, table.get(i-1, j).length)
    else:
      return LCSCell(i, j-1, table.get(i, j-1).length)

def cell_ordering(n,m):
    L = []
    for i in range(n+1):
        for j in range(m+1):
            L.append((i,j))
    return L

# Returns the LCS from the table.
def diff_from_table(s, t, table):
    lcs = ""
    i = len(s)
    j = len(t)
    cell = table.get(i, j)
    while i != 0 and j != 0:
      current_len = cell.length
      next_len = table.get(cell.i, cell.j).length
      if (next_len < current_len):
        lcs = s[i-1] + lcs
      i = cell.i
      j = cell.j
      cell = table.get(i, j)
    return lcs

# Example usage
if __name__ == "__main__":
    import dynamic_programming
    s = "MANHATTAN"
    t = "ITHACA"
    D = dynamic_programming.DynamicProgramTable(len(s) + 1, len(t) + 1, cell_ordering(len(s), len(t)), fill_cell)
    D.fill(s = s, t = t)
    lcs = diff_from_table(s,t, D)
    print("lcs was %s"%lcs)
