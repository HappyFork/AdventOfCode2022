# AOC23-D2P2.py
# Advent of code 2023, day 2 part 2

#FILENAME = "testd2.txt"
FILENAME = "inputd2"


total = 0       # Puzzle solution. Sum of possible line IDs

# Open the file
with open( FILENAME ) as f:
    # Get each line
    lines = f.readlines()
    for l in lines:
        spl = l.split(":",1)                # First split, 0 is game #, 1 is the rest of the line
        most_blue = 0
        most_red = 0
        most_green = 0
        rounds = spl[1].split(";")          # Get the rounds from the rest of the line
        for r in rounds:                    # For each line,
            cubes = r.split(",")            # Get the cubes of different colors pulled
            for c in cubes:                 # Cube lists have 2 parts: the color and the number
                cs = c.strip()              # First, strip whitespace
                t = cs.split(" ")           # Then split into color (1) and number (0)
                if t[1] == "blue" and int(t[0]) > most_blue:
                    most_blue = int(t[0])
                elif t[1] == "red" and int(t[0]) > most_red:
                    most_red = int(t[0])
                elif t[1] == "green" and int(t[0]) > most_green:
                    most_green = int(t[0])
        total += int(most_blue*most_red*most_green)
        

print( total )