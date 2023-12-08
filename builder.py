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
            print("etat inexistante .")

    def add_final_state(self, state):
        if state in self.states:
            self.final_states.add(state)
        else:
            print("etet inexistante.")

    def add_transition(self, from_state, to_state, label):
        if from_state in self.states and to_state in self.states:
            if from_state not in self.transitions:
                self.transitions[from_state] = []
            self.transitions[from_state].append((to_state, label))
        else:
            print(" l'un des etates est  inexistante")

    def visualize(self):
        if not self.start_state:
            print("l'etat initial inexistante ")
            return

        print("\nl'automate:")
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
                    paths.append(f"{path} -> {current_state} --({label})-- boucle")
                else:
                    traverse(next_state, f"{path} -> {current_state} --({label})--")

        traverse(self.start_state, f"start={self.start_state}")

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
                return False, "Bloqué : Aucune transition pour le caractère actuel."

        return current_state in self.final_states, "Accepté" if current_state in self.final_states else "Rejeté : La dernière transition ne mène pas à l'état final."

def main():
    fsm = StateMachine()

    while True:
        print("\n menu:")
        print("1. ajouter etat")
        print("2.  Définir l'état initial ")
        print("3. Définir l'état final ")
        print("4. Ajouter  transition")
        print("5. Visualizer")
        print("6. Exit")
        print("7. Tester  un mot ")

        choice = input("Entrez votre choix :")

        if choice == "1":
            state = input("Entre ke nom de l'etat: ")
            fsm.add_state(state)
        elif choice == "2":
            start_state = input("Entre l'etet initial: ")
            fsm.set_start_state(start_state)
        elif choice == "3":
            final_state = input("Entre l'etet final: ")
            fsm.add_final_state(final_state)
        elif choice == "4":
            from_state = input(" De: ")
            to_state = input("Vers: ")
            label = input("le caracter: ")
            fsm.add_transition(from_state, to_state, label)
        elif choice == "5":
            fsm.visualize()
        elif choice == "7":
            test_str = input("Entre le mot a tester: ")
            accepted, message = fsm.test_string(test_str)
            print(f"Result: {'Accepté' if accepted else 'Rejecté'} - {message}")
        elif choice == "6":
            break
        else:
            print("choix Invalid . réessayer .")

if __name__ == "__main__":
    main()
