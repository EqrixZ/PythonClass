# This program display the total of the
# amounts in the sales_data.txt file.

def main():
    # Intialize an accumulator.
    total = 0.0
    try:
        # Open the sales_data.txt file.
        infile = open('sales_data.txt', 'r')

        # Read the values from the file and
        # accmulate them.
        for line in infile:
            amount = float(line)
            total += amount

        # Close the file.
        infile.close()

        # Print the total.
        print(format(total, ',.2f'))

    except IOError:
        print('An error occured trying to read the file.')

    except ValueError:
        print('Non-numberic data found in the file.')

    except:
        print('An error occured.')

# Call the main function.
main()