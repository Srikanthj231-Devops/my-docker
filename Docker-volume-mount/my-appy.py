# read_servers.py

def read_server_file():
    try:
        with open("servers.txt", "r") as file:
            lines = file.readlines()
            if lines:
                print("Servers listed in the file:")
                for idx, line in enumerate(lines, start=1):
                    print(f"{idx}. {line.strip()}")
            else:
                print("The servers.txt file is empty.")
    except FileNotFoundError:
        print("Error: The file 'servers.txt' was not found.")

if __name__ == "__main__":
    read_server_file()
