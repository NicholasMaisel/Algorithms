items = {}

class knapsack():
    def __init__(self,size,items):
        self.size = size
        self.items = items
        self.contents = {}

    def sack(item,qty):
        self.size -= items[item]['cost']
        self.contents[item] = qty


    def greedyChooser(self, size_avail, item, cost, qty_avail):
        qty = size_avail // cost
        if qty > 0: # Checks to see if the sack can fit any of item
            if qty_avail >= qty: # checks to see if we can add all of the item
                self.sack(item, qty)
            else:   #qty_avil is less than qty, so add all we can
                self.sack(item,qty_avail)


def read():
    for line in open('/Users/nicholasmaisel/Documents/Programming/Algorithms/spice.txt','r'):
        items = {}
        line = line.rstrip().split(';')
        line = [x.strip() for x in line]
        if 'spice name' in line[0]:
            items[line[0].split('=')[1].strip()] = [line[1].split('=')[1].strip(),
                                                    line[2].split('=')[1].strip()]

def main():
    items =
