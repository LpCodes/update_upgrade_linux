import subprocess
import sys

def run_command(command):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        sys.exit(e.returncode)

def update_upgrade():
    """Update and upgrade the Linux system."""
    print("Updating the package list...")
    run_command(["sudo", "apt", "update"])
    
    print("Upgrading the packages...")
    run_command(["sudo", "apt", "upgrade", "-y"])
    
    print("Cleaning up unnecessary packages...")
    run_command(["sudo", "apt", "autoremove", "-y"])

if __name__ == "__main__":
    update_upgrade()