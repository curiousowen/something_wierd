# something_wierd
Something_Wierd simplifies the use of the Volatility Framework for memory forensics. It guides users through analyzing memory dumps with intuitive prompts and input validation.

Prerequisites

Before using Something_wierd, ensure you have the following:

    Python 3.x installed on your system.
    Volatility Framework installed and available in your PATH.
    A memory dump file for analysis.

Installing Volatility

You can install the Volatility Framework using pip:

    pip install volatility

Getting Started
Script Usage

Clone or download the script:
Save the something_wierd.py script to your local machine.

Run the script:
Open a terminal or command prompt, navigate to the directory containing something_wierd.py, and execute the script:

    python something_wierd.py

Follow the prompts:
The script will guide you through the process of analyzing a memory dump. Enter the required information as prompted.

Inputs

Memory Dump File Path:
Format: Should be an absolute path to the memory dump file.
Examples:
Windows: C:\memory_dumps\example.dmp
Linux: /home/user/memory_dumps/example.dmp

Profile:
Format: Should match the operating system and version of the memory dump.
Examples:
Windows 7 Service Pack 1, 64-bit: Win7SP1x64
Windows 10, 64-bit, build 19041: Win10x64_19041
Ubuntu 18.04, 64-bit: LinuxUbuntu_18_04_x64

Action:
Selection: Choose an action by entering the corresponding number.
Examples:
1: pslist - List all running processes.
2: psscan - Scan for process objects in memory.
3: netscan - Scan for network connections.
4: dlllist - List all loaded DLLs for each process.
5: handles - List all open handles for each process.
6: filescan - Scan for file objects in memory.
7: imageinfo - Display information about the memory image.
8: kdbgscan - Scan for Kernel Debugger Block structures.
9: malfind - Scan for hidden or injected code.

Additional Inputs for Specific Actions:
printkey:
Registry Key: Enter the registry key to print.
procdump:
Process ID (PID): Enter the PID of the process to dump.
Output Directory: Enter a valid directory path to save the dumped process memory.
dumpfiles:
File Offset: Enter the file offset to dump.
Output Directory: Enter a valid directory path to save the dumped files.

Troubleshooting

If you encounter any issues, ensure that:

The memory dump file path is correct and the file exists.
The profile matches the operating system and version of the memory dump.
Volatility is installed and available in your PATH.
