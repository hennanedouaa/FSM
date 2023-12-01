#les boucles 
#Deterministe 
# cases accepted : - the chars of the word takes us from S0 and finishes at Sf (one transition at each character and
#we can pass by Sf before it's ending what's important is that the last transition ( character take sus to Sf )
# refused : 1- the last transition (character) doesn't take us to Sf 
#2- we are blocked at a state and can't move ( becausethe state doesn't have a tranistion (coming out of the state )that is laeled as the next caracter in the word)
#Non determinist 
#

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
            if self.start_state is None:
                self.start_state = state
            else:
                self.start_state = state
                print("Start state updated.")
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
        if self.start_state:
            print("\nFinite State Automaton:")
            visited = set()

            def traverse(current_state, path):
                visited.add(current_state)
                if current_state in self.transitions:
                    for next_state, label in self.transitions[current_state]:
                        if next_state not in visited:
                            traverse(next_state, f"{path} --({label})--> {next_state}")
                if current_state in self.final_states:
                    print(f"Path: {path}*")
                elif current_state not in self.transitions:
                    print(f"Path: {path}")

            traverse(self.start_state, f"={self.start_state}")

            for state in self.states:
                if state not in visited:
                    if state in self.final_states:
                        print(f"Path: {state}*")
                    else:
                        print(f"Path: {state}")

        else:
            print("Start state is not set.")

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
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()