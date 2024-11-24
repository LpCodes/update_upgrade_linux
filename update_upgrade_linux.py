import subprocess
import sys
import os
import logging

# Configure logging
logging.basicConfig(
    filename='update_upgrade.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_command(command):
    """
    Run a system command and handle errors.

    Args:
        command (list): The command to run as a list of arguments.

    Returns:
        str: The standard output of the command.
    """
    try:
        result = subprocess.run(
            command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        logging.info(f"Command succeeded: {' '.join(command)}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {' '.join(command)}")
        logging.error(f"Error output: {e.stderr}")
        print(f"Error: {e.stderr.strip()}")
        sys.exit(e.returncode)

def check_root():
    """
    Ensure the script is run with root privileges.
    """
    if os.geteuid() != 0:
        print("This script must be run as root. Use 'sudo' to execute it.")
        logging.error("Script not run as root.")
        sys.exit(1)

def update_upgrade():
    """
    Update and upgrade the Linux system.
    """
    check_root()

    print("Updating the package list...")
    logging.info("Updating the package list.")
    print(run_command(["apt", "update"]))

    print("Upgrading the packages...")
    logging.info("Upgrading the packages.")
    print(run_command(["apt", "upgrade", "-y"]))

    print("Cleaning up unnecessary packages...")
    logging.info("Cleaning up unnecessary packages.")
    print(run_command(["apt", "autoremove", "-y"]))

    print("Cleaning up package cache...")
    logging.info("Cleaning up package cache.")
    print(run_command(["apt", "autoclean"]))

    print("Update and upgrade completed successfully!")
    logging.info("Update and upgrade process completed successfully.")

if __name__ == "__main__":
    update_upgrade()
