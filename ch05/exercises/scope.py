import math

def kobebryant(x):
    him = 0
    for counter in range(x):
        him = him + x

    return him

tokobebryant = 2
kobebryantResult = kobebryant(tokobebryant)
print("The result of", tokobebryant, "Kobe Bryant is", kobebryantResult)

values = [2,3,4,5,6,7]
powers = [2,3,4,5,6,7]
results = []

for i, value in enumerate(values):
  results.append(pow(value, powers[i]))

print("Your Answer is:\n", results)

def square(x):
    y = x * x
    return y

toSquare = 5
result = square(toSquare)
print("The result of", toSquare, "squared is", result)