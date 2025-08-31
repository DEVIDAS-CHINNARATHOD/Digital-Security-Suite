# Digital Security Suite

**Digital Security Suite: Keylogger Guard, PassGuard, PhishNet & SecureVault**  
A comprehensive set of cybersecurity tools designed to educate users and provide practical solutions for common digital threats. This suite includes tools for keylogger detection, password analysis, phishing detection, and data encryption/decryption. The goal is to provide both educational value and practical utility in a single platform.

---

## **Sub-Projects / Modules**

### 1️⃣ **Keylogger Guard**
- **Purpose:** Detect, demonstrate, and deactivate keyloggers safely.  
- **Description:** Keylogger Guard allows users to safely simulate a keylogger for educational purposes, detect potentially malicious keylogger processes running on their system, and deactivate them if necessary. Works across **Windows, Linux, and macOS**.  
- **Features:**  
  - Safe demo keylogger for controlled testing  
  - Detect suspicious processes monitoring keyboard input  
  - Deactivate or terminate detected keylogger processes  
  - Display detection reports  
- **Folder:** `KeyloggerGuard/`  

### 2️⃣ **PassGuard**
- **Purpose:** Check password strength and detect if passwords have been leaked.  
- **Description:** PassGuard helps users create strong passwords and checks whether existing passwords have been compromised in known data breaches. Provides real-time feedback and suggestions for improving password security.  
- **Features:**  
  - Real-time password strength evaluation  
  - Suggestions for stronger passwords  
  - Leak detection against known breached databases  
- **Folder:** `PassGuard/`  

### 3️⃣ **PhishNet**
- **Purpose:** Detect phishing URLs and protect users online.  
- **Description:** PhishNet allows users to input URLs to verify if they are safe or potentially malicious. Checks for common phishing patterns and alerts the user with a safety score.  
- **Features:**  
  - Input URL for safety check  
  - Detect common phishing patterns (fake domains, missing HTTPS, etc.)  
  - Display safety score and warnings  
- **Folder:** `PhishNet/`  

### 4️⃣ **SecureVault**
- **Purpose:** Encrypt and decrypt text or files securely.  
- **Description:** SecureVault ensures secure storage and sharing of sensitive data. Users can encrypt messages or files with AES or RSA encryption and decrypt them with the proper key. Demonstrates both symmetric and asymmetric encryption.  
- **Features:**  
  - AES/RSA encryption for files and text  
  - Encrypt and decrypt text or files  
  - Demonstrates symmetric vs asymmetric encryption  
- **Folder:** `SecureVault/`  

---

## **Technologies Used**
- **Languages:** Python, JavaScript (React optional)  
- **Libraries:** `pynput`, `psutil`, `tkinter`, `pycryptodome`, `crypto-js`, Flask  
- **Deployment:**  
  - Web: Render (PassGuard, PhishNet, SecureVault)  
  - Desktop: PyInstaller for Keylogger Guard  

---

## **Contributing**
- Each team member works in their respective sub-project folder.  
- Use branches for feature development and create pull requests for merging.  
- Keep README updated with features and instructions.  

---

## **Fork, Star & Pull Requests**

### **Forking**
Create your own copy of the repository:

```bash
# For Example ,Fork the repository on GitHub first, then clone it locally:
git clone https://github.com/DEVIDAS-CHINNARATHOD/Digital-Security-Suite.git

```

### **Starring**

Bookmark or show support for this repository:
 - Click the "Star" button at the top-right of the repository page on GitHub
 - Helps others discover the project

### **Pull Requests**

Contribute improvements back to the main repository:
- Make changes in your fork
- Push changes to your forked repository
- Open a Pull Request on the original repository page
- The main repo owner will review and merge your changes

### **License**

- This project is for educational purposes only. Do not use Keylogger Guard on unauthorized systems.
