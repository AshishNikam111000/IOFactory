# Input
unit = int(input("Time Unit:"))

# Default values
di_units = {'T': 5, 'P': 4, 'C': 10}
di_solutions = {'T': 0, 'P': 0, 'C': 0}
di_earnings = {'T': 1500, 'P': 1000, 'C': 3000}

# Recursive method to find number of possible construction building along with their earnings
def maxProfit(unit,  index, i, con_sol, earning=0):
    if unit < di_units[i]:
        return [con_sol, earning]
    con_sol[index] += 1
    unit -= di_units[i]
    earning += unit * di_earnings[i]
    return maxProfit(unit, index, i, con_sol, earning)

# Looking for all three categories of building
maxEarning, index = 0, 0
solutions = {}
for i in ['T', 'P', 'C']:
    solutions[i] = maxProfit(unit, index, i, [0, 0, 0])
    maxEarning = max(maxEarning, solutions[i][1])
    index += 1

# Displaying output
index = 1
print("Earnings: $", maxEarning, sep='')
print("Solutions")
for key, value in solutions.items():
    if value[1] == maxEarning:
        print("\t{0}. T:{1} P:{2} C:{3}".format(
            index, value[0][0], value[0][1], value[0][2]))
    index += 1
