import knapsack
import traceback
import re
from dynamic_programming import DynamicProgramTable

def test_knapsack(testcase):
    outputString = ""
    testname, items, W, included_items, total_value = testcase

    # Set up the dynamic programming table.
    D = DynamicProgramTable(len(items) + 1, W + 1, knapsack.cell_ordering(items, W), knapsack.fill_cell)

    try:
        D.fill(items=items, W=W)
    except:
        outputString += "Exception encountered when filling dynamic-programming table:\n"
        outputString += traceback.format_exc()
        return outputString

    try:
        (res_included_items, res_total_value) = knapsack.knapsack_from_table(items,W,D)
    except:
        outputString += "Exception encountered when running diff_from_table:\n"
        outputString += traceback.format_exc()
        return outputString

    for x in included_items:
        if not x in res_included_items:
            outputString += "Output list should have included %s but did not\n"%str(x)

    for x in res_included_items:
        if not x in included_items:
            outputString += "Output list included %s but should not have\n"%str(x)

    if res_total_value != total_value:
        outputString += "Total value output was %s but should've been %s\n"%(res_total_value,total_value)

    return outputString

def stringToList(input):
    output = []
    tuples = input.strip("[()]").split("), (")
    if tuples == ['']:
        return []
    for i in tuples:
        vw = i.split(", ")
        output.append((int(vw[0]), int(vw[1])))
    return output

with open("knapsack_tests.txt", 'r') as testfile:
    L = testfile.readlines()
    num_tests_run = 0
    num_failed_tests = 0
    for l in L:
        (testname, items, W, included_items, total_value)  = l.strip().split(";")
        testcase = (testname, stringToList(items), int(W), stringToList(included_items), int(total_value))
        test_result = test_knapsack(testcase)
        num_tests_run += 1
        if len(test_result) > 0:
            print("Failed test with name %s" % testname)
            print(test_result)
            num_failed_tests += 1

print("Ran %d tests"%num_tests_run)
print("Failed %d tests"%num_failed_tests)
