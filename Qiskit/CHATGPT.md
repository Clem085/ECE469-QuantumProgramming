# ECE469-QuantumProgramming

This repository contains all of the code for my Quantum Programming class: ECE 469. Everything is programmed in Python using the Qiskit quantum library.

---

# Setting Up Qiskit on WSL Arch Linux

This document outlines the steps and intricacies involved in setting up Qiskit on a WSL Arch Linux installation.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Why this Configuration?](#why-this-configuration)
3. [Prerequisites](#prerequisites)
4. [Installing WSL Arch Linux](#installing-wsl-arch-linux)
5. [Installation Steps](#installation-steps)
6. [Troubleshooting](#troubleshooting)
7. [Notes and Tips](#notes-and-tips)
8. [Conclusion](#conclusion)
9. [References](#references)

---

## Introduction

Qiskit is a Python library created by IBM, designed to simulate quantum computer systems and circuits. I run Arch Linux via the Windows Subsystem for Linux (WSL) on my Windows 11 machine. WSL allows me to interact with remote GitHub repositories and work on most of my programming projects. Setting up Qiskit on WSL Arch Linux requires specific steps, as Python and pip services must be installed differently. To manage the installation, I created a Python virtual environment to locally install all libraries through pip. Below is the entire process.

---

## Why this Configuration?

There are many different reasons I chose each component of this configuration. In the subsections below, I summarize my reasoning. This is not the only way, and it might not be the best way for most people. I enjoy a challenge and tend to overcomplicate things. This solution may not be optimal, but it works perfectly for me. If you're questioning my sanity... you probably should. Hopefully, this tutorial gives you the tools and resources needed to replicate my setup.

### Why Arch?

Honestly, part of it is just to be able to say "I use Arch, BTW." Arch is not for everyone. The most accessible WSL install will be Ubuntu, which has extensive documentation. Choosing Arch means facing issues others won’t. Arch isn’t hard, but the learning curve is steep. Fortunately, with help from the Arch Wiki, ChatGPT, and some technical knowledge, anyone can succeed.

### Why WSL?

Git. I use WSL because I prefer using SSH keys to access my remote GitHub repositories, which is easier in a Linux environment. WSL is slower than a native Linux installation—dual booting would be faster. Some commands take a while to run. Be patient. Your computer isn’t frozen; it’s just working hard.

---

## Prerequisites

Make sure you have the following before starting:

* A Windows 11 machine
* Administrator access to install WSL
* Basic terminal familiarity
* Internet connection

---

## Installing WSL Arch Linux

To install Arch Linux on WSL without using the Microsoft Store, follow these steps:

### Step 1: Enable WSL and Virtual Machine Platform

Open Command Prompt as Administrator:

```powershell
wsl --install --no-distribution
wsl --set-default-version 2
```

Reboot Computer to allow changes to take effect.

### Step 2: Download Arch WSL Root Filesystem

Download the Arch Linux WSL tarball:

```bash
curl -LO https://github.com/yuk7/ArchWSL/releases/download/20240311.0/Arch.tar.gz
```

### Step 3: Install Arch WSL Manually

Create a folder for Arch and extract:

```powershell
mkdir C:\WSL\Arch
cd C:\WSL\Arch
wsl --import ArchLinux C:\WSL\Arch .\Arch.tar.gz --version 2
```

### Step 4: Launch Arch WSL

```powershell
wsl -d ArchLinux
```

You’re now in your Arch shell.

---

## Installation Steps

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

### Step 3: Install Qiskit and Tools

Install the following Python libraries one at a time:

```bash
pip install qiskit
pip install qiskit-aer
pip install qiskit-optimization
pip install matplotlib
pip install pylatexenc
pip install numpy
pip install colorcet
```

### Step 4: Verify Installation

```bash
python -c "import qiskit; print(qiskit.__qiskit_version__)"
```

### Step 5: Set Up GitHub Repository

Create a GitHub repository, then link it locally:

```bash
git init
git remote add origin git@github.com:your_username/your_repo.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

If there's a history conflict:

```bash
git pull --allow-unrelated-histories origin main
```

---

## Troubleshooting

* **Error:** `ModuleNotFoundError: No module named 'qiskit'`

  * **Fix:** Make sure your virtual environment is activated.

* **Error:** Dependency conflicts

  * **Fix:** Upgrade pip: `pip install --upgrade pip`

---

## Notes and Tips

* Always activate your virtual environment before running any Qiskit code
* Recommended resource: [https://qiskit.org/documentation/](https://qiskit.org/documentation/)
* Use `deactivate` to exit the Python virtual environment

---

## Conclusion

This guide provides a step-by-step approach to installing and using Qiskit on WSL Arch Linux using terminal commands. It should serve both as documentation for others and a reference for future setups.

---

## References

* [Arch Wiki](https://wiki.archlinux.org)
* [WSL Documentation](https://learn.microsoft.com/en-us/windows/wsl/)
* [Qiskit Installation Guide](https://qiskit.org/documentation/getting_started.html)
* [ArchWSL GitHub](https://github.com/yuk7/ArchWSL)
