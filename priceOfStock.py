def total_price(prompt):
    first, second, third = prompt.split(' ')
    price =  (int(shares) * float((int(first) + (int(second) / int(third)))))
    return (str(shares) + ' shares with market price ' + str(first) + ' ' + str(second) + '/' + str(third)  + ' have value $' + str('%.2f' % price))

def yes_no(prompt):
    if prompt == 'y':
        return (True)
    elif prompt == 'n':
        return (False)
    

cont = 'Continue'

while cont == 'Continue':
    try:
        shares = int(input('Enter number of shares: '))
    except ValueError:
        print('Invalid number!')
        continue
    valid = False
    while valid != True:
        try:
            print(total_price((str(input('Enter price (dollars, numerator, denominator): ')))))
            valid = True      
        except ValueError:
            print('Invalid price!') 
            continue


    if (yes_no(input('Continue: '))):
        cont = 'Continue'
    else:
        cont = 'stop'