import subprocess

def execute_remote_script():
    remote_host = "54.91.98.173"
    remote_script_path = "/home/ec2-user/welcome.sh"

    # Construct the command to execute the shell script remotely
    command = f"ssh -v {remote_host} {remote_script_path}"

    print(f"Executing remote script on {remote_host} at {remote_script_path}...")

    # Execute the command
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    execute_remote_script()
