import os
import subprocess
import sys

def run_volatility(plugin, memory_file, profile, extra_args=None):
    """
    Runs a Volatility plugin with the provided memory dump, profile, and extra arguments.
    """
    command = ['vol.py', '-f', memory_file, '--profile', profile, plugin]
    if extra_args:
        command.extend(extra_args)
    
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            print(f"Error: {stderr.decode()}")
        else:
            print(stdout.decode())
    except FileNotFoundError:
        print("Error: Volatility not found. Make sure it is installed and in your PATH.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def validate_file_path(file_path):
    """
    Validates if the provided file path exists and is a file.
    """
    if not os.path.isfile(file_path):
        print(f"Invalid file path: {file_path}. Please enter a valid memory dump file path.")
        sys.exit(1)

def validate_input(input_value, valid_values):
    """
    Validates if the input value is among the valid values.
    """
    if input_value not in valid_values:
        print(f"Invalid input: {input_value}. Expected one of {valid_values}.")
        sys.exit(1)

def main():
    """
    Main function to guide the user through the memory dump analysis.
    """
    memory_file = input("Enter the memory dump file path (e.g., C:\\memory_dumps\\example.dmp or /home/user/memory_dumps/example.dmp): ")
    validate_file_path(memory_file)
    
    profile = input("Enter the profile (e.g., Win7SP1x64, Win10x64_19041, LinuxUbuntu_18_04_x64): ")

    actions = {
        '1': 'pslist',
        '2': 'psscan',
        '3': 'netscan',
        '4': 'dlllist',
        '5': 'handles',
        '6': 'filescan',
        '7': 'imageinfo',
        '8': 'kdbgscan',
        '9': 'malfind'
    }

    print("\nSelect an action:")
    for key, action in actions.items():
        print(f"{key}. {action}")
    
    choice = input("Enter the number of the action you want to perform: ")
    validate_input(choice, actions.keys())

    plugin = actions[choice]
    extra_args = None

    if plugin == 'printkey':
        registry_key = input("Enter the registry key: ")
        extra_args = ['-K', registry_key]
    elif plugin == 'procdump':
        pid = input("Enter the process ID (PID): ")
        output_dir = input("Enter the output directory: ")
        if not os.path.isdir(output_dir):
            print(f"Invalid directory path: {output_dir}. Please enter a valid directory.")
            sys.exit(1)
        extra_args = ['-p', pid, '-D', output_dir]
    elif plugin == 'dumpfiles':
        file_offset = input("Enter the file offset: ")
        output_dir = input("Enter the output directory: ")
        if not os.path.isdir(output_dir):
            print(f"Invalid directory path: {output_dir}. Please enter a valid directory.")
            sys.exit(1)
        extra_args = ['-Q', file_offset, '-D', output_dir]

    run_volatility(plugin, memory_file, profile, extra_args)

if __name__ == "__main__":
    main()
