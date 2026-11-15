# Read data from file1.txt and save it to file2.txt

try:
    # Step 1: open file1.txt in read mode and read all its content
    with open('file1.txt', 'r') as f1:
        data = f1.read()

    # Step 2: open file2.txt in write mode and write the content
    with open('file2.txt', 'w') as f2:
        f2.write(data)

    print('Data copied from file1.txt to file2.txt successfully')

except FileNotFoundError:
    print('file1.txt not found')
except Exception as e:
    print('Something went wrong:', e)
