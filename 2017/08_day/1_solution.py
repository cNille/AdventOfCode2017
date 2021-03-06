import re

data = open('my.input')
var = {}
max_val = 0

for row in data:
    [   variable, 
        operator, 
        delta, 
        iif, 
        condition_variable, 
        condition_operator, 
        condition_value] = row[:-1].split(' ')
    
    if condition_variable not in var:
        var[condition_variable] = 0 
    if variable not in var: 
        var[variable] = 0 

    if not eval('var["' + condition_variable + '"] ' + condition_operator + ' ' + condition_value):
        continue

    if operator == 'dec':
        var[variable] -= int(delta)
    else:     
        var[variable] += int(delta)

for v in var.values():
    max_val = max(max_val, v)
print(max_val)
