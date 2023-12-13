empty_bottles = 5
founded_empty_bottles = 5
required_bottles = 2
all_empty_bottles = empty_bottles + founded_empty_bottles
bottles_bought = 1
result = 0

while bottles_bought > 0:
    bottles_bought = all_empty_bottles // required_bottles
    all_empty_bottles = all_empty_bottles % required_bottles + bottles_bought
    result += bottles_bought

print(result)
