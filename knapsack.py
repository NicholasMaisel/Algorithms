
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

    sortedItems = sorted(items.items(), key=lambda val: val[1], reverse=True)
    return(sortedItems,capacities)


def knapsack(itemGen, capacity):
    sack = {}
    sackValue = 0

    while capacity > 0:

        try:
            item = next(itemGen)
            itemName = item[0]
            itemQty = item[1][1]
            itemPrice = item[1][0]
        except:
            return(sack, sackValue)

        if capacity >= itemQty:
            sack[itemName] = itemQty #adds all of item[index] qty to sack
            sackValue += itemQty * itemPrice #adds to sack value
            capacity -= itemQty #updates cap
            item[1][1] = 0

        elif capacity < itemQty:
            sack[itemName] = capacity
            item[1][1] -= capacity
            sackValue += capacity * itemPrice
            capacity = 0

    return(sack, sackValue)


def spice_gen(items):
    i = 0
    while i < len(items):
        yield(items[i])
        i +=1


def main():
    items, capacities = read()

    for cap in capacities:
        items=read()[0]
        sg = spice_gen(items)
        contents, value = knapsack(sg,cap)
        print(f'The sack with capacity: {cap}, is worth {value} and contains:')
        for k,v in contents.items():
            print(f'{v} of {k}')



main()
