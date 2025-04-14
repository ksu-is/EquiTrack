import datetime
import dateparser

# Define the vaccines
VACCINES = ["Tetanus", "EEE/WEE", "West Nile Virus", "Rabies", "Equine Influenza"]

# Store horse records
equine_records = []

def parse_flexible_date(input_str):
    date = dateparser.parse(input_str)
    if date:
        return date.date()
    else:
        return None

def add_horse_record():
    print("\n--- Add New Horse Record ---")
    horse_name = input("Horse Name: ")
    barn_name = input("Barn Name: ")
    owner_name = input("Owner Name: ")

    vaccines = {}
    for vaccine in VACCINES:
        raw_date = input(f"Date of {vaccine} vaccine (any format, e.g. '2024-04-14', 'April 14', or 'today'): ")
        parsed_date = parse_flexible_date(raw_date)
        if parsed_date:
            vaccines[vaccine] = parsed_date
        else:
            print("⚠️ Could not parse date. Saving as 'Not Recorded'.")
            vaccines[vaccine] = None

    record = {
        "horse_name": horse_name,
        "barn_name": barn_name,
        "owner_name": owner_name,
        "vaccines": vaccines
    }
    equine_records.append(record)
    print("✅ Record added successfully!\n")

def view_all_records():
    print("\n--- Equine Vaccination Records ---")
    if not equine_records:
        print("No records found.")
    for idx, record in enumerate(equine_records, start=1):
        print(f"\nRecord #{idx}")
        print(f"Horse Name: {record['horse_name']}")
        print(f"Barn Name: {record['barn_name']}")
        print(f"Owner Name: {record['owner_name']}")
        print("Vaccinations:")
        for vaccine, date in record["vaccines"].items():
            print(f"  {vaccine}: {date if date else 'Not Recorded'}")

def check_vaccination_reminders():
    print("\n--- 🛎️ Upcoming Vaccination Reminders (Next 30 Days) ---")
    today = datetime.date.today()
    upcoming_window = today + datetime.timedelta(days=30)
    reminders_found = False

    for record in equine_records:
        for vaccine, last_date in record["vaccines"].items():
            if last_date:
                try:
                    next_due = last_date.replace(year=last_date.year + 1)
                except ValueError:
                    # Handle leap year issue if needed
                    next_due = last_date + datetime.timedelta(days=365)

                if today <= next_due <= upcoming_window:
                    print(f"\nHorse: {record['horse_name']} (Owner: {record['owner_name']})")
                    print(f"  🗓️ {vaccine} due on {next_due}")
                    reminders_found = True

    if not reminders_found:
        print("✅ No vaccinations due in the next 30 days.")

def main():
    while True:
        print("\n--- Equine Vaccination System ---")
        print("1. Add New Record")
        print("2. View All Records")
        print("3. Check Upcoming Vaccination Reminders")
        print("4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == "1":
            add_horse_record()
        elif choice == "2":
            view_all_records()
        elif choice == "3":
            check_vaccination_reminders()
        elif choice == "4":
            print("👋 Goodbye! Stay safe and vaccinate those ponies.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
