#les boucles 
#Deterministe 
# cases accepted : - the chars of the word takes us from S0 and finishes at Sf (one transition at each character and
#we can pass by Sf before it's ending what's important is that the last transition ( character take sus to Sf )
# refused : 1- the last transition (character) doesn't take us to Sf 
#2- we are blocked at a state and can't move ( becausethe state doesn't have a tranistion (coming out of the state )that is laeled as the next caracter in the word)
#Non determinist 
# Import the necessary libraries
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx

class FSMApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Finite State Machine Visualizer')
        self.geometry('800x600')  # Set initial size of the window

        self.setup_widgets()

        self.states = set()
        self.start_state = None
        self.final_states = set()
        self.transitions = {}

        self.fsm_graph = nx.DiGraph()
        self.figure, self.ax = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def setup_widgets(self):
        top_frame = ttk.Frame(self)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        self.state_entry = ttk.Entry(top_frame)
        self.state_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

        add_button = ttk.Button(top_frame, text="Add", command=self.add_state)
        add_button.pack(side=tk.LEFT, padx=5, pady=5)

        set_start_button = ttk.Button(top_frame, text="Set Start", command=self.set_start_state)
        set_start_button.pack(side=tk.LEFT, padx=5, pady=5)

        set_final_button = ttk.Button(top_frame, text="Set Final", command=self.add_final_state)
        set_final_button.pack(side=tk.LEFT, padx=5, pady=5)

        middle_frame = ttk.Frame(self)
        middle_frame.pack(side=tk.TOP, fill=tk.X)

        self.from_state_entry = ttk.Entry(middle_frame, width=10)
        self.from_state_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

        self.to_state_entry = ttk.Entry(middle_frame, width=10)
        self.to_state_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

        self.transition_label_entry = ttk.Entry(middle_frame, width=10)
        self.transition_label_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

        add_transition_button = ttk.Button(middle_frame, text="Add Transition", command=self.add_transition)
        add_transition_button.pack(side=tk.LEFT, padx=5, pady=5)

        bottom_frame = ttk.Frame(self)
        bottom_frame.pack(side=tk.TOP, fill=tk.X)

        visualize_button = ttk.Button(bottom_frame, text="Visualize", command=self.visualize_fsm)
        visualize_button.pack(pady=5)

    def add_state(self):
        state = self.state_entry.get()
        if state:
            self.states.add(state)
            self.state_entry.delete(0, tk.END)
            self.update_fsm_visualization()

    def set_start_state(self):
        state = self.state_entry.get()
        if state in self.states:
            self.start_state = state

    def add_final_state(self):
        state = self.state_entry.get()
        if state in self.states:
            self.final_states.add(state)

    def add_transition(self):
        from_state = self.from_state_entry.get()
        to_state = self.to_state_entry.get()
        label = self.transition_label_entry.get()
        if from_state and to_state and label:
            self.transitions[(from_state, to_state)] = label
            self.from_state_entry.delete(0, tk.END)
            self.to_state_entry.delete(0, tk.END)
            self.transition_label_entry.delete(0, tk.END)

    def visualize_fsm(self):
        # Add visualization logic here
        pass

    def update_fsm_visualization(self):
        # Update FSM visualization logic here
        pass

    def run(self):
        self.mainloop()

app = FSMApp()
app.run()
