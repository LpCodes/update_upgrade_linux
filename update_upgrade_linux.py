import subprocess
import sys
import os
import logging
import time
from typing import List, Optional

# Configure logging
logging.basicConfig(
    filename='update_upgrade.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ANSI color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_colored(text: str, color: str) -> None:
    """Print colored text to the terminal."""
    print(f"{color}{text}{Colors.END}")

def print_header(text: str) -> None:
    """Print a header with a separator line."""
    print_colored(f"\n{Colors.BOLD}{text}{Colors.END}", Colors.BLUE)
    print_colored("=" * len(text), Colors.BLUE)

def print_success(text: str) -> None:
    """Print success message in green."""
    print_colored(f"✓ {text}", Colors.GREEN)

def print_warning(text: str) -> None:
    """Print warning message in yellow."""
    print_colored(f"⚠ {text}", Colors.YELLOW)

def print_error(text: str) -> None:
    """Print error message in red."""
    print_colored(f"✗ {text}", Colors.RED)

def run_command(command: List[str], dry_run: bool = False) -> Optional[str]:
    """
    Run a system command and handle errors.

    Args:
        command (list): The command to run as a list of arguments.
        dry_run (bool): If True, only print the command without executing it.

    Returns:
        str: The standard output of the command or None if dry_run is True.
    """
    if dry_run:
        print_warning(f"Would run: {' '.join(command)}")
        return None

    try:
        print_colored(f"Running: {' '.join(command)}", Colors.BLUE)
        result = subprocess.run(
            command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        logging.info(f"Command succeeded: {' '.join(command)}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {' '.join(command)}")
        logging.error(f"Error output: {e.stderr}")
        print_error(f"Command failed: {e.stderr.strip()}")
        sys.exit(e.returncode)

def check_root() -> None:
    """Ensure the script is run with root privileges."""
    if os.geteuid() != 0:
        print_error("This script must be run as root. Use 'sudo' to execute it.")
        logging.error("Script not run as root.")
        sys.exit(1)

def show_progress(message: str, duration: int = 2) -> None:
    """Show a simple progress animation."""
    for i in range(duration * 10):
        sys.stdout.write(f"\r{message} {'⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'[i % 10]}")
        sys.stdout.flush()
        time.sleep(0.1)
    print()

def update_upgrade(dry_run: bool = False) -> None:
    """
    Update and upgrade the Linux system.

    Args:
        dry_run (bool): If True, only show what would be done without making changes.
    """
    check_root()

    print_header("Linux System Update and Upgrade")
    print_colored("This script will update and upgrade your Linux system.", Colors.BOLD)
    print_colored("It will perform the following steps:", Colors.BOLD)
    print("1. Update package list")
    print("2. Upgrade installed packages")
    print("3. Remove unnecessary packages")
    print("4. Clean package cache")
    
    if dry_run:
        print_warning("DRY RUN MODE: No changes will be made to the system")

    # Update package list
    print_header("Updating Package List")
    show_progress("Updating package list...")
    output = run_command(["apt", "update"], dry_run)
    if output and not dry_run:
        print_success("Package list updated successfully")

    # Upgrade packages
    print_header("Upgrading Packages")
    show_progress("Upgrading packages...")
    output = run_command(["apt", "upgrade", "-y"], dry_run)
    if output and not dry_run:
        print_success("Packages upgraded successfully")

    # Remove unnecessary packages
    print_header("Cleaning Up")
    show_progress("Removing unnecessary packages...")
    output = run_command(["apt", "autoremove", "-y"], dry_run)
    if output and not dry_run:
        print_success("Unnecessary packages removed")

    # Clean package cache
    show_progress("Cleaning package cache...")
    output = run_command(["apt", "autoclean"], dry_run)
    if output and not dry_run:
        print_success("Package cache cleaned")

    print_header("Summary")
    if dry_run:
        print_warning("This was a dry run. No changes were made to the system.")
    else:
        print_success("System update and upgrade completed successfully!")
        print_colored("Your system is now up to date!", Colors.BOLD)
    logging.info("Update and upgrade process completed successfully.")

if __name__ == "__main__":
    dry_run = "--dry-run" in sys.argv
    update_upgrade(dry_run)
