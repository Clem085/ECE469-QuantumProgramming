# In Class Assignment 1-24-25
from qiskit import *
from qiskit import visualization
from qiskit_aer import AerSimulator

# Create circuit
circ = QuantumCircuit(2)
circ.h(0)
circ.cx(0, 1)
circ.measure_all()

# Transpile for simulator
simulator = AerSimulator()
circ = transpile(circ, simulator)

# Run and get counts
result = simulator.run(circ).result()
counts = result.get_counts(circ)
visualization.plot_histogram(counts, title='Bell-State counts')

# Draw Circuit # Doesn't seem to work currently
circ.draw(output='mpl') # Pretty
# circ.draw() # ASCII

# print(circ)