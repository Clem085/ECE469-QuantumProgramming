import classiq
# import classiq import *

# @qfunc

# def main(x: Output[QNum], y: Output[QNum]) -> None:
#     allocate(3,x)
#     hadamard_transform(x)
#     y |= x**2 + 1

    
# Check Classiq SDK version
print(f"Classiq SDK version: {classiq.__version__}")

# Ensure authentication
try:
    classiq.authenticate()
    print("Successfully authenticated with Classiq cloud.")
except Exception as e:
    print(f"Authentication error: {e}")
    exit(1)

# Define a simple quantum program using `create_model`
try:
    ghz_model = classiq.create_model(
        model_type="QuantumCircuit",  # Explicitly defining a circuit model
        data={
            "qubits": 3,
            "gates": [
                {"gate": "H", "target": [0]},
                {"gate": "CNOT", "control": [0], "target": [1]},
                {"gate": "CNOT", "control": [1], "target": [2]},
            ],
            "measurements": [{"qubit": i} for i in range(3)]
        }
        # main
    )

    synthesized_circuit = classiq.synthesize(ghz_model)
    print("Successfully synthesized a GHZ quantum circuit.")
    print(synthesized_circuit)
except Exception as e:
    print("Error synthesizing quantum circuit:")
    import traceback
    traceback.print_exc()
    exit(1)

print("Classiq environment is properly configured.")
