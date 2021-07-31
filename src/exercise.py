def main():
    #write your code below this line
    names = []

    while True:
        name = input()

        if name == '':
            break

        names.append(name)

    query = input("Search for?")
    if query in names:
        print(query + " was found!")
    else:
        print(query + " was not found!")

if __name__ == '__main__':
    main()
