import psutil
import time
import subprocess
from send import send_message

# List of known scammer software
def load_blacklist(file_path):
    try:
        with open(file_path, "r") as text_file:
            scammer_software = text_file.read().split('\n')
        return scammer_software
    except Exception as e:
        print(f"Error loading blacklist: {e}")
        return []

scammer_software = load_blacklist("blacklist.txt")

# Flag to check if app.py is already running
app_running = False

def send_message_to_app(message):
    try:
        with open("log.txt", "a") as file:  # Use "a" mode for append
            file.write(message + "\n")  # Append a newline character after each message
    except Exception as e:
        print(f"Error: {e}")

def terminate_scammer_processes():
    global app_running  # Declare app_running as global
    
    while True:
        try:
            for process in psutil.process_iter(attrs=['pid', 'name']):
                process_name = process.info['name'].lower()
                for scammer_tool in scammer_software:
                    if scammer_tool in process_name:
                        process.terminate()

                        # Send a message to app.py
<<<<<<< HEAD
                        send_message(f"Terminated {scammer_tool.capitalize()} process (PID {process.info['pid']})")
=======
                        send_message_to_app(f"Suspicious software has been detected: {scammer_tool.capitalize()}. A trusted contact has been notified.)")
>>>>>>> b8ab09cabf0b19ddf9f77534a260a33b9c20760b
                        
                        # Check if app.py is already running, if not, run it
                        if not app_running:
                            subprocess.Popen(["python", "app.py"])
                            app_running = True
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(10)  # Check for scammer processes every 10 seconds

if __name__ == "__main__":
    terminate_scammer_processes()
