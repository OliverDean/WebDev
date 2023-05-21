import time
import subprocess

# Define the number of app instances to create
num_instances = 1

# Start the loop to create and run the app instances
for i in range(num_instances):
    # Generate a unique port number for each instance
    port = 5000 + i

    # Start the app instance in a subprocess
    command = f"python -m flask run -p {port}"
    process = subprocess.Popen(command, shell=True, cwd='.')
    print(f"Started app instance {i + 1} on port {port}...")
    print(f"Starting selenium test... for registration and login")
    time.sleep(3)

    selenium_command =f"python testing/selenium_test.py -p {port}"
    selenium_process = subprocess.Popen(selenium_command, shell=True, cwd='.')
    selenium_process.wait()

    # Terminate the app instance subprocess
    process.terminate()

    print(f"Terminated app instance {i + 1}.")


    port += i

    # Start the app instance in a subprocess
    command = f"python -m flask run -p {port}"
    process = subprocess.Popen(command, shell=True, cwd='.')
    print(f"Started app instance {i + 1} on port {port}...")
    print(f"Starting selenium test... for navigation")
    time.sleep(3)

    selenium_command =f"python testing/selenium2.py -p {port}"
    selenium_process = subprocess.Popen(selenium_command, shell=True, cwd='.')
    selenium_process.wait()

    # Terminate the app instance subprocess
    process.terminate()

    print(f"Terminated app instance {i + 1}.")



print("All app instances completed.")