def main():
    print("This program converts US dollars to Rupees")
    print()

    dollars = eval(input("Enter amount in dollars: "))

    rupees = convert_to_rupees(dollars)

    print("That is" , rupees, "rupees. ")

convert_to_rupees = lambda dollars: dollars * 81.22

main()