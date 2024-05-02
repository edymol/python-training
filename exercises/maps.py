n = int(input())

phone_book = {}

# Populate the phone book
for _ in range(n):
    name, number = input().split()
    phone_book[name] = number

# Process queries until there's no more input
while True:
    try:
        query = input()
        if query:
            if query in phone_book:
                print(query + " = " + phone_book[query])
            else:
                print("Not found")
        else:
            break
    except EOFError:
        break
