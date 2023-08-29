import socket

target_host = input("Enter the target host or IP address: ")

for port in range(1, 65536):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        socket.setdefaulttimeout(1)
        
        result = client.connect_ex((target_host, port))
        
        if result == 0:
            print(f"Port {port} is open")
        
        client.close()
    
    except KeyboardInterrupt:
        print("\nExiting...")
        break
    
    except socket.gaierror:
        print("Hostname could not be resolved")
        break
    
    except socket.error:
        print("Couldn't connect to server")
        break
