import psutil
import time
import subprocess

# List of known scammer software
scammer_software = ['teamviewer', 'anydesk', 'logmein', 'ammyy', 'rdp', 'vnc', 'netsupport', 'gotomypc', 'supremo', 'notepad']

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
                        print(f"Terminating {scammer_tool.capitalize()} process (PID {process.info['pid']})")
                        process.terminate()
                        
                        # Write the termination message to a file
                        with open("log.txt", "a") as file:  # Use "a" mode for append
                            file.write(f"Terminated {scammer_tool.capitalize()} process (PID {process.info['pid']})\n")
                        
                        # Send a message to app.py
                        send_message_to_app(f"Terminated {scammer_tool.capitalize()} process (PID {process.info['pid']})")
                        
                        # Check if app.py is already running, if not, run it
                        if not app_running:
                            print("Starting app.py...")
                            subprocess.Popen(["python", "app.py"])
                            app_running = True
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(10)  # Check for scammer processes every 60 seconds

if __name__ == "__main__":
    terminate_scammer_processes()
