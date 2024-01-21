import paramiko

def execute_remote_script(hostname, port, username, private_key_path, script_path):
    # Create an SSH client
    ssh = paramiko.SSHClient()

    try:
        # Automatically add the server's host key
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the remote server using the private key
        ssh.connect(hostname, port, username, key_filename=private_key_path)

        # Execute the remote script
        stdin, stdout, stderr = ssh.exec_command(f"bash {script_path}")

        # Print the output of the remote script
        print("=== Remote Script Output ===")
        print(stdout.read().decode("utf-8"))

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the SSH connection
        ssh.close()

if __name__ == "__main__":
    # Replace these values with your own
    remote_hostname = "54.91.98.173"
    remote_port = 22  # Default SSH port
    remote_username = "ec2-user"
    private_key_path = "/home/ec2-user/my_key/id_rsa"  # Replace with your private key file path
    remote_script_path = "/home/ec2-user/welcome.sh"

    execute_remote_script(remote_hostname, remote_port, remote_username, private_key_path, remote_script_path)