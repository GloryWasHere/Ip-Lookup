import requests
from colorama import Fore, Style, init

def get_ip_info(ip):
    """
    Get IP information from ip-api.com
    """
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print_colorful(f"Error fetching IP information: {e}", "red")
        return None

def print_colorful(text, color):
    """
    Print text in a specified color.
    """
    colors = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "purple": Fore.MAGENTA,
        "cyan": Fore.CYAN,
    }
    print(f"{colors.get(color, Fore.WHITE)}{text}{Style.RESET_ALL}")

def main():
    init(autoreset=True)
    print_colorful("Welcome to T9tz's IP Lookup Tool", "blue")
    print_colorful("[💎] Made by T9tz [💎]", "yellow")
    print_colorful("----------------------------------------", "cyan")

    while True:
        ip_address = input("Enter IP Address: ")
        if not ip_address:
            print_colorful("Please enter a valid IP address.", "red")
            continue

        print_colorful("Fetching data...", "yellow")
        ip_info = get_ip_info(ip_address)

        if ip_info and ip_info["status"] == "success":
            print_colorful("🌍 IP Information 🌍", "green")
            print_colorful("----------------------------------------", "cyan")
            print_colorful(f"IP Address: {ip_info['query']}", "blue")
            print_colorful(f"Country: {ip_info['country']}", "blue")
            print_colorful(f"State: {ip_info.get('regionName', 'N/A')}", "blue")
            print_colorful(f"City: {ip_info['city']}", "blue")
            print_colorful(f"ISP: {ip_info['isp']}", "blue")
            print_colorful("----------------------------------------", "cyan")
        else:
            print_colorful("Error: Unable to fetch IP information.", "red")

        another = input("Do you want to perform another IP lookup? (yes/no): ")
        if another.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
