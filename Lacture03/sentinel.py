keep_going = 'y'

# Calculate a series of commissions.
while keep_going == 'y':
    # Get a wholesale cost.
    wholesale = float(input("Enter the item' wholesale cost: "))
    retail_price = wholesale * 2.5

    # Calculate the commission/retail price.
    commission = retail_price

    # Display the commission.
    print('Retail price: $',\
    format(commission, ',.2f'), sep= '')

    # See if the user wants to do another one.
    keep_going = input('Do you have another item?' + \
                       ' (Enter y for yes): ')