open_tabs = int(input())
total_salary = int(input())

salary = total_salary

for i in range(1, open_tabs + 1):
    name_tab = input()

    if name_tab == "Facebook":
        salary -= 150
    elif name_tab == "Instagram":
        salary -= 100
    elif name_tab == "Reddit":
        salary -= 50
    elif salary <= 0:
        break
if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")
