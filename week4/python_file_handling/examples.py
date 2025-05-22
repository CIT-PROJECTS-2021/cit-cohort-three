# Constants for filenames
TEXT_FILENAME = "sample_text_data.txt"
BINARY_FILENAME = "sample_binary_data.bin"

# --- Text File Operations ---

def demo_text_write():
    print("\n--- Text: 'w' (write, truncates) ---")
    try:
        with open(TEXT_FILENAME, 'w', encoding='utf-8') as f:
            f.write("Line 1: Hello from 'w' mode.\n")
            f.write("Line 2: Python file handling.\n")
        print(f"Content written to {TEXT_FILENAME}")
    except IOError as e:
        print(f"IOError: {e}")

def demo_text_read():
    print("\n--- Text: 'r' (read) ---")
    try:
        with open(TEXT_FILENAME, 'r', encoding='utf-8') as f:
            print(f"Reading full content of {TEXT_FILENAME}:\n{f.read()}")
        
        with open(TEXT_FILENAME, 'r', encoding='utf-8') as f:
            print(f"\nReading {TEXT_FILENAME} line by line:")
            for line in f:
                print(line, end='')
        
        with open(TEXT_FILENAME, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(f"\n\nRead lines with f.readlines():\n{lines}")
    except FileNotFoundError:
        print(f"Error: {TEXT_FILENAME} not found.")
    except IOError as e:
        print(f"IOError: {e}")

def demo_text_append():
    print("\n--- Text: 'a' (append) ---")
    try:
        with open(TEXT_FILENAME, 'a', encoding='utf-8') as f:
            f.write("Line 3: Appended line.\n")
        print(f"Appended to {TEXT_FILENAME}. New content:")
        with open(TEXT_FILENAME, 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Error: {TEXT_FILENAME} not found.")
    except IOError as e:
        print(f"IOError: {e}")

def demo_text_w_plus():
    print("\n--- Text: 'w+' (write & read, truncates) ---")
    try:
        with open(TEXT_FILENAME, 'w+', encoding='utf-8') as f:
            f.write("Overwritten by 'w+' mode.\nSecond line for 'w+'.\n")
            print(f"Wrote to {TEXT_FILENAME}. Pointer: {f.tell()}")
            f.seek(0) # Go to start to read
            print(f"Seek(0). Pointer: {f.tell()}. Reading:\n{f.read()}")
    except IOError as e:
        print(f"IOError: {e}")

def demo_text_r_plus():
    print("\n--- Text: 'r+' (read & write) ---")
    try:
        # Ensure file exists with known content for this demo
        with open(TEXT_FILENAME, 'w', encoding='utf-8') as f:
            f.write("Original line for r+.\nSecond original line.\n")

        with open(TEXT_FILENAME, 'r+', encoding='utf-8') as f:
            print(f"Initial content for 'r+':\n{f.read()}")
            # f.tell() is now at the end. Let's seek to overwrite start of first line.
            f.seek(0) 
            f.write("MODIFIED") # Overwrites first 8 chars
            print(f"Wrote 'MODIFIED'. Pointer: {f.tell()}")
            f.seek(0)
            print(f"Content after 'r+' modification:\n{f.read()}")
    except FileNotFoundError:
        print(f"Error: {TEXT_FILENAME} not found.")
    except IOError as e:
        print(f"IOError: {e}")

def demo_text_a_plus():
    print("\n--- Text: 'a+' (append & read) ---")
    try:
        # Ensure file exists with known content for this demo
        with open(TEXT_FILENAME, 'w', encoding='utf-8') as f:
            f.write("Base content for a+.\n")

        with open(TEXT_FILENAME, 'a+', encoding='utf-8') as f:
            # Pointer starts at end for writing in 'a+'
            f.write("Appended in 'a+' mode.\n")
            print(f"Appended to {TEXT_FILENAME}. Pointer: {f.tell()}")
            f.seek(0) # Go to start to read
            print(f"Seek(0). Pointer: {f.tell()}. Full content:\n{f.read()}")
    except FileNotFoundError:
        print(f"Error: {TEXT_FILENAME} not found.")
    except IOError as e:
        print(f"IOError: {e}")

# --- Binary File Operations ---

def demo_binary_write():
    print("\n--- Binary: 'wb' (write binary) ---")
    try:
        with open(BINARY_FILENAME, 'wb') as f:
            data = b'\x00\xDE\xAD\xBE\xEF\xFF'
            f.write(data)
        print(f"Binary data written to {BINARY_FILENAME}: {data}")
    except IOError as e:
        print(f"IOError: {e}")

def demo_binary_read():
    print("\n--- Binary: 'rb' (read binary) ---")
    try:
        with open(BINARY_FILENAME, 'rb') as f:
            data_read = f.read()
            print(f"Binary data read from {BINARY_FILENAME}: {data_read}")
            print(f"Hex representation: {data_read.hex()}")
    except FileNotFoundError:
        print(f"Error: {BINARY_FILENAME} not found.")
    except IOError as e:
        print(f"IOError: {e}")

# --- Main execution ---
def main():
    print("=== Python File Handling Examples ===")
    
    demo_text_write()
    demo_text_read()
    demo_text_append()
    demo_text_w_plus()
    demo_text_r_plus()
    demo_text_a_plus()
    
    demo_binary_write()
    demo_binary_read()
    
    print(f"\n=== Demonstrations complete. Check '{TEXT_FILENAME}' and '{BINARY_FILENAME}'. ===")
    print(f"Note: '{TEXT_FILENAME}' will reflect the state after the *last* text operation ('a+' mode).")

if __name__ == "__main__":
    main()
