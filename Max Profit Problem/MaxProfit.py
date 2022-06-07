# Taking input from user
unit = int(input('Time Unit: '))
earnings = int(input('Earnings: $'))

# Default time unit for establishment
di_units = {
    't': 5,
    'p': 4,
    'c': 10,
}

# Dictionary to store number of establishment which can be constructed
di_solutions = {
    't': 0,
    'p': 0,
    'c': 0,
}

# Default earnings from respective establishment
te, pe, ce = 1500, 1000, 3000

# An array to store possible solutions
possible_solutions = []

# Finding possible solutions based on units and earnings given by user
if earnings % te == 0 and unit >= di_units['t']:
    possible_solutions.append('t')
if earnings % pe == 0 and unit >= di_units['p']:
    possible_solutions.append('p')
if earnings % ce == 0 and unit >= di_units['c']:
    possible_solutions.append('c')

index = 1
final_solutions = []
for i in possible_solutions:
    temp = unit
    while temp >= di_units[i]:
        di_solutions[i] += 1
        temp -= di_units[i]
    final_solutions.append("\t {}. T:{} P:{} C:{}".format(
        index, di_solutions['t'], di_solutions['p'], di_solutions['c']))
    di_solutions[i] = 0
    index += 1

# Displaying output
print("Solutions")
for i in final_solutions:
    print(i)
