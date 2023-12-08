class StateMachine:
    def __init__(self):
        self.states = set()
        self.start_state = None
        self.final_states = set()
        self.transitions = {}

    def add_state(self, state):
        self.states.add(state)

    def set_start_state(self, state):
        if state in self.states:
            self.start_state = state
        else:
            print("State not found or not in the state set.")

    def add_final_state(self, state):
        if state in self.states:
            self.final_states.add(state)
        else:
            print("State not found.")

    def add_transition(self, from_state, to_state, label):
        if from_state in self.states and to_state in self.states:
            if from_state not in self.transitions:
                self.transitions[from_state] = []
            self.transitions[from_state].append((to_state, label))
        else:
            print("One or both states not found.")

    def visualize(self):
        if not self.start_state:
            print("Start state is not set.")
            return

        print("\nFinite State Automaton:")
        paths = []

        def traverse(current_state, path):
            if current_state in self.final_states:
                paths.append(f"{path} -> {current_state}*")
                return

            if current_state not in self.transitions:
                paths.append(f"{path} -> {current_state}")
                return

            for next_state, label in self.transitions[current_state]:
                if next_state == current_state:
                    paths.append(f"{path} -> {current_state} --({label})-- Loop")
                else:
                    traverse(next_state, f"{path} -> {current_state} --({label})--")

        traverse(self.start_state, f"Start={self.start_state}")

        for path in paths:
            print(f"Path: {path}")

    def test_string(self, test_str):
        current_state = self.start_state
        for char in test_str:
            transition_found = False
            if current_state in self.transitions:
                for to_state, label in self.transitions[current_state]:
                    if label == char:
                        current_state = to_state
                        transition_found = True
                        break
            if not transition_found:
                return False, "Blocked: No transition for current character."

        return current_state in self.final_states, "Accepted" if current_state in self.final_states else "Rejected: Last transition doesn't lead to final state."

def main():
    fsm = StateMachine()

    while True:
        print("\nOptions:")
        print("1. Add state")
        print("2. Set start state")
        print("3. Add final state")
        print("4. Add transition")
        print("5. Visualize")
        print("6. Exit")
        print("7. Test string")

        choice = input("Enter your choice: ")

        if choice == "1":
            state = input("Enter state name: ")
            fsm.add_state(state)
        elif choice == "2":
            start_state = input("Enter start state: ")
            fsm.set_start_state(start_state)
        elif choice == "3":
            final_state = input("Enter final state: ")
            fsm.add_final_state(final_state)
        elif choice == "4":
            from_state = input("Enter from state: ")
            to_state = input("Enter to state: ")
            label = input("Enter transition label: ")
            fsm.add_transition(from_state, to_state, label)
        elif choice == "5":
            fsm.visualize()
        elif choice == "7":
            test_str = input("Enter string to test: ")
            accepted, message = fsm.test_string(test_str)
            print(f"Result: {'Accepted' if accepted else 'Rejected'} - {message}")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
