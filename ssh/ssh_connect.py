import paramiko

def ssh_connect(hostname, port, username, password):
    try:
        # Create an SSH client
        client = paramiko.SSHClient()
        
        # Load system host keys
        client.load_system_host_keys()
        
        # Set the policy to add the server's host key if missing
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the SSH server
        client.connect(hostname, port=port, username=username, password=password)
        
        print(f"Successfully connected to {hostname}")

        # Execute a command (optional)
        stdin, stdout, stderr = client.exec_command('ls -l')
        print(stdout.read().decode())
        
    except Exception as e:
        print(f"Failed to connect to {hostname}: {e}")
    finally:
        # Close the connection
        client.close()

if __name__ == "__main__":
    # Replace with your device's details
    hostname = '192.168.111.251'  # IP address or hostname of the SSH device
    port = 22                  # Default SSH port
    username = 'root' # SSH username
    password = '' # SSH password

    ssh_connect(hostname, port, username, password)