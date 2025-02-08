<!-- This entire document is deprecated and only left for archiving purposes. Please refer the README.md -->


<!-- # Setting Up Qiskit on WSL Arch Linux

This document outlines the steps and intricacies involved in setting up Qiskit on a WSL Arch Linux installation.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Installation Steps](#installation-steps)
4. [Troubleshooting](#troubleshooting)
5. [Notes and Tips](#notes-and-tips)
6. [Conclusion](#conclusion)

---

## Introduction
Qiskit is a Python library created by IBM, designed to simulate quantum computer systems and circuits. I run Arch Linux via the Windows Subsystem for Linux (WSL) on my Windows 11 machine. WSL allows me to interact with remote GitHub repositories and work on most of my programming projects. Setting up Qiskit on WSL Arch Linux requires specific steps, as Python and pip services must be installed differently. To manage the installation, I created a Python virtual environment to locally install all libraries through pip. Below you will find the entire process.

---

## Why this Configuration?
There are many different reasons I chose each component of this configuration. In the subsections below, I do my best to summarize my reasoning. This is NOT the only way. This might not be the best way for most people. I love a challenge. I over complicate everything I do. This soltuion is not optimal, but it was the perfect solution for me. If you're currently questioning my sansity... you should. But hopefully this tutorial will give you all the tools and resources you need to accomplish a setup identical to mine. 

### Why Arch?
Of course the main reason to choose Arch is so that you can say "I use Arch BTW." Arch is not for everyone. The most accessible WSL Install will be Ubuntu, where there is LOTS of documentation. When you choose Arch, you choose to face issues that other people won't. Arch is not hard, but the learning curve is steep. Things work differently on Arch. Thankfully, with the help of Arch Wiki, Chat GPT, and a little bit of technical knowledge, anyone can successfully set this up.

### Why WSL?
Git. I use WSL because I prefer the use SSH Keys to access my remote github repositories. This is easiet to do in a lnux environemtn. WSL is slow. Running Linux via dual boot is way faster. Sometimes, it will take a while for some commands to be completed. Have patactice. Your computer isn't frozen, its just working really hard to complete the commands you requested. 

## Prerequisites
List all the requirements and tools needed before starting the installation process. For example:
<!-- - WSL with Arch Linux installed -->
<!-- - Python version (e.g., Python 3.8 or higher) -->
<!-- - pip package manager -->
<!-- - Internet connection -->
---
## Open Environment in Arch WSL
### Open Command Line, Move to Correct Directory, and Enter Arch WSL
```bash
WSL
cd /mnt/c/Users/consa/Downloads/Programming/Python/QuantumComputing/Sandbox
```

### Open Virutal Environment (VENV)
```bash
source /mnt/c/Users/consa/Downloads/Programming/Python/QuantumComputing/.venv/bin/activate
```
### Open VS Code from Terminal
```bash
code .
```




---
## Installation Process
### Arch WSL Installation

### Python Installation

### PIP Installation

### Python Virtual Environment Setup
I followed this tutorial to setup my virtual environment. This link can provide more context, but simply following the commands I have listed below. 
https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

```bash
cd /path/to/development/directory`
python3 -m venv .venv`
source .venv/bin/activate`
```

### PIP Library Installations
Install the following python libraies by running each command ONE at a time. Please let each command complete before entering the next command.
```bash
python3 -m pip install qiskit
python3 -m pip install qiskit-aer
python3 -m pip install matplotlib
python3 -m pip install pylatexenc
python3 -m pip install numpy
python3 -m pip install colorcet
```

### Git Repository Setup
Source Link: https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github
First, create a reomte github repo using github online GUI. 



### Step 1: Update System and Install Dependencies
```bash
sudo pacman -Syu
sudo pacman -S python python-pip
```

### Step 2: Set Up a Python Virtual Environment
```bash
python -m venv qiskit_env
source qiskit_env/bin/activate
```

### Step 3: Install Qiskit
```bash
pip install qiskit
```

### Step 4: Verify Installation
```bash
python -c "import qiskit; print(qiskit.__qiskit_version__)"
```

---

## Troubleshooting
Document any issues you faced and how you resolved them. For instance:

- **Error:** `ModuleNotFoundError: No module named 'qiskit'`
  - **Solution:** Ensure the virtual environment is activated before running the command.

- **Error:** Dependency conflicts during installation
  - **Solution:** Use `pip install --upgrade pip` to upgrade pip.

---

## Notes and Tips
Include any additional notes or tips, such as:
- Recommended resources for learning Qiskit
- Useful commands for managing virtual environments
- Links to official documentation

---

## Conclusion
Summarize the key takeaways from the setup process. Mention how this documentation can help others or serve as a personal reference for the future.

---

## References
List any links to online guides, forums, or documentation that helped you during the setup process. -->
