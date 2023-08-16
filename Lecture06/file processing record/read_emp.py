def main():
    emp_file = open('employees.txt', 'r')
    for line in emp_file:
        emp = emp_file.readline()
        emp[2] = emp[2].strip('')

        print('Name:',emp[0])
        print('ID:', emp[1])
        print('Dept:', emp[2])

    emp_file.close()
main()