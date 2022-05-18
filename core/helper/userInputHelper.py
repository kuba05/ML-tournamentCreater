def confirm(text):
    while True:
        a = input(text)
        if len(a) > 0:
            if a[0].lower() == "y":
                return True
            elif a[0].lower() == "n":
                return False
        print(f"\"{a}\" is not a valid choice!")
        print("Use \"Y\" or \"N\" instead!")