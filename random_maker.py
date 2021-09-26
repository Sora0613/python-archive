import random

def main():
    print("[Info]If you want to use this file for Roto6, please press 6")
    print("      or you want to use for Roto7, please press 7.")
    print("      or If you want more advanced settings, please press [c].")
    print("      Then, you can setting the int (min, max, element count) ")
    print("      The numbers you enter must be in this order.")

    result = input("please press 6 or 7 or 0 (custom) : ")

    if result.isdigit():

        if result == 6:
            print("[Info]The numbers are ... " + str(make_random(1, 43, 6)))
        elif result == 7:
            print("[Info]The numbers are ... " + str(make_random(1, 37, 7)))
        elif result == 0:
            try:
                min = int(input("[Info]Please set min : "))
                max = int(input("[Info]Please set max : "))
                element = int(input("[Info]Please set elements count : "))

                print("[Info]The numbers are ... " + str(make_random(min, max, element)))
            except ValueError:
                print("[Info]That's not an int!")

    else:
        print("[Info]The value you entered is incorrect.")


def make_random(min, max, element):
    contents = []
    while len(contents) < element:
        n = random.randint(min, max)
        if not n in contents:
            contents.append(n)
    return contents


if __name__ == '__main__':
    main()
