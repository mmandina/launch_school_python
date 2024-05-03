'''
input: 2 floats, bill and tip percentage
output: two floats, $tip and $total
'''


def tip_calculator():
    bill = float(input('What is the bill?'))
    tip = float(input('What is the tip percentage?'))
    tip_amount=(tip/100)*bill
    print(f'The tip is ${tip_amount:.2f}')
    print(f'The total is ${bill+tip_amount:.2f}')

tip_calculator()