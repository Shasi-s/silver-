def main():
    print("This program converts Canadian dollars to Rupees")
    print()

    Canadian_dollars = eval(input("Enter amount in canadian dollars: "))

    rupees = convert_to_rupees(Canadian_dollars)

    print("That is" , rupees, "rupees. ")

convert_to_rupees = lambda Canadian_dollars: Canadian_dollars * 61.324

main()