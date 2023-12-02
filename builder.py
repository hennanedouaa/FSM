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
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx

class FSMApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Finite State Machine Visualizer')
        self.geometry('800x600')

        self.setup_widgets()

        self.states = set()
        self.start_state = None
        self.final_states = set()
        self.transitions = {}

        self.fsm_graph = nx.MultiDiGraph()
        self.figure, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=tk.BOTH, expand=True)

    def setup_widgets(self):
        top_frame = ttk.Frame(self)
        top_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        ttk.Label(top_frame, text="State:").pack(side=tk.LEFT)
        self.state_entry = ttk.Entry(top_frame)
        self.state_entry.pack(side=tk.LEFT, padx=5)
        add_state_button = ttk.Button(top_frame, text="Add State", command=self.add_state)
        add_state_button.pack(side=tk.LEFT, padx=5)

        ttk.Label(top_frame, text="Start State:").pack(side=tk.LEFT)
        self.start_state_entry = ttk.Entry(top_frame)
        self.start_state_entry.pack(side=tk.LEFT, padx=5)
        set_start_button = ttk.Button(top_frame, text="Set Start", command=self.set_start_state)
        set_start_button.pack(side=tk.LEFT, padx=5)

        ttk.Label(top_frame, text="Final State:").pack(side=tk.LEFT)
        self.final_state_entry = ttk.Entry(top_frame)
        self.final_state_entry.pack(side=tk.LEFT, padx=5)
        add_final_state_button = ttk.Button(top_frame, text="Add Final", command=self.add_final_state)
        add_final_state_button.pack(side=tk.LEFT, padx=5)

        bottom_frame = ttk.Frame(self)
        bottom_frame.pack(side=tk.TOP, fill=tk.X, padx=10)

        ttk.Label(bottom_frame, text="From State:").pack(side=tk.LEFT)
        self.from_state_entry = ttk.Entry(bottom_frame)
        self.from_state_entry.pack(side=tk.LEFT, padx=5)
        ttk.Label(bottom_frame, text="To State:").pack(side=tk.LEFT)
        self.to_state_entry = ttk.Entry(bottom_frame)
        self.to_state_entry.pack(side=tk.LEFT, padx=5)
        ttk.Label(bottom_frame, text="Transition Label:").pack(side=tk.LEFT)
        self.transition_label_entry = ttk.Entry(bottom_frame)
        self.transition_label_entry.pack(side=tk.LEFT, padx=5)
        add_transition_button = ttk.Button(bottom_frame, text="Add Transition", command=self.add_transition)
        add_transition_button.pack(side=tk.LEFT, padx=5)

        visualize_button = ttk.Button(self, text="Visualize", command=self.visualize_fsm)
        visualize_button.pack(side=tk.BOTTOM, pady=10)

    def add_state(self):
        state = self.state_entry.get()
        if state and state not in self.states:
            self.states.add(state)
            self.state_entry.delete(0, tk.END)
            self.update_fsm_visualization()

    def set_start_state(self):
        state = self.start_state_entry.get()
        if state in self.states:
            self.start_state = state
            self.start_state_entry.delete(0, tk.END)
            self.update_fsm_visualization()

    def add_final_state(self):
        state = self.final_state_entry.get()
        if state in self.states:
            self.final_states.add(state)
            self.final_state_entry.delete(0, tk.END)
            self.update_fsm_visualization()

    def add_transition(self):
        from_state = self.from_state_entry.get()
        to_state = self.to_state_entry.get()
        label = self.transition_label_entry.get()
        if from_state in self.states and to_state in self.states:
            self.transitions[(from_state, to_state)] = label
            self.from_state_entry.delete(0, tk.END)
            self.to_state_entry.delete(0, tk.END)
            self.transition_label_entry.delete(0, tk.END)
            self.update_fsm_visualization()

    def visualize_fsm(self):
        self.fsm_graph.clear()
        self.ax.clear()

        for state in self.states:
            self.fsm_graph.add_node(state)
        for (from_state, to_state), label in self.transitions.items():
            style = 'arc3,rad=0.2' if from_state == to_state else ''
            self.fsm_graph.add_edge(from_state, to_state, label=label, connectionstyle=style)

        pos = nx.spring_layout(self.fsm_graph)
        nx.draw_networkx_nodes(self.fsm_graph, pos, node_size=3000, node_color='white', edgecolors='black')
        nx.draw_networkx_labels(self.fsm_graph, pos)

        if self.start_state:
            nx.draw_networkx_nodes(self.fsm_graph, pos, nodelist=[self.start_state], node_size=3000, node_color='yellow', edgecolors='black')
        for final_state in self.final_states:
            nx.draw_networkx_nodes(self.fsm_graph, pos, nodelist=[final_state], node_size=3000, node_color='pink', edgecolors='black')

        nx.draw_networkx_edges(self.fsm_graph, pos, edge_color='black', arrowstyle='->', arrowsize=20, connectionstyle='arc3,rad=0.1')
        edge_labels = nx.get_edge_attributes(self.fsm_graph, 'label')
        if edge_labels:
            nx.draw_networkx_edge_labels(self.fsm_graph, pos, edge_labels=edge_labels, label_pos=0.5)

        plt.axis('off')
        self.figure.tight_layout()
        self.canvas.draw()

    def update_fsm_visualization(self):
        self.visualize_fsm()

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = FSMApp()
    app.run()
