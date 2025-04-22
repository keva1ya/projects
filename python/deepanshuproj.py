hotel_name = "GUJARAT BHAWAN"
double_bedrooms = 7
four_bed_rooms = 5
payments_received = 0
payments_pending = 0

double_room_price = 2000
four_bed_room_price = 3500

bookings = []

def book_room():
    global double_bedrooms, four_bed_rooms, payments_pending

    print("\nRoom Types:\n1. Double-bed Room (₹2000 per night)\n2. Four-Bed Room (₹3500 per night)")
    choice = input("Enter room type (1 or 2): ")

    if choice == "1" and double_bedrooms > 0:
        double_bedrooms -= 1
        payments_pending += double_room_price
        bookings.append(("Double-bed Room", double_room_price, 0, double_room_price))
        print("✅ Double-bed Room booked successfully!")
    elif choice == "2" and four_bed_rooms > 0:
        four_bed_rooms -= 1
        payments_pending += four_bed_room_price
        bookings.append(("Four-Bed Room", four_bed_room_price, 0, four_bed_room_price))
        print("✅ Four-Bed Room booked successfully!")
    else:
        print("❌ Sorry, no rooms available for this type!")

def receive_payment():
    global payments_received, payments_pending

    print("\n🔍 Checking Pending Payments...")

    if len(bookings) == 0:
        print("No bookings found.")
        return

    for i, (room_type, price, paid, remaining) in enumerate(bookings, start=1):
        if remaining > 0:
            print(f"{i}. {room_type} - Total: ₹{price}, Paid: ₹{paid}, Remaining: ₹{remaining}")

    payment = input("Enter the amount you want to pay: ₹")

    if payment.isdigit():
        payment = int(payment)
        for i in range(len(bookings)):
            room_type, price, paid, remaining = bookings[i]
            if remaining > 0:
                if payment >= remaining:
                    payments_received += remaining
                    payments_pending -= remaining
                    bookings[i] = (room_type, price, paid + remaining, 0)
                    print(f"✅ Full payment received for {room_type}.")
                else:
                    payments_received += payment
                    payments_pending -= payment
                    bookings[i] = (room_type, price, paid + payment, remaining - payment)
                    print(f"✅ Partial payment of ₹{payment} received for {room_type}. Remaining balance: ₹{remaining - payment}")
                break
        else:
            print("❌ No pending payments found.")
    else:
        print("❌ Invalid input. Please enter a valid amount.")

def check_status():
    print("\n=== HOTEL STATUS ===")
    print(f"🏨 Hotel Name: {hotel_name}")
    print(f"🏡 Empty Double Rooms: {double_bedrooms}/7")
    print(f"🏡 Empty Four-Bed Rooms: {four_bed_rooms}/5")
    print(f"💰 Total Payments Received: ₹{payments_received}")
    print(f"💳 Total Payments Pending: ₹{payments_pending}")

def view_excel_data():
    print("\n📊 HOTEL BOOKINGS RECORD (Excel Format)")
    if len(bookings) > 0:
        print("Room Type, Price, Payment Received, Remaining Balance")
        for booking in bookings:
            print(f"{booking[0]}, ₹{booking[1]}, ₹{booking[2]}, ₹{booking[3]}")
    else:
        print("No bookings found.")

def main_menu():
    print("\n===== GUJARAT BHAWAN YATRI NIVAS HOTEL =====")
    print("1. Book a Room")
    print("2. PAY booking amount")
    print("3. Check Hotel Status")
    print("4. Manager: View Booking Records")
    print("5. Exit")

    option = input("Enter your choice: ")

    if option == "1":
        book_room()
    elif option == "2":
        receive_payment()
    elif option == "3":
        check_status()
    elif option == "4":
        view_excel_data()
    elif option == "5":
        print("✅ THANK YOU FOR COMING🙏.")
        return
    else:
        print("❌ Invalid choice! Please enter a valid option.")
    
    main_menu()

main_menu()
