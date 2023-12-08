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
            print("Etat inexistante.")

    def add_final_state(self, state):
        if state in self.states:
            self.final_states.add(state)
        else:
            print("Etat inexistante.")

    def add_transition(self, from_state, to_state, label):
        if from_state in self.states and to_state in self.states:
            if from_state not in self.transitions:
                self.transitions[from_state] = []
            self.transitions[from_state].append((to_state, label))
        else:
            print("L'un des etats est inexistante")

    def visualize(self):
        if not self.start_state:
            print("L'etat initial inexistante")
            return

        print("\nL'automate:")
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

    def test_string_nd(self, test_str):
        stack = [(self.start_state, 0, [])]

        while stack:
            current_state, pos, path = stack.pop()

            if pos == len(test_str):
                if current_state in self.final_states:
                    return True, "Accepté", path
                continue

            if current_state in self.transitions:
                char = test_str[pos]
                for to_state, label in self.transitions[current_state]:
                    if label == char:
                        stack.append((to_state, pos + 1, path + [f"{current_state} --({label})--> {to_state}"]))

        return False, "Rejeté : Aucun chemin valide trouvé", path

def main():
    fsm = StateMachine()

    while True:
        print("\nMenu:")
        print("1. Ajouter etat")
        print("2. Définir l'état initial")
        print("3. Définir l'état final")
        print("4. Ajouter transition")
        print("5. Visualizer")
        print("6. Exit")
        print("7. Tester un mot")

        choice = input("Entrez votre choix: ")

        if choice == "1":
            state = input("Entrez le nom de l'etat: ")
            fsm.add_state(state)
        elif choice == "2":
            start_state = input("Entrez l'etat initial: ")
            fsm.set_start_state(start_state)
        elif choice == "3":
            final_state = input("Entrez l'etat final: ")
            fsm.add_final_state(final_state)
        elif choice == "4":
            from_state = input("De: ")
            to_state = input("Vers: ")
            label = input("Le caractere: ")
            fsm.add_transition(from_state, to_state, label)
        elif choice == "5":
            fsm.visualize()
        elif choice == "7":
            test_str = input("Entrez le mot a tester: ")
            accepted, message, path = fsm.test_string_nd(test_str)
            print(f"Resultat: {'Accepté' if accepted else 'Rejeté'} - {message}")
            if accepted:
                print("Chemin:", " -> ".join(path))
        elif choice == "6":
            break
        else:
            print("Choix invalide. Reessayez.")

if __name__ == "__main__":
    main()
