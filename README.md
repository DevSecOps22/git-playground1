# 🚀 DevOps Bar-Ilan


## 📌 Features

- **Install Git & Docker Script**

---

## Table of content

- [🚀 DevOps Bar-Ilan](#-devops-bar-ilan)
    - [📌 Pre-Requirements](#-pre-requirements)
      - [Mac OS](#-Mac-OS)
      - [Linux OS](#linux-os)
      - [Windows OS](#windows)
  - [🛠 Installation \& Usage](#-installation--usage)
    - [Follow the Instruaction of file lab-instructions.md](./lab-instructions.md)
  - [🧩 Use Cases](#-use-cases)
  - [🙌 Contributions](#-contributions)

---

## 📁 Repository Structure

```text
git-playground1
├── README.md
├── install-git-and-docker.ps1
└── lab-instructions.md
```

---

## 📌 Pre-Requirements

- Install Git package

### Mac / Linux

#### Mac OS

#### Install homebrew package manager
- 1️⃣ Install Homebrew 

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- 2️⃣ Add Homebrew to PATH
  - You can add it into the ~/.zshrc or ~/.bashrc file 
```bash
eval "$(/opt/homebrew/bin/brew shellenv)"
export PATH="/opt/homebrew/bin:$PATH"
```

- 3️⃣ Verify Installation
```bash
brew --version
```

- Expected output (example):
```bash
Homebrew 4.x.x
```

#### Install Git
- Now, after you install the package manager, you can install the git tool.
```bash
brew install git
```

#### Linux OS

- Install git package
```bash
apt-get update
apt install git
```
---

### Windows

- You can download the Git specific from the browser, or with the @Aviel-Amitay script

####
- Download from Internet
```url
https://git-scm.com/install/windows
```
#### Install the latest PowerShell

```powershell
winget install --id Microsoft.PowerShell --source winget
```

#### ▶️ How to Run the Script (Required)

- Download a PoweShell script for the installation of Git and Docker packages.

```powershell
wget -Uri "https://raw.githubusercontent.com/Aviel-Amitay/docker-dev-desktop-vnc/main/install-git-and-docker.ps1" -OutFile "install-git-and-docker.ps1"
```

- Run this command as Administrator for allow explicitly using PowerShell with execution bypass enabled for this file:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install-git-and-docker.ps1
```

#### What I have include in the script

- Script will check if you have currently install Git or Docker.
  If you have onw of the package, it will print the package version.
- Install silent the default configuration.
- Check if you have a diffrente IDE, and ask prompt if you want to change, for example: PyCharm, VS Code, etc.
- If the script detect that you have an old version will offer if you want to upgarde the package.

---
## 🛠 Installation & Usage

- [Follow the Instruaction of file lab-instructions.md](./lab-instructions.md)

---

## 🙌 Contributions

PRs, issues, and suggestions are welcome!

- Open a new branch

```bash
git checkout -b <branch-name>
```

- After complete the. changes, switch back into the main branch
```bash
git switch main
```

- Merge your changes with the main branch
```bash
git merge <Your-Branch-name>
```

- Open the GitHub on the browser, and open a new Pull Request (PR)
```url
https://github.com/DevSecOps22/git-playground1/pulls
```