# Algoritmus

## Základní popis
 Tato složka obsahuje jednoduché řešení v jazyce Python 3.7.
 
### filter_functions.py 
 Knihovna  obsahuje zakladní sadu pravidel pro třidění seznamu řetězců, kam lze zapisovat funkce s návratovou hodnotou typu boolean pro filtrování

## Popis příkladu
 Příklad v main.py vytřídí ze seznamu řetězců palindromy neobsahujicí pisměno *A*. Složitost je *O(nm)*, kde *m* je počet pravidel a *n* je počet prvků.
```
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
```
