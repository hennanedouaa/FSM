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

# Define the main GUI application class
class FSMApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Finite State Machine Visualizer')

        # Set up the main GUI components
        self.setup_widgets()

        # Initialize attributes for the FSM
        self.states = set()
        self.start_state = None
        self.final_states = set()
        self.transitions = {}

        # Set up the FSM visualization
        self.fsm_graph = nx.DiGraph()
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=tk.BOTH, expand=True)

    def setup_widgets(self):
        # Add state section
        ttk.Label(self, text="State Name:").pack(side=tk.LEFT)
        self.state_entry = ttk.Entry(self)
        self.state_entry.pack(side=tk.LEFT)
        ttk.Button(self, text="Add State", command=self.add_state).pack(side=tk.LEFT)

        # Set start state section
        ttk.Button(self, text="Set Start State", command=self.set_start_state).pack(side=tk.LEFT)

        # Set final state section
        ttk.Button(self, text="Add Final State", command=self.add_final_state).pack(side=tk.LEFT)

        # Add transition section
        ttk.Label(self, text="From State:").pack(side=tk.LEFT)
        self.from_state_entry = ttk.Entry(self)
        self.from_state_entry.pack(side=tk.LEFT)
        ttk.Label(self, text="To State:").pack(side=tk.LEFT)
        self.to_state_entry = ttk.Entry(self)
        self.to_state_entry.pack(side=tk.LEFT)
        ttk.Label(self, text="Transition Label:").pack(side=tk.LEFT)
        self.transition_label_entry = ttk.Entry(self)
        self.transition_label_entry.pack(side=tk.LEFT)
        ttk.Button(self, text="Add Transition", command=self.add_transition).pack(side=tk.LEFT)

        # Visualize button
        ttk.Button(self, text="Visualize FSM", command=self.visualize_fsm).pack(side=tk.LEFT)

    def add_state(self):
        state = self.state_entry.get()
        if state:
            self.states.add(state)
            self.state_entry.delete(0, tk.END)
            self.update_fsm_graph()

    def set_start_state(self):
        state = self.state_entry.get()
        if state in self.states:
            self.start_state = state
            self.state_entry.delete(0, tk.END)
            self.update_fsm_graph()
        else:
            messagebox.showerror("Error", "State not found")

    def add_final_state(self):
        state = self.state_entry.get()
        if state in self.states:
            self.final_states.add(state)
            self.state_entry.delete(0, tk.END)
            self.update_fsm_graph()
        else:
            messagebox.showerror("Error", "State not found")

    def add_transition(self):
        from_state = self.from_state_entry.get()
        to_state = self.to_state_entry.get()
        label = self.transition_label_entry.get()
        if from_state in self.states and to_state in self.states:
            if from_state not in self.transitions:
                self.transitions[from_state] = []
            self.transitions[from_state].append((to_state, label))
            self.from_state_entry.delete(0, tk.END)
            self.to_state_entry.delete(0, tk.END)
            self.transition_label_entry.delete(0, tk.END)
            self.update_fsm_graph()
        else:
            messagebox.showerror("Error", "One or both states not found")

    def update_fsm_graph(self):
        # Clear the current graph and rebuild it
        self.fsm_graph.clear()

        # Add nodes and transitions to the graph
        for state in self.states:
            self.fsm_graph.add_node(state)
        for from_state, transitions in self.transitions.items():
            for to_state, label in transitions:
                self.fsm_graph.add_edge(from_state, to_state, label=label)

        # Now visualize the updated graph
        self.visualize_fsm()

    def visualize_fsm(self):
        self.ax.clear()

        # Define layout for our nodes
        pos = nx.circular_layout(self.fsm_graph)  # Circular layout for symmetry

        # Draw the nodes with a circular shape and a specific style for start and final states
        nx.draw_networkx_nodes(self.fsm_graph, pos, node_color='white', edgecolors='black', node_size=2000, ax=self.ax)

        # Highlight the start state with a distinct color
        if self.start_state:
            nx.draw_networkx_nodes(self.fsm_graph, pos, nodelist=[self.start_state], node_color='lightblue', edgecolors='black', node_size=2000, ax=self.ax)

        # Draw final states with double circles
        for final_state in self.final_states:
            nx.draw_networkx_nodes(self.fsm_graph, pos, nodelist=[final_state], node_color='white', edgecolors='black', node_size=2200, ax=self.ax)  # Outer circle for double border effect
            nx.draw_networkx_nodes(self.fsm_graph, pos, nodelist=[final_state], node_color='white', edgecolors='black', node_size=2000, ax=self_ax)  # Inner circle

        # Draw the edges with arrows, ensuring they are very visible
        normal_edges = [(u, v) for u, v in self.fsm_graph.edges() if u != v]
        nx.draw_networkx_edges(self.fsm_graph, pos, edgelist=normal_edges, ax=self.ax, arrows=True, arrowstyle='-|>', arrowsize=15, width=2)

        # Modify edge labels to include direction indicator
        edge_labels = {edge: data.get('label', 'eps') for edge, data in self.fsm_graph.edges.items()}
        # Adjust labels for normal edges
        for edge in normal_edges:
            edge_labels[edge] = f">{edge_labels[edge]}>"

        # Handle loop edges (self-transitions) separately to make them more obvious
        loop_edges = [(u, v) for u, v in self.fsm_graph.edges() if u == v]
        for loop_edge in loop_edges:
            # Adjust the loop size
            nx.draw_networkx_edges(
                self.fsm_graph, pos, edgelist=[loop_edge], ax=self.ax,
                connectionstyle=f'arc3,rad={0.1 + 0.1 * loop_edges.index(loop_edge)}',
                arrows=True, arrowstyle='-|>', arrowsize=15, width=2
            )
            # Place the label above the loop
            label_pos = pos[loop_edge[0]][0], pos[loop_edge[0]][1] + 0.1
            self.ax.text(label_pos[0], label_pos[1], f">{edge_labels[loop_edge]}>", size=10, ha='center', va='center')

        # Draw non-loop edge labels
        nx.draw_networkx_edge_labels(self.fsm_graph, pos, edge_labels=edge_labels, ax=self.ax, font_size=10)

        # Label the nodes with their names
        nx.draw_networkx_labels(self.fsm_graph, pos, ax=self.ax, font_size=10)

        # Remove axes
        self.ax.axis('off')

        # Update the canvas
        self.canvas.draw()


    def run(self):
        self.mainloop()

# Create and run the FSM application
app = FSMApp()
app.run()
