import pexpect
from servers import servers

# Author: Kushal Dalasaniya
# Date: January 23, 2024
# Description: solution to effortlessly manage your servers

def gen_ssh_command(server_ind:int):
    selected_server = servers[server_ind - 1]
    host = selected_server['host']
    username = selected_server['username']
    password = selected_server.get('password')
    pem_path = selected_server.get('pem_path')

    if pem_path:
        ssh_command = f'ssh -i {pem_path} {username}@{host}'
    else:
        ssh_command = f'ssh {username}@{host}'
    
    return (ssh_command, password)


def ssh_to_remote(server1_ind:int,server2_ind=None):
    ssh_command, password=gen_ssh_command(server1_ind)
    term = pexpect.spawn(ssh_command)

    try:
        if password:
            # Expect the password prompt and send the password
            term.expect('password:')
            term.sendline(password)

        # second server connection 
        if server2_ind :
            server2_ssh_command, server2_pass = gen_ssh_command(server2_ind)

            term.sendline(server2_ssh_command)

            # If the second server is not connected via .pem file,
            if server2_pass :
                term.expect('password:')
                term.sendline(server2_pass)
            
            term.expect(['$', '#', '>'])
        
        print(f"Connected to server")

        rows, cols = term.getwinsize()
        term.setwinsize(rows=rows, cols=166)
        
        # Interact with the pseudo-terminal to keep the connection open
        term.interact()
    
    except Exception as e:
        print(f"Error connecting to server: {e} \n")
    
    finally:
        term.close()


# Function to display the menu and get user's choice
def select_server(servers):
    print("Please select two servers from below given servers ")
    print("1. ** Basic SSH Server: **")
    print("   Connect to a fundamental SSH server.")
    print("2. ** Server connected from the first server: **")
    print("   Choose a server that is intricately connected from the first server.\n")
    print("📝 Note : For quit, press 'q' in the first server input, and if you do not want to connect to a second server, press 'n' in the second server input. \n")
 
    print("🌐 Server List : ")
    
    for index, server in enumerate(servers, start=1):
        print(f"{index}. {server['name']} ({server['host']})")
    print(" ")

    server1 = input("Enter the number of the first server (or 'q' to quit): ")
    server2 = 'n'

    if server1.lower() != 'q':
        server2 = input("Enter the number of the second server to connect from the first server (or 'n' to not select any): ")

    print(" ")

    # return {'server1': server1, 'server2': server2}
    return (server1,server2)


# Main function
def main():
    print("👤 Author: Kushal Dalasaniya\n")

    print("Welcome!!  A seamless solution to effortlessly manage your servers! 🚀\n")
    
    while True:
        server1,server2 = select_server(servers)

        if server1.lower() == 'q':
            print("Exiting.........")
            break

        try:
            index = int(server1)
        
            if 1 <= index <= len(servers) and (server2.lower()=='n' or 1 <= int(server2) <= len(servers)):
                server2_ind =  None if server2.lower()=='n' else int(server2)
                ssh_to_remote(index,server2_ind)
        
            else:
                print("Error : Invalid choice. Please enter a valid value!!!!!!!!!!\n")
        
        except ValueError as error:
            print("Error : Invalid input. Please enter a valid value!!!!!!!!!!!\n")
        
        print("\n\n")


if __name__ == '__main__':
    main()