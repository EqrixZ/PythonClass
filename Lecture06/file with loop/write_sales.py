def main():
    # Get the number of days.
    numdays = int(input('For how many days do' + \
                        'you have sales? '))
    
    # Open a new file named sales.txt
    sales_file = open('sales.txt', 'w')

    # Get the amount of sales of each day and write
    # it to the file
    for count in range(1, numdays +1):
        sales = float(input('Enter the sales for day #' + \
                            str(count) + ': '))
        
        # Write the sales amount to the file.
        sales_file.write(str(sales) + '\n')

    # Close the file.
    sales_file.close()
    print('Data written to sales.txt')

main()