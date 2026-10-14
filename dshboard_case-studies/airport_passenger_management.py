passengers = ["Ayesha", "Rahul", "Fatima", "Sameer"]
while True:
    print("\n1.Add 2.Remove 3.Search 4.Sort 5.Dashboard 6.Exit")
    ch = input("Choice: ")
    if ch == "1" :
        passengers.append(input("Name: "))
    elif ch == "2":
        name = input("Name: ")
        if name in passengers:
            passengers.remove(name)
        else: print("Not found")
    elif ch ==" 3":
        name = input("Name: "); print("FOUND" if name in passengers else "NOT FOUND")
    elif ch == "4":
        passengers.sort()
    elif ch == "5":
        print("\n====================================")
        print(" AIRPORT PASSENGER DASHBOARD")
        print("====================================")
        print("Total Passengers:",len(passengers))
        for i,p in enumerate(passengers,1):
            print(i,".",p)
    elif ch == "6":
        break
    else:
        print("Invalid choice")