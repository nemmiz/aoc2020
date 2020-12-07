import re


with open('../input/07.txt') as stream:
    lines = [line.strip() for line in stream]



def parse_rules(lines):
    contains = {}
    contained_in = {}
    for line in lines:
        parts = line.split()
        bag = f'{parts[0]} {parts[1]}'
        #print(bag)
        tmp = {}
        for i in range(4, len(parts), 4):
            if parts[i] != 'no':
                bag2 = f'{parts[i+1]} {parts[i+2]}'
                tmp[bag2] = int(parts[i])
                x = contained_in.get(bag2, set())
                x.add(bag)
                contained_in[bag2] = x
        contains[bag] = tmp
    #print(contains)
    #print(contained_in)
    return contains, contained_in

def part1(bag, contained_in):
    options = set()
    def _find(bag):
        for parent in contained_in.get(bag, []):
            options.add(parent)
            _find(parent)
    _find(bag)
    print(len(options))
    #return options

def part2(bag, contains):
    def _count(bag):
        n = 0
        for name, count in contains.get(bag, {}).items():
            n += count
            n += count * _count(name)
        return n
    print(_count(bag))
            #if x != 0:
            #    n += x * count
            #print(name, count)
            #n += (count * _find(name))
            #_find(name)
    #if bag in contains:
    #return _find(bag)
    #return n


contains, contained_in = parse_rules(lines)
part1('shiny gold', contained_in)
part2('shiny gold', contains)
#print(len(find_options('shiny gold', contained_in)))


    #parts = line.split()
    #print(parts[0], parts[1])
    #print(line.split())

