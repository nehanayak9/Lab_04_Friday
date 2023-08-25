class Process:
    def __init__(self, pid, name, start_time, priority):
        self.pid = pid
        self.name = name
        self.start_time = start_time
        self.priority = priority

    def __str__(self):
        return f"{self.pid}\t{self.name}\t{self.start_time}\t{self.priority}"

def sort_and_print(processes, key):
    sorted_processes = sorted(processes, key=lambda x: getattr(x, key))
    print("P_ID\tName\tStart Time (ms)\tPriority")
    for process in sorted_processes:
        print(process)

def main():
    processes = [
        Process("P1", "VSCode", 100, "MID"),
        Process("P23", "Eclipse", 234, "MID"),
        Process("P93", "Chrome", 189, "High"),
        Process("P42", "JDK", 9, "High"),
        Process("P9", "CMD", 7, "High"),
        Process("P87", "NotePad", 23, "Low"),
    ]

    while True:
        print("\nMenu:")
        print("1. Sort by Process ID (P_ID)")
        print("2. Sort by Start Time (ms)")
        print("3. Sort by Priority")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            sort_and_print(processes, 'pid')
        elif choice == '2':
            sort_and_print(processes, 'start_time')
        elif choice == '3':
            sort_and_print(processes, 'priority')
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
