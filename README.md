# Multiples
Small script to find multiples of first two numbers (A, B) that are smaller than the third number ("Goal").

# Prerequisites
Python installed. Tested with 3.9, should work with any supported version.

# Usage
```
python multiples.py <input_file> <output_file>
```

Input needs to be a text file with lines having three integers:
```
A B Goal
```
The script counts multiples of `A` and `B` that are lower than `Goal`.

Output is provided in the format, sorted by ascending order of amount of multiples:
```
Goal: multiple multiple multiple...
```

## Example
input:
```
4 7 20
5 8 31
8 9 21
3 4 30
```

For which the output would be:
```
21: 8 16 18 9
20: 4 7 8 12 14 16
31: 5 8 10 15 16 20 24 25 30
30: 3 4 6 8 9 12 15 16 18 20 21 24 27 28
```

Sample input file provided (input.txt).
