# Linux System Update and Upgrade Script

A user-friendly Python script to update and upgrade your Linux system with visual feedback and safety features.

## Features

- 🎨 **Colorful Output**: Easy-to-read colored terminal output
- 🔄 **Progress Indicators**: Visual feedback during operations
- 🛡️ **Safety Features**: 
  - Root permission check
  - Dry-run mode for testing
  - Detailed error handling
- 📝 **Logging**: All operations are logged to `update_upgrade.log`
- 📊 **Summary Reports**: Clear summary of operations performed

## Requirements

- Python 3.x
- Linux operating system
- Root privileges (script will prompt for sudo if needed)
- `apt` package manager (Debian/Ubuntu based systems)

## Installation

1. Clone or download this repository
2. Make the script executable:
```bash
chmod +x update_upgrade_linux.py
```

## Usage

### Basic Usage
```bash
sudo python update_upgrade_linux.py
```

### Dry Run Mode
To see what the script would do without making any changes:
```bash
sudo python update_upgrade_linux.py --dry-run
```

## What the Script Does

1. **Updates Package List**
   - Fetches the latest package information from repositories

2. **Upgrades Packages**
   - Installs available updates for all packages
   - Automatically answers "yes" to prompts

3. **Cleans Up**
   - Removes unnecessary packages
   - Cleans the package cache

## Output Examples

### Normal Run
```
Linux System Update and Upgrade
=============================
This script will update and upgrade your Linux system.
It will perform the following steps:
1. Update package list
2. Upgrade installed packages
3. Remove unnecessary packages
4. Clean package cache

Updating Package List
===================
Updating package list... ⠋
✓ Package list updated successfully

Upgrading Packages
================
Upgrading packages... ⠋
✓ Packages upgraded successfully

Cleaning Up
==========
Removing unnecessary packages... ⠋
✓ Unnecessary packages removed
Cleaning package cache... ⠋
✓ Package cache cleaned

Summary
=======
✓ System update and upgrade completed successfully!
Your system is now up to date!
```

### Dry Run
```
Linux System Update and Upgrade
=============================
This script will update and upgrade your Linux system.
It will perform the following steps:
1. Update package list
2. Upgrade installed packages
3. Remove unnecessary packages
4. Clean package cache

⚠ DRY RUN MODE: No changes will be made to the system

Updating Package List
===================
Updating package list... ⠋
⚠ Would run: apt update

Upgrading Packages
================
Upgrading packages... ⠋
⚠ Would run: apt upgrade -y

Cleaning Up
==========
Removing unnecessary packages... ⠋
⚠ Would run: apt autoremove -y
Cleaning package cache... ⠋
⚠ Would run: apt autoclean

Summary
=======
⚠ This was a dry run. No changes were made to the system.
```

## Logging

The script creates a log file `update_upgrade.log` with detailed information about:
- Start and end times of operations
- Success or failure of each command
- Error messages if any occur

## Error Handling

The script includes comprehensive error handling:
- Checks for root privileges
- Handles command execution errors
- Provides clear error messages
- Logs all errors for debugging

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License.
