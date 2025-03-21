# This is a sample file used to test the functionality of my quantum programming environment
# # Runs Python with the qiskit Library
# import qiskit as qi

# # Create a quantum Circuit
# circuit = qi.QuantumCircuit(2, 2)

# # Apply a Hadamard Gate to the first qubit
# circuit.h(0)

# # Apply a CNOT Gate to the first and second qubit
# circuit.cx(0, 1)

# # Measure the qubits
# circuit.measure([0, 1], [0, 1])

# # Print Measurements
# print(circuit)


###########################
import numpy as np

# Import Qiskit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_state_city
import qiskit.quantum_info as qi

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
# plot_histogram(counts, title='Bell-State counts')

# Draw Circuit
# circ.draw(output='mpl') # Pretty
# circ.draw() # ASCII # Print in Juptier Notebook
print(circ) # Print in Terminal
