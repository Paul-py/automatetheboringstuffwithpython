tableData = [['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']]


def tableprinter(table):
    #create a new list of 3 '0' values: one for each list in tableData
    colWidths = [0] * len(table)
    #search for the longest string in each list in tableData
    # and put the number of characters in the new list
    for y in range(len(table)):
        for x in table[y]:
            if colWidths[y] < len(x):
                colWidths[y] = len(x)

    for x in range(len(table[0])):
        for y in range(len(table)):
            print(table[y][x].rjust(colWidths[y]), end=' ')
        print()
        x += 1

tableprinter(tableData)