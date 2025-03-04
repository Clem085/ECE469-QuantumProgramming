# Setting Up Classiq on Arch Linux

## Table of Contents
1. [Introduction](#introduction)
2. [Installation Steps](#installation-steps)
3. [Virtual Environment Setup](#virtual-environment-setup)
4. [Classiq SDK Installation](#classiq-sdk-installation)
5. [Verifying the Setup](#verifying-the-setup)
6. [Switching Between Environments](#switching-between-environments)
7. [Conclusion](#conclusion)

## Introduction
Classiq is a quantum software development platform that requires a specific Python environment. This guide ensures that the correct version of Python is installed and a dedicated virtual environment is created to avoid conflicts with other quantum computing tools like Qiskit.

## Installation Steps

### Step 1: Navigate to the Desired Directory
```bash
cd ~/QuantumComputing/Classiq_Env/
```

### Step 2: Install Python 3.12
```bash
yay -S python312
```

### Step 3: Verify Python Installation
```bash
python3.12 -c 'print("Hello World")'
```

## Virtual Environment Setup

### Step 4: Create a Virtual Environment
```bash
python3.12 -m venv classiq-venv
```

### Step 5: Activate the Virtual Environment
```bash
source ~/QuantumComputing/Classiq_Env/classiq-venv/bin/activate
```

## Classiq SDK Installation

### Step 6: Upgrade `pip` and Install Classiq SDK
```bash
pip install --upgrade pip
pip install -U classiq
```

### Step 7: Verify the Installation
```bash
python -c "import classiq; print(classiq.__version__)"
```

## Switching Between Environments

### To activate the Classiq environment:
```bash
source ~/QuantumComputing/Classiq_Env/classiq-venv/bin/activate
```

### To return to your Qiskit environment:
```bash
source ~/QuantumComputing/QuantumFiles/.venv/bin/activate
```

### To deactivate any active environment:
```bash
deactivate
```

## Conclusion
This guide provided step-by-step instructions to install Python 3.12, set up a virtual environment, and install the Classiq SDK on Arch Linux. By keeping Classiq in a separate virtual environment, you can avoid conflicts with other quantum computing tools like Qiskit.

Now you're ready to start developing with Classiq!
