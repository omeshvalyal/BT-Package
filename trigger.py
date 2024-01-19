import subprocess

def execute_remote_script():
    remote_host = "54.91.98.173"
    remote_script_path = "/home/ec2-user/welcome.sh"

    # Construct the command to execute the shell script remotely
    command = f"ssh {remote_host} {remote_script_path}"

    # Execute the command
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    execute_remote_script()
