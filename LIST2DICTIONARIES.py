

def addToInventory(inventory, addedItems):
    for i in dragonLoot:
        if i not in inv:
            inv[i] = 1
        else:
            inv[i] += 1

    return inv

def displayInventory(inv):
    print("Inventory:")
    item_total = 0
    for k, v in inv.items():
        print(v, k)
        item_total += v
    print("Total number of items: " + str(item_total))
    #for k in inv.values:
     #   p += k

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)

displayInventory(inv)








'''The previous program (with your displayInventory() function from the
previous project) would output the following:
Inventory:
45 gold coin
1 rope
1 ruby
1 dagger
Total number of items: 48'''