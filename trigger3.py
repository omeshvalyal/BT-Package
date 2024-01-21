import paramiko
import mysql.connector

def execute_remote_script_and_fetch_data(hostname, port, username, private_key_path, script_path):
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

        # MySQL connection details
        db_host = "mysql-rds.cr8a6wu8g9pk.us-east-1.rds.amazonaws.com"
        db_port = 3306
        db_user = "admin"
        db_password = "Krish$1007"
        db_name = "student_details"

        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=db_name
        )

        cursor = connection.cursor()

        # Fetch the email of student_id 3 from the student_data table
        query = "SELECT email FROM student_data WHERE student_id = 2"
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            print("=== Student Email ===")
            print(result[0])
        else:
            print("Student with ID 3 not found in the database.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the SSH connection
        ssh.close()
        # Close the MySQL connection
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    # Replace these values with your own
    remote_hostname = "54.91.98.173"
    remote_port = 22  # Default SSH port
    remote_username = "ec2-user"
    private_key_path = "/var/lib/jenkins/my_key/id_rsa"  # Replace with your private key file path
    remote_script_path = "/home/ec2-user/welcome.sh"

    execute_remote_script_and_fetch_data(remote_hostname, remote_port, remote_username, private_key_path, remote_script_path)
