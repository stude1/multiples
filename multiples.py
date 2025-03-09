import sys

if len(sys.argv) != 3:
    raise AssertionError("Usage: python multiples.py <input_file> <output_file>")

inputFilename = sys.argv[1]
outputFilename = sys.argv[2]

input_file = open(inputFilename, "r")
content = input_file.readlines()
input_file.close()

multiples_count = []
multiples_output = []
output_file = open(outputFilename, "w")

# Sort output lines by amount of multiples in ascending order
def sort_output(items, counts):
    sorted_output = [0] * len(counts)
    counts_sorted = sorted(range(len(counts)), key=lambda k: counts[k])
    index = 0
    for count in counts_sorted:
        sorted_output[index] = items[count]
        index += 1
    return sorted_output


# Create a line of output in format "goal: multiple multiple..."
def create_line(counts, goal):
    output_line = str(goal) + ":"
    for item in counts:
        output_line += " " + str(item)
    output_line += "\n"
    return output_line

# For each line calculate all multiples and their count, and prepare the line for output
for line in content:
    multiples_list = []
    numbers = line.strip().split(" ")
    goal = int(numbers[2])
    list_ab = numbers[0:2]
    combined_count = 0
    for ab in list_ab:
        multiple = int(ab)
        count = 0
        while multiple < goal:
            multiples_list.append(multiple)
            count = count + 1
            multiple += int(ab)
        combined_count += count
    multiples_list.sort()
    multiples_output.append(create_line(multiples_list, goal))
    multiples_count.append(combined_count)

sorted_output = sort_output(multiples_output, multiples_count)

for line in sorted_output:
    output_file.write(line)
output_file.close()



