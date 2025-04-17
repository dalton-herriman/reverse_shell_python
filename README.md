# 🔁 ReverseShellPy
ReverseShellPy is a lightweight Python-based reverse shell designed for ethical hacking, red teaming, CTFs, and cybersecurity research. It features optional TLS encryption for secure communication between attacker and target systems.

---

## ⚙️ Features
- ✅ Plaintext and TLS-encrypted modes
- ✅ Minimal dependencies
- ✅ UNIX and Windows-compatible
- ✅ Easy-to-extend architecture

## 🚀 Usage

### 🔐 Setup TLS Certificates (optional but recommended)
Generate self-signed TLS certs using OpenSSL:
```bash
openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout key.pem
```
🔒 Store these outside your project directory (e.g., ~/.reverse_shell_certs)
and reference them securely via absolute paths or environment variables.

### 🖥️ Listener (Attacker)
Run the listener:
```bash
python listener.py
```
### 🖥️ Reverse Shell (Victim)
Run the reverse shell from the target machine:
```bash
python reverse_shell.py
```
Ensure that you update the IP addresses properly before use.

## 📁 File Structure
reverse_shell/
├── listener.py          # TLS/Plaintext listener
├── reverse_shell.py     # Client reverse shell payload
└── README.md

## ⚠️ Legal Disclaimer
This project is provided for educational purposes only.
You are solely responsible for how you use this code.
Use only on machines and networks you own or are explicitly authorized to test.
Unauthorized access to computers or networks is illegal and unethical.
The developers of this tool are not responsible for any misuse, damage, or legal consequences that result from using this software.

If you're unsure whether you have permission — you don't.

## 📚 Learn More
- OWASP Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
- MITRE ATT&CK Framework: https://attack.mitre.org/
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework

## 🛠️ Contributions
Pull requests are welcome for improvements, especially around:
- Cross-platform payload support
- Detection evasion techniques (for legal red team use)

## 📜 License
This project is licensed under the MIT License. See LICENSE for more details.

