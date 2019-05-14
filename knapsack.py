
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


def knapsack(items, capacity):
    sack = {}
    for i in items:
        if capacity == 0:
            break
        price = i[1][0]
        qty = i[1][1]

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

        elif 1 not in [p[1][0] for p in items]:
            frac_qty = capacity/price #add the item until full
                #Add frac_item of item to sack
            capacity -= frac_qty * price
            sack[i[0]] = frac_qty

    for i in sack:
        sack[i] = round(sack[i],2)
    return(sack)


def main():
    items, capacities = read()

    for cap in capacities:
        items =read()[0]
        print(cap, knapsack(items,cap))



main()
