
<p align="center">
  <img src="assets/noprompt-logo.png" alt="NoPrompt Logo" width="250"/>
</p>

<h1 align="center">NoPrompt</h1>
<p align="center"><i>Password-Only Access Detector for Entra ID APIs</i></p>




---

## 🚀 What is NoPrompt?

NoPrompt is a lightweight tool to **check if Microsoft Entra ID APIs allow password-only authentication** — meaning whether access can be granted with just a username and password, without requiring Multi-Factor Authentication (MFA).

It sends OAuth2 token requests simulating various device user agents to quickly detect if password-only access is possible on different Microsoft APIs.

---

## 🔍 Why Use NoPrompt?

- Quickly verify if password-only access is enabled for your account on key Microsoft APIs.
- Understand where MFA enforcement is missing or not applied.
- Help improve your account security posture by identifying weak access controls.
- Evaluate your organization's Conditional Access policies effectiveness.

---
## 🔧 Installation 

You can run NoPrompt using **Python 3.8+**. Follow these steps:

```bash
# 1. Clone the repository
git clone https://github.com/terminalOO12/NoPrompt.git
cd noprompt

# 2. (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

## Command-Line Options

| Flag                 | Description                                              | Example                 |
|----------------------|----------------------------------------------------------|-------------------------|
| `--useragent`, `-u`  | Specify a user agent to test (case-insensitive).         | `--useragent Windows`   |
|                      | Use `all` (default) to test all available user agents.   | `--useragent all`       |

---

## Supported User Agents

- Windows
- Linux
- MacOS
- Android
- iPhone
- WindowsPhone

---

## ▶️ Usage Examples

| Command                                | Description                         |
|---------------------------------------|-----------------------------------|
| `python3 noprompt.py -h`                   | Show help and available options   |
| `python3 noprompt.py --useragent all`      | Run tests for all user agents (default) |
| `python3 noprompt.py --useragent Windows`  | Test using the Windows user agent |
| `python3 noprompt.py --useragent Linux`    | Test using the Linux user agent   |
| `python3 noprompt.py --useragent MacOS`    | Test using the MacOS user agent   |
| `python3 noprompt.py --useragent Android`  | Test using the Android user agent |
| `python3 noprompt.py --useragent iPhone`   | Test using the iPhone user agent  |
| `python3 noprompt.py --useragent WindowsPhone` | Test using the WindowsPhone user agent |

---


## 🧪 Sample Output

```plaintext

  _   _         _____                           _
 | \ | |       |  __ \                         | |
 |  \| | ___   | |__) | __ ___  _ __ ___  _ __ | |_
 | . ` |/ _ \  |  ___/ '__/ _ \| '_ ` _ \| '_ \| __|
 | |\  | (_) | | |   | | | (_) | | | | | | |_) | |_
 |_| \_|\___/  |_|   |_|  \___/|_| |_| |_| .__/ \__|
                                         | |
                                         |_|

Password-Only Access Detector for Entra ID APIs

Enter your email: test@test.com
Enter your password:

######### PASSWORD-ONLY ACCESS CHECK #########

==== Testing User Agent: Windows ====
   AAD Graph API                  | ✅ Access Granted
   Microsoft Graph API            | ✅ Access Granted
   Service Management API         | 🔒 Blocked Requires MFA

==== Testing User Agent: Linux ====
   AAD Graph API                  | ✅ Access Granted
   Microsoft Graph API            | ✅ Access Granted
   Service Management API         | 🔒 Blocked Requires MFA

==== Testing User Agent: MacOS ====
   AAD Graph API                  | ✅ Access Granted
   Microsoft Graph API            | ✅ Access Granted
   Service Management API         | 🔒 Blocked Requires MFA

==== Testing User Agent: Android ====
   AAD Graph API                  | ✅ Access Granted
   Microsoft Graph API            | ✅ Access Granted
   Service Management API         | 🔒 Blocked Requires MFA

==== Testing User Agent: iPhone ====
   AAD Graph API                  | ✅ Access Granted
   Microsoft Graph API            | ✅ Access Granted
   Service Management API         | 🔒 Blocked Requires MFA

==== Testing User Agent: WindowsPhone ====
   AAD Graph API                  | ✅ Access Granted
   Microsoft Graph API            | ✅ Access Granted
   Service Management API         | 🔒 Blocked Requires MFA

```



