print('>')
user = input()
numbers = []
while True:
    print('>')
    if user == "help":
        print('Show')
        print('Add <Value1>, <Value2>, <Value3>...')
        print('Update <Old Value> <New Value>')
        print('Reset')
        print('Exit')

        choice = input()

        if choice == "show":
            if len(numbers) <1:
                print("List is empty")
            else:
                print(numbers)

        elif choice == "add":
            nums = [input()]
            numbers.extend(nums)
            print("Items added")

        elif choice == "update":
            old_value = int(input())
            new_value = int(input())
            position = numbers.index(old_value)
            numbers.index(position)


        elif choice == "reset":
            numbers = []
            print("List is cleared")

        elif choice == "exit":
            break