class FlightTable:
    def __init__(self):
        self.data = [
            ("Mumbai", "India", "Sri Lanka", "DAY"),
            ("Delhi", "England", "Australia", "DAY-NIGHT"),
            ("Chennai", "India", "South Africa", "DAY"),
            ("Indore", "England", "Sri Lanka", "DAY-NIGHT"),
            ("Mohali", "Australia", "South Africa", "DAY-NIGHT"),
            ("Delhi", "India", "Australia", "DAY")
        ]

    def search_by_team(self, team_name):
        result = [match for match in self.data if team_name in (match[1], match[2])]
        return result

    def search_by_location(self, location):
        result = [match for match in self.data if match[0] == location]
        return result

    def search_by_timing(self, timing):
        result = [match for match in self.data if match[3] == timing]
        return result

    def print_matches(self, matches):
        for match in matches:
            print("Location:", match[0])
            print("Team 01:", match[1])
            print("Team 02:", match[2])
            print("Timing:", match[3])
            print()

def main():
    flight_table = FlightTable()

    while True:
        print("Search Options:")
        print("1. List of all matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Quit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            team_name = input("Enter the Team name: ")
            matches = flight_table.search_by_team(team_name)
            flight_table.print_matches(matches)
        elif choice == "2":
            location = input("Enter the Location: ")
            matches = flight_table.search_by_location(location)
            flight_table.print_matches(matches)
        elif choice == "3":
            timing = input("Enter the Timing: ")
            matches = flight_table.search_by_timing(timing)
            flight_table.print_matches(matches)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
