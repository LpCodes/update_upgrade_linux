# Update & Upgrade Linux Script

This Python script is designed to simplify the process of updating and upgrading Linux machines. It works on Debian-based distributions (like Ubuntu) that use the `apt` package manager.

## Requirements
- Python 3 must be installed on your Linux machine.
- The script requires `sudo` privileges to run, so make sure you have administrative access.

## Installation

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/LpCodes/update_upgrade_linux.git
   cd update-upgrade-linux 

Note : You may need to install Python if you don’t already have it. Run the following command:

  ```sudo apt install python3 ```

## Usage

1. Save/download the script.
2. Make it executable: chmod +x update_upgrade.py.
3. Run it with sudo: sudo ./update_upgrade.py.

The script will automatically:

1. Update the package list.
2. Upgrade installed packages.
3. Remove unnecessary packages.
