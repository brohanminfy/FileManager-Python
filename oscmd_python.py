import os

def createFile(fileName, content=None):
    try:
        with open(fileName, 'w') as f:
            if content:
                f.write(' '.join(content).replace("\"", ""))
                print(f"Content: '{content}' written successfully")
        print(f"File '{fileName}' created successfully")
    except Exception as e:
        print(f"Error creating file: {e}")

def listDirectory(path='.'):
    try:
        
        entries = os.listdir(path)
       
        max_length = max(len(name) for name in entries) if entries else 0
        for entry in sorted(entries):
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                print(f"{entry}/", end = ' ')
        for entry in sorted(entries):
            full_path = os.path.join(path, entry)
            if os.path.isfile(full_path):
                # Get file size
                print(f"{entry}", end= ' ')
        print()
                
    except Exception as e:
        print(f"Error listing directory: {e}")

def main():
    print(f"{os.getcwd()} > " )
    print("Enter command in format: touch filename [content] / ls [path] / cd [path]")
    string = input()
    parts = string.split()
    cmd = parts[0].lower()

    if cmd == 'touch':
        if len(parts) < 2:
            print("Invalid command format. Use: touch filename [content]")
            return
        file_name = parts[1].replace("\"", "")
        content = parts[2:] if len(parts) > 2 else None
        createFile(file_name, content)
    elif cmd == 'ls':
        path = parts[1] if len(parts) > 1 else '.'
        listDirectory(path)
    elif cmd == 'cd':
        try:
            path = parts[1]
            os.chdir(path)
            print(f"Changed directory to {path}")
        except FileNotFoundError:
            print(f"Directory '{path}' not found")
    else:
        print("Only 'touch', 'ls', 'cd' commands are supported")
        return

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")