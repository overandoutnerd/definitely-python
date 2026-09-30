seats = [
    [False, False, False, False],
    [False, False, False, False],
    [False, False, False, False]
]


def bookSeat(seats, row, column):
    validRow = 0 <= row < len(seats)
    validColumn = 0 <= column < len(seats[0])

    if validRow and validColumn:
        if seats[row][column] == False:
            seats[row][column] = True
            return "BOOKED"
        else:
            return "ALREADY BOOKED"
    else:
        return "INVALID SEAT"


def displayMap(seats):
    print("\nGrid Layout ([ ] = Empty, [X] = Booked):")

    for row in range(len(seats)):
        print(f"Row {row}: ", end="")

        for column in range(len(seats[row])):
            if seats[row][column]:
                print("[X]  ", end="")
            else:
                print("[ ]  ", end="")

        print()


while True:
    print("\n1. Book Seat")
    print("2. View Seat Map")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        row = int(input("Enter row number: "))
        column = int(input("Enter column number: "))

        bookingStatus = bookSeat(seats, row, column)
        print("Booking Status:", bookingStatus)

    elif choice == 2:
        displayMap(seats)

    elif choice == 3:
        break

    else:
        print("Invalid choice.")


totalSeats = 0
bookedSeats = 0

for row in seats:
    for seat in row:
        totalSeats += 1

        if seat:
            bookedSeats += 1

if totalSeats > 0:
    occupancyRate = (bookedSeats / totalSeats) * 100
else:
    occupancyRate = 0


print("\n====================================================")
print("          THEATER OCCUPANCY DASHBOARD")
print("====================================================")

displayMap(seats)

print("----------------------------------------------------")
print(f"Total Seats     : {totalSeats}")
print(f"Booked Seats    : {bookedSeats}")
print(f"Occupancy Rate  : {occupancyRate:.1f}%")
print("====================================================")