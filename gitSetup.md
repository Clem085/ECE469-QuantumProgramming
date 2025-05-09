# GitHub SSH Setup with Ed25519 on Ubuntu Linux

This document outlines the steps to set up GitHub SSH authentication using the Ed25519 key algorithm on Ubuntu Linux, clone a remote repository, and initialize a local project directory with a `.gitignore` file tailored for C++ projects.

---

## Table of Contents
1. [Generate SSH Key](#generate-ssh-key)
2. [Add SSH Key to GitHub](#add-ssh-key-to-github)
3. [Verify SSH Connection](#verify-ssh-connection)
4. [Set Up Local Repository](#set-up-local-repository)
5. [Clone Remote Repository](#clone-remote-repository)
6. [Create `.gitignore` for C++](#create-gitignore-for-c)
7. [Commit and Push Changes](#commit-and-push-changes)

---

## Generate SSH Key
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
When prompted, save the key in `~/.ssh/id_ed25519` and set a secure passphrase.

## Add SSH Key to GitHub
```bash
cat ~/.ssh/id_ed25519.pub
```
Copy the output and add it to your GitHub SSH keys at:
[GitHub SSH Settings](https://github.com/settings/keys)

## Verify SSH Connection
```bash
ssh -T git@github.com
```
If successful, you should see a message welcoming you to GitHub.

---

## Set Up Local Repository
### Create Project Directory and Initialize Git
```bash
mkdir -p ~/local_Dir
cd ~/local_Dir

git init
```

## Clone Remote Repository
```bash
git clone git@github.com:your-username/your-repository.git ~/local_Dir
cd ~/local_Dir
```

---

## Create `.gitignore` for C++
Create a `.gitignore` file with common C++ exclusions:
```bash
echo "# C++ .gitignore
*.o
*.obj
*.exe
*.out
*.a
*.lib
*.so
*.dll
*.dSYM/
.vscode/
.idea/
*.swp
*.swo
build/
debug/
release/
" > .gitignore
```

## Commit and Push Changes
```bash
git add .gitignore
git commit -m "Added C++ .gitignore file"
git push origin main
```

---

Your GitHub SSH authentication is now set up, and your local repository is initialized and linked with the remote repository. You’re ready to start coding! 🚀
