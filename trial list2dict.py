inv = {'gold coin': 42, 'rope': 1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

for i in dragonLoot:
    if i not in inv:
        inv[i] = 1
    else:
        inv[i] += 1

print(inv)