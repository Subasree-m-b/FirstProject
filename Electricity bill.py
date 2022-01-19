def bill(unit):
    if unit <= 100:
        amount = 0
    elif unit > 100 and unit < 200:
        amount = unit * 5
    else:
        amount = 500+(unit-200)*10
        
    return amount
    
print("Your electricity bill is: " + str(bill(200)))