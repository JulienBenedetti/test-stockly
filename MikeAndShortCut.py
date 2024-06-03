# INPUT: 
## n == number of intersections
## a == shortcuts [a1, a2, ...]
## a1 == walk from current intersection to a1 using 1 energy

# given input is always valid

def shortcut_or_next(current_position, current_dest, shortcuts):
    # check is shortcut faster than next node
    current_dest -= 1
    shortcut_destination = shortcuts[current_position] - 1
    if shortcut_destination > current_dest or shortcut_destination <= current_position:
        print("NO SHORTCUT")
        return current_position + 1
    print("SHORTCUT!")
    return current_position + shortcut_destination

def compute_min_energy(shortcuts, current_dest):
    energy = 0 
    print("\nComputing for destination: "+str(current_dest)+" = "+str(shortcuts[current_dest]))
    current_position = 0
    # while we didnt reach destination
    while current_position != current_dest:
        # check if shortcut is faster than next node
        print("current_position: "+str(current_position)+", current_dest: "+str(current_dest)+", shortcut_destination: "+str(shortcuts[current_position] - 1))
        current_position = shortcut_or_next(current_position, current_dest, shortcuts)
        energy += 1
    return energy

def compute_mike_shortcuts(number_intersections, input_shortcuts):
    ## compute from current to dest
    result = []
    for current_dest in range(number_intersections) :
        min_energy = compute_min_energy(input_shortcuts, current_dest)
        print(min_energy)
#        print("minimum_energy from 1 to "+str(current_dest)+": "+str(min_energy))
        result.append(min_energy)
    # print("final result:")
    # print(result)

input_number_intersections = int(input())
input_shortcuts = [int(i) for i in input().split()]

compute_mike_shortcuts(input_number_intersections, input_shortcuts)
