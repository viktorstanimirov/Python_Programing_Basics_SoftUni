models_of_computers = int(input())

reiting = 0
sales = 0

for number in range(1, models_of_computers + 1):
    sales_plus_reiting = int(input())
    units = sales_plus_reiting % 10
    hundrets_pus_tens = sales_plus_reiting // 10
    if units == 2:
        sales += 0
        reiting += units
    elif units == 3:
        sales = sales + (hundrets_pus_tens * 0.50)
        reiting += units
    elif units == 4:
        sales = sales + (hundrets_pus_tens * 0.70)
        reiting += units
    elif units == 5:
        sales = sales + (hundrets_pus_tens * 0.85)
        reiting += units
    elif units == 6:
        sales = sales + (hundrets_pus_tens * 1)
        reiting += units

avg_reiting = reiting / models_of_computers

print(f"{sales:.2f}")
print(f"{avg_reiting:.2f}")
