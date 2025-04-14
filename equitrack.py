import datetime

# Define the vaccines
VACCINES = ["Tetanus", "EEE/WEE", "West Nile Virus", "Rabies", "Equine Influenza"]

# Store horse records in a list
equine_records = []

def add_horse_record():
    print("\n--- Add New Horse Record ---")
    horse_name = input("Horse Name: ")
    barn_name = input("Barn Name: ")
    owner_name = input("Owner Name: ")

    vaccines = {}
    for vaccine in VACCINES:
        date = input(f"Date of {vaccine} vaccine (YYYY-MM-DD): ")
        try:
            vaccines[vaccine] = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Skipping this vaccine.")
            vaccines[vaccine] = None

    record = {
        "horse_name": horse_name,
        "barn_name": barn_name,
        "owner_name": owner_name,
        "vaccines": vaccines
    }
    equine_records.append(record)
    print("Record added successfully!\n")

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

def main():
    while True:
        print("\n--- Equine Vaccination System ---")
        print("1. Add New Record")
        print("2. View All Records")
        print("3. Exit")
        choice = input("Select an option (1-3): ")

        if choice == "1":
            add_horse_record()
        elif choice == "2":
            view_all_records()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
