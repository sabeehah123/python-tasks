def pycat():
    f = open(input("Enter filename: "), "r")
    text = f.read()
    print(text)
    f.close()

pycat()

