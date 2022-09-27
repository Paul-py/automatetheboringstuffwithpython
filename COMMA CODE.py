spam = ['apples', 'bananas', 'tofu', 'cats']

'''for i in spam:
    if i == spam(len(spam))
        print(i)
    else:
        i+=', '
        print(i, end='')

#print(spam[-1])


'''
'''def comma(items):
    for i in range(len(items) -2):
        print(items[i], end=',')
    print(items[-2] + ' and ' + items[-1])


comma(spam)'''

for i in spam:
    if i == spam[-2]:
        print(i + ' and ', end='')
    elif i == spam[0]:
        print(i)
    else:
        print(i + ',', end='')
