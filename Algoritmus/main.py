from filter_functions import palindrome, contain_a

# Example of test list
test_list = {"Nun", "Taco cat", "No lemon, no melon", "Never odd or even", "Not a palindrome"}

# Example of rules list
rules_list = [palindrome, contain_a]

# Empty list for accepted elements
final_list = set()

print("Set of elements to test: ", test_list)

for element in test_list:
    passed = True

    for rule in rules_list:
        if not rule(element):
            passed = False
            break

    if passed:
        final_list.add(element)


print("Set of elements that were accepted by rules:", final_list)

