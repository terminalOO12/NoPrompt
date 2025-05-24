import requests
import getpass
from colorama import Fore, Style, init
import argparse
import sys

# Initialize colorama
init(autoreset=True)

# Color definitions
GREEN = Fore.GREEN
RED = Fore.RED
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RESET = Style.RESET_ALL

# User agents
user_agents = {
    "Windows": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/58.0.3029.110 Safari/537.3",
    "Linux": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/88.0.4324.96 Safari/537.36",
    "MacOS": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/605.1.15",
    "Android": "Mozilla/5.0 (Linux; Android 10; Pixel 3) AppleWebKit/537.36 Chrome/91.0.4472.120 Mobile Safari/537.36",
    "iPhone": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 Mobile/15E148 Safari/604.1",
    "WindowsPhone": "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1116) AppleWebKit/537.36 Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254"
}

# APIs to test
apis = {
    "AAD Graph API": "https://graph.windows.net/",
    "Microsoft Graph API": "https://graph.microsoft.com/",
    "Service Management API": "https://management.core.windows.net/",
}

# ASCII logo
def print_logo():
    print(fr"""{CYAN}
  _   _         _____                           _   
 | \ | |       |  __ \                         | |  
 |  \| | ___   | |__) | __ ___  _ __ ___  _ __ | |_ 
 | . ` |/ _ \  |  ___/ '__/ _ \| '_ ` _ \| '_ \| __|
 | |\  | (_) | | |   | | | (_) | | | | | | |_) | |_ 
 |_| \_|\___/  |_|   |_|  \___/|_| |_| |_| .__/ \__|
                                         | |        
                                         |_|      

{YELLOW}Password-Only Access Detector for Entra ID APIs{RESET}
""")

# Parse command-line arguments
def parse_args():
    parser = argparse.ArgumentParser(description="Check password-only access for Entra ID APIs.")
    parser.add_argument("--useragent", "-u", default="all", help="Choose a user agent (Windows, Linux, MacOS, Android, iPhone, WindowsPhone, all)")
    return parser.parse_args()

def main():
    args = parse_args()
    selected_agent = args.useragent.lower()

    print_logo()

    email = input("Enter your email: ")
    password = getpass.getpass("Enter your password: ")

    print(f"\n{CYAN}######### PASSWORD-ONLY ACCESS CHECK #########{RESET}\n")

    agents_to_test = []

    if selected_agent == "all":
        agents_to_test = user_agents.items()
    else:
        # Match case-insensitive agent name
        matched = [(k, v) for k, v in user_agents.items() if k.lower() == selected_agent]
        if not matched:
            print(f"{RED}Invalid user agent specified: {args.useragent}{RESET}")
            print("Valid options are: " + ", ".join(user_agents.keys()) + ", all")
            sys.exit(1)
        agents_to_test = matched

    for ua_name, ua_string in agents_to_test:
        print(f"{CYAN}==== Testing User Agent: {ua_name} ===={RESET}")

        for api_name, resource in apis.items():
            headers = {
                'User-Agent': ua_string,
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            data = {
                'grant_type': 'password',
                'client_id': '1b730954-1685-4b74-9bfd-dac224a7b894',
                'resource': resource,
                'username': email,
                'password': password,
                'scope': 'openid'
            }

            try:
                response = requests.post("https://login.microsoftonline.com/common/oauth2/token", data=data, headers=headers)

                if response.status_code == 200:
                    json_resp = response.json()
                    if 'access_token' in json_resp:
                        result = f"{GREEN}✅ Access Granted{RESET}"
                    else:
                        result = f"{RED}🔒 Blocked Requires MFA{RESET}"
                else:
                    result = f"{RED}🔒 Blocked Requires MFA{RESET}"


            except Exception as e:
                result = f"{RED}ERROR: {str(e)}{RESET}"

            print(f"   {api_name:<30} | {result}")

        print()

if __name__ == '__main__':
    main()
