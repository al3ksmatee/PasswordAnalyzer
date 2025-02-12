# Password Analyzer 🔐

## 📌 Overview
The **Password Analyzer** is a cybersecurity tool designed to **analyze password security** by checking if a given password hash exists in common wordlists. It helps security professionals and penetration testers evaluate password strength by leveraging **SHA-256 hashing**, **wordlist attacks**, and integration with popular tools like **John the Ripper** and **Hashcat**.

## 🚀 Features
- **Generate and analyze SHA-256 hashes**
- **Check passwords against common wordlists** (e.g., RockYou)
- **Automate password cracking attempts** using John the Ripper & Hashcat
- **Supports dictionary attacks & brute-force attacks**
- **Flexible and easy-to-use command-line interface (CLI)**

## 🛠 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/al3ksmatee/PasswordAnalyzer.git
cd PasswordAnalyzer
```

### 2️⃣ Install Dependencies
Ensure you have Python installed (**Python 3.x recommended**). Install required dependencies:
```bash
pip install -r requirements.txt
```

For Hashcat and John the Ripper, install them if they are not already installed:
```bash
# Install John the Ripper (Linux)
sudo apt install john

# Install Hashcat (Linux)
sudo apt install hashcat
```

## 🔍 Usage
### 1️⃣ Hash a Password
To generate a SHA-256 hash from a password:
```bash
python password_analyzer.py --hash "yourpassword"
```

### 2️⃣ Crack a Hash Using a Wordlist
To check if a given hash is found in a wordlist (**RockYou** in this example):
```bash
python password_analyzer.py --check hashfile.txt --wordlist /usr/share/wordlists/rockyou.txt
```

### 3️⃣ Crack a Hash Using John the Ripper
```bash
john --format=raw-sha256 --wordlist=/usr/share/wordlists/rockyou.txt hashfile.txt
```

### 4️⃣ Crack a Hash Using Hashcat
```bash
hashcat -m 1400 hashfile.txt /usr/share/wordlists/rockyou.txt
```

### 5️⃣ Brute-force Attack with Hashcat
If wordlists fail, try brute-force:
```bash
hashcat -m 1400 -a 3 hashfile.txt ?a?a?a?a?a?a?a?a
```
This tries **all combinations** of 8-character passwords.

## ⚙️ Configuration
Modify **password_analyzer.py** to customize:
- **Hash type** (default: SHA-256)
- **Wordlist path**
- **Attack mode** (Dictionary vs. Brute-force)

## 🔥 Troubleshooting
### 🛑 "Command not found" Errors
Ensure **John the Ripper** or **Hashcat** is installed:
```bash
which john  # Should return a path
which hashcat  # Should return a path
```
If missing, install them as mentioned in the **Installation** section.

### 🛑 Hashcat Fails Due to Outdated Drivers
Check GPU drivers:
```bash
hashcat -I  # List available GPUs
```
If the error persists, update your drivers:
- **NVIDIA**: `sudo apt install nvidia-driver`
- **AMD**: `sudo apt install amdgpu-pro`

### 🛑 RockYou Wordlist Not Found
On Kali Linux, the RockYou wordlist is located at:
```bash
/usr/share/wordlists/rockyou.txt.gz
```
Unzip it if necessary:
```bash
gunzip /usr/share/wordlists/rockyou.txt.gz
```
## 📜 License
This project is licensed under the **MIT License**.

---
🚀 **Developed by [al3ksmatee](https://github.com/al3ksmatee)** | 🌍 **Stay safe in cyberspace!**

