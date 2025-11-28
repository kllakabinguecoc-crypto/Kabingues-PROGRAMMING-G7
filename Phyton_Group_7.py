from datetime import datetime

appointments = []

def view_health_center_info():
    print("\n--- Health Center Information ---")
    print("Name: Barangay Carmen Health Center")
    print("Location: Barangay Carmen, Cagayan de Oro City")
    print("Services: Medical check-up, consultation, appointment, health education")
    print("\nOperating Hours:")
    print("Monday - Friday")
    print("Morning: 8:00 AM - 11:59 AM")
    print("Afternoon: 1:00 PM - 3:59 PM")
    print("\nContact Information:")
    print("Facebook: Barangay Carmen Health Center CDO")
    print("Email: carmenhealthcenter@gmail.com")
    print("Hotline: 09756094699")
    input("\nPress Enter to return...")

def is_valid_time(time_str):
    """Check if entered time is within 8:00–11:59 AM or 1:00–3:59 PM"""
    try:
        t = datetime.strptime(time_str.strip().lower(), "%I:%M %p").time()
        morning = datetime.strptime("8:00 am", "%I:%M %p").time(), datetime.strptime("11:59 am", "%I:%M %p").time()
        afternoon = datetime.strptime("1:00 pm", "%I:%M %p").time(), datetime.strptime("3:59 pm", "%I:%M %p").time()
        return morning[0] <= t <= morning[1] or afternoon[0] <= t <= afternoon[1]
    except:
        return False

def book_checkup():
    print("\n--- Book a Consultation Schedule ---")
    name = input("Enter your full name: ")
    contact = input("Enter your contact number: ")
    checkup = input("Enter type of check-up (General, Dental, Prenatal, etc.): ")
    date = input("Enter preferred date (YYYY-MM-DD): ")
    time = input("Enter preferred time (e.g., 9:30 AM): ")

    if not is_valid_time(time):
        print("\n⚠️ Invalid time. Please choose between 8:00–11:59 AM or 1:00–3:59 PM.\n")
        return

    for a in appointments:
        if a["date"] == date and a["time"].lower() == time.lower():
            print(f"\n⚠️ Sorry, that slot ({date} at {time}) is already booked.\n")
            return

    appointments.append({"name": name, "contact": contact, "checkup": checkup, "date": date, "time": time})
    print(f"\n✅ Appointment successfully booked!\n{name} | {checkup} | {date} at {time}\n")

def view_all_appointments():
    print("\n--- All Confirmed Appointments ---")
    if not appointments:
        print("No appointments found.\n")
    else:
        for i, a in enumerate(appointments, 1):
            print(f"{i}. {a['name']} | {a['checkup']} | {a['date']} at {a['time']}")
        print()

def cancel_appointment():
    print("\n--- Cancel Appointment ---")
    name = input("Enter patient name to cancel: ").lower()
    for a in appointments:
        if a["name"].lower() == name:
            if input(f"Cancel {a['name']}'s appointment? (yes/no): ").lower() == "yes":
                appointments.remove(a)
                print(f"❌ Appointment for {a['name']} cancelled.\n")
            else:
                print("Cancellation aborted.\n")
            return
    print("No appointment found for that name.\n")


def patient_menu():
    while True:
        print("\n===== PATIENT MENU =====")
        print("1. View Health Center Info")
        print("2. Book a Consultation")
        print("3. Back to Main Menu")
        choice = input("Enter choice: ")
        if choice == "1":
            view_health_center_info()
        elif choice == "2":
            book_checkup()
        elif choice == "3":
            break
        else:
            print("Invalid choice.\n")

def staff_menu():
    while True:
        print("\n===== HEALTH STAFF MENU =====")
        print("1. View All Appointments")
        print("2. Cancel Appointment")
        print("3. Back to Main Menu")
        choice = input("Enter choice: ")
        if choice == "1":
            view_all_appointments()
        elif choice == "2":
            cancel_appointment()
        elif choice == "3":
            break
        else:
            print("Invalid choice.\n")

def main_menu():
    while True:
        print("\n===== BARANGAY CARMEN HEALTH CENTER SCHEDULING SYSTEM =====")
        print("1. Patient")
        print("2. Health Staff / Receptionist")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            patient_menu()
        elif choice == "2":
            if input("Enter staff password: ") == "PHINMA":
                print("\n✅ Access granted. Welcome, Health Staff!\n")
                staff_menu()
            else:
                print("\n❌ Incorrect password.\n")
        elif choice == "3":
            print("\nThank you for using the system. Goodbye!\n")
            break
        else:
            print("Invalid choice.\n")

main_menu()

from datetime import datetime

appointments = []

def view_health_center_info():
    print("\n--- Health Center Information ---")
    print("Name: Barangay Carmen Health Center")
    print("Location: Barangay Carmen, Cagayan de Oro City")
    print("Services: Medical check-up, consultation, appointment, health education")
    print("\nOperating Hours:")
    print("Monday - Friday")
    print("Morning: 8:00 AM - 11:59 AM")
    print("Afternoon: 1:00 PM - 3:59 PM")
    print("\nContact Information:")
    print("Facebook: Barangay Carmen Health Center CDO")
    print("Email: carmenhealthcenter@gmail.com")
    print("Hotline: 09756094699")
    input("\nPress Enter to return...")

def is_valid_time(time_str):
    """Check if entered time is within 8:00–11:59 AM or 1:00–3:59 PM"""
    try:
        t = datetime.strptime(time_str.strip().lower(), "%I:%M %p").time()
        morning = datetime.strptime("8:00 am", "%I:%M %p").time(), datetime.strptime("11:59 am", "%I:%M %p").time()
        afternoon = datetime.strptime("1:00 pm", "%I:%M %p").time(), datetime.strptime("3:59 pm", "%I:%M %p").time()
        return morning[0] <= t <= morning[1] or afternoon[0] <= t <= afternoon[1]
    except:
        return False

def book_checkup():
    print("\n--- Book a Consultation Schedule ---")
    name = input("Enter your full name: ")
    contact = input("Enter your contact number: ")
    checkup = input("Enter type of check-up (General, Dental, Prenatal, etc.): ")
    date = input("Enter preferred date (YYYY-MM-DD): ")
    time = input("Enter preferred time (e.g., 9:30 AM): ")

    if not is_valid_time(time):
        print("\n⚠️ Invalid time. Please choose between 8:00–11:59 AM or 1:00–3:59 PM.\n")
        return

    for a in appointments:
        if a["date"] == date and a["time"].lower() == time.lower():
            print(f"\n⚠️ Sorry, that slot ({date} at {time}) is already booked.\n")
            return

    appointments.append({"name": name, "contact": contact, "checkup": checkup, "date": date, "time": time})
    print(f"\n✅ Appointment successfully booked!\n{name} | {checkup} | {date} at {time}\n")

def view_all_appointments():
    print("\n--- All Confirmed Appointments ---")
    if not appointments:
        print("No appointments found.\n")
    else:
        for i, a in enumerate(appointments, 1):
            print(f"{i}. {a['name']} | {a['checkup']} | {a['date']} at {a['time']}")
        print()

def cancel_appointment():
    print("\n--- Cancel Appointment ---")
    name = input("Enter patient name to cancel: ").lower()
    for a in appointments:
        if a["name"].lower() == name:
            if input(f"Cancel {a['name']}'s appointment? (yes/no): ").lower() == "yes":
                appointments.remove(a)
                print(f"❌ Appointment for {a['name']} cancelled.\n")
            else:
                print("Cancellation aborted.\n")
            return
    print("No appointment found for that name.\n")


def patient_menu():
    while True:
        print("\n===== PATIENT MENU =====")
        print("1. View Health Center Info")
        print("2. Book a Consultation")
        print("3. Back to Main Menu")
        choice = input("Enter choice: ")
        if choice == "1":
            view_health_center_info()
        elif choice == "2":
            book_checkup()
        elif choice == "3":
            break
        else:
            print("Invalid choice.\n")

def staff_menu():
    while True:
        print("\n===== HEALTH STAFF MENU =====")
        print("1. View All Appointments")
        print("2. Cancel Appointment")
        print("3. Back to Main Menu")
        choice = input("Enter choice: ")
        if choice == "1":
            view_all_appointments()
        elif choice == "2":
            cancel_appointment()
        elif choice == "3":
            break
        else:
            print("Invalid choice.\n")

def main_menu():
    while True:
        print("\n===== BARANGAY CARMEN HEALTH CENTER SCHEDULING SYSTEM =====")
        print("1. Patient")
        print("2. Health Staff / Receptionist")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            patient_menu()
        elif choice == "2":
            if input("Enter staff password: ") == "PHINMA":
                print("\n✅ Access granted. Welcome, Health Staff!\n")
                staff_menu()
            else:
                print("\n❌ Incorrect password.\n")
        elif choice == "3":
            print("\nThank you for using the system. Goodbye!\n")
            break
        else:
            print("Invalid choice.\n")

main_menu()

