
def read():
    items = {}
    capacities =[]
    for line in open('/Users/nicholasmaisel/Documents/Programming/Algorithms/spice.txt','r'):

        line = line.rstrip().split(';')
        line = [x.strip() for x in line]
        if 'spice name' in line[0]:
            items[line[0].split('=')[1].strip()] = [float(line[1].split('=')[1].strip()),
                                                    int(line[2].split('=')[1].strip())]

        elif 'knapsack capacity' in line[0]:
            capacities.append(int(line[0].split('=')[1].strip()))

    return(items,capacities)


def knapsack(items, capacity):
    sack = {}
    for i in items:
        if capacity == 0:
            break
        price = i[1][0]
        qty = i[1][1]
        print(capacity,'is the pre processed capacity')
        if qty == 0: # if 0 qty left of item, remove it from list
            items.remove(i)
        if price <= capacity:
            qty_to_add = capacity // price
            if qty_to_add <= qty:
                i[1][1] -= qty_to_add
                sack[i[0]] = qty_to_add
                capacity -= qty_to_add * price
            else:
                i[1][1] -= qty
                sack[i[0]] = qty
                capacity -= qty_to_add * price

        else:
            frac_qty = capacity/price #add the item until full
            #Add frac_item of item to sack
            capacity -= frac_qty * price

        print('capacity:', capacity)
    if capacity > 0:
        knapsack(items,capacity)
    return(sack)


def main():
    items,capacities = read()
    sortedItems = sorted(items.items(), key=lambda val: val[1], reverse=True)

    print(sortedItems)
    print(knapsack(sortedItems,1))
    '''for cap in capacities:
        print(knapsack(sortedItems,cap))'''


main()

'''
red [1.0, 4]
green [2.0, 6]
blue [5.0, 8]
orange [9.0, 2]
[1, 6, 10, 20, 21]'''
