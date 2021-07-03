# TODO: Hongyi Nie, hn327

# DO NOT CHANGE THIS CLASS
class RespaceTableCell:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.validate()

    # This function allows Python to print a representation of a RespaceTableCell
    def __repr__(self):
        return "(%s,%s)"%(str(self.value), str(self.index))

    # Ensure everything stored is the right type and size
    def validate(self):
        assert(type(self.value) == bool), "Values in the respacing table should be booleans."
        assert(self.index == None or type(self.index) == int), "Indices in the respacing table should be None or int"

# Inputs: the dynamic programming table, indices i, j into the dynamic programming table, the string being respaced, and an "is_word" function.
# Returns a RespaceTableCell to put at position (i,j)
def fill_cell(T, i, j, string, is_word):
    #TODO: YOUR CODE HERE
    #
    # if i == 0 and j == 0:
    #     return RespaceTableCell(True, i)
    if i == j:
        if i == 0:
            return RespaceTableCell(True, i)
        else:
            for a in range(0,i):
                if T.get(i,a).value == True:
                    return RespaceTableCell(True, i)
            return RespaceTableCell(False, None)
    sub_string = string[j:i]

    if is_word(sub_string) == True and T.get(j,j).value:
        return RespaceTableCell(True, j)
    else:
        return RespaceTableCell(False, None)

# Inputs: N, the size of the list being respaced
# Outputs: a list of (i,j) tuples indicating the order in which the table should be filled.
def cell_ordering(N):
    #TODO: YOUR CODE HERE
    l = []
    for i in range(N+1):
        for j in range(0,i+1):
            l.append((i,j))
    return l
# Input: a filled dynamic programming table.
# (See instructions.pdf for more on the dynamic programming skeleton)
# Return the respaced string, or None if there is no respacing.
def respace_from_table(s, table):
    #TODO: YOUR CODE HERE
    if table._table[len(s)][len(s)].value == False:
        return None
    else:
        i = len(s)
        word = ""
        while i > 0:
            l = []
            for j in range(len(s)+1):
                if table._table[i][j] != None and table._table[i][j].value:
                    l.append(table._table[i][j].index)
            word = s[l[0]:l[1]] + " " + word
            i = l[0]

        return word[:-1]

if __name__ == "__main__":
    # Example usage.
    # from dynamic_programming import DynamicProgramTable
    # s = "itwasthebestoftimes"
    # wordlist = ["of", "it", "the", "best", "times", "was"]
    # D = DynamicProgramTable(len(s) + 1, len(s) + 1, cell_ordering(len(s)), fill_cell)
    # D.fill(string=s, is_word=lambda w:w in wordlist)
    # print(respace_from_table(s, D))
    from dynamic_programming import DynamicProgramTable
    s = "proudsellsailsellproud"
    wordlist = ["suse","isle","sell","wars","proud","flood","sail","mar","depot","pda"]
    D = DynamicProgramTable(len(s) + 1, len(s) + 1, cell_ordering(len(s)), fill_cell)
    D.fill(string=s, is_word=lambda w:w in wordlist)
    print(respace_from_table(s, D))
    # generated_positive_0;suse,isle,sell,wars,proud,flood,sail,mar,depot,pda;proudsellsailsellproud;proud sell sail sell proud;
