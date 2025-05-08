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

I use Garuda Linux, an Arch based distro as the primary OS on one of my laptops. Using the Arch flavor of WSL helps to ensure compantiblity between my devices. Another plus is being able to say "I use Arch, BTW." Arch is not for everyone. The most accessible WSL distrobution will be Ubuntu, which has extensive documentation. Choosing Arch means facing issues others won’t. Arch isn’t hard, but the learning curve is steep. Fortunately, with help from the Arch Wiki, ChatGPT, and some technical knowledge, anyone can succeed.

### Why WSL?

Git. I use WSL because I prefer using SSH keys to access my remote GitHub repositories, which is easier in a Linux environment. WSL is slower than a native Linux installation, and dual-booting Linux would be faster. Some commands take a while to run. Be patient. Your computer isn’t frozen; it’s just working hard. I chose WSL over dual-booting because swapping OSs every time I need to write some Python code takes too long when I have to use Windows for many of my other courses.

---

## Prerequisites

Make sure you have the following before starting:

* A Windows 10/11 machine
* Administrator access
* Basic terminal familiarity
* Internet connection

---

## Installing WSL Arch Linux

As of 2025, you can install Arch Linux directly through WSL using a single command. This is the easiest and most reliable method.

### Step 1: Open Command Prompt as Administrator

* Press the **Windows** key
* Type `cmd`
* Right-click **Command Prompt** and choose **Run as administrator**

### Step 2: Enable WSL and Set Version 2 as Default

In the Command Prompt window:

```cmd
wsl --install
```

```cmd
wsl --set-default-version 2
```

**Important:** You must reboot your system after running these commands, even if you are not prompted.

### Step 3: Install Arch Linux

After rebooting, open Command Prompt again
* Press the **Windows** key
* Type `cmd`
* Press the **Enter** key
```cmd
wsl --install -d Arch
```

This command will download and install the official Arch Linux image configured for WSL.

### Step 4: Launch Arch Linux

Once installation is complete:

```cmd
wsl -d Arch
```

You’re now in your Arch shell.

To make it easier to activate your Qiskit environment, add the following alias to your `~/.bashrc` file:

```bash
echo 'alias qiskit="cd ~/QuantumComputing/Qiskit && source ~/QuantumComputing/Qiskit/.venv/bin/activate"' >> ~/.bashrc
```

Then, reload your shell:

```bash
source ~/.bashrc
```

Now, you can simply run `qiskit` to jump into your environment.

---

## Python & Qiskit Installation Steps

### Step 1: Update System and Install Dependencies

```bash
sudo pacman -Syu
```

```bash
sudo pacman -S python python-pip
```

### Step 2: Set Up a Python Virtual Environment

```bash
python -m venv qiskit_env
```

```bash
source qiskit_env/bin/activate
```

### Step 3: Install Qiskit and Tools

Install all required Python libraries using a single command:

```bash
pip install qiskit qiskit-aer qiskit-optimization matplotlib pylatexenc numpy colorcet
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

This guide provides a step-by-step approach to installing and using Qiskit on WSL Arch Linux using Command Prompt. It should serve both as documentation for others and a reference for future setups.

---

## References

* [Arch Wiki](https://wiki.archlinux.org)
* [WSL Documentation](https://learn.microsoft.com/en-us/windows/wsl/)
* [Qiskit Installation Guide](https://qiskit.org/documentation/getting_started.html)
* [ArchWSL GitHub](https://github.com/yuk7/ArchWSL)
