import random
#Part A
WEEKS = 16
CLASSES = 5
TUITION = 6000
cost_per_week = ((TUITION / CLASSES) / WEEKS)
print("Cost per week: ", cost_per_week, type(cost_per_week))


CLASSES_PER_WEEK = 3 
print("Classes per week: ",CLASSES_PER_WEEK, type(CLASSES_PER_WEEK))
cost_per_class = cost_per_week / CLASSES_PER_WEEK

print("Cost per class: ", cost_per_class, type(cost_per_class))


#Part B

LIST_OF_NUMBERS = [69, 420, 777, 444, 666]
print("List of numbers is: ", LIST_OF_NUMBERS, type(LIST_OF_NUMBERS))
random_choice = random.choice(LIST_OF_NUMBERS)
print("Randomly selected number from list of numbers: ",random_choice, type(random_choice))
