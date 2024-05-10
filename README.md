# Server Manager Command-line Interface

Welcome to the Server Manager Command-line Interface (CLI)!

## Functionality
- Server Selection: Choose and connect to two servers from the available list.
- Multi-Hop Connections (Optional): Optionally, initiate a connection directly to a second server through the first server, enabling secure multi-hop access.

## Preview
![server-manager-img](https://github.com/Kushal-Dalasaniya/server-manager/assets/108124477/c658317c-d926-473e-b579-e11be594eb02)

## How to Use

1. **Selecting Servers:**
   - Launch the Server Manager: Access your terminal and navigate to the directory containing the server manager executable.
   - Select the First Server: You'll be presented with a list of accessible servers. Enter the corresponding number to connect to a specific server (e.g., 1 for "server 1"). Alternatively, type "q" to exit the program.
   - Optional: Connect to a Second Server: If you desire a multi-hop connection, enter the number of the desired second server after selecting the first one. Otherwise, press "n" to bypass this step and directly connect to the initially selected server.

2. **Connecting Servers:**
   - If you choose to connect to a second server, both the first and second servers will be connected, and you will be directly connected to the second server.

3. **Exiting the CLI:**
   - To quit the CLI, simply press 'q' when prompted for the first server.

## Saving Server Details

To save server details for the Server Manager, you need to edit the `servers.py` file. Here's how:

1. Open the `servers.py` file in a text editor.

2. Update the `servers` list with the details of your servers. Each server should be represented as a dictionary with the following keys:
   - `'name'`: Name of the server.
   - `'host'`: IP address or hostname of the server.
   - `'username'`: Username for SSH login.
   - `'password'`: Password for SSH login (if applicable).
   - `'pem_path'`: Path to the PEM file for SSH login (if applicable).

3. Save the `servers.py` file.

## Setting up Server Manager Desktop Shortcut

To create a desktop shortcut for easy access to the Server Manager on Ubuntu or Linux, follow these steps:
1. Replace `<Give server-manager folder path here>` with the actual path to your Server Manager folder in server-manager.desktop file.
2. Move the `server-manager.desktop` file from the project folder to the `~/.local/share/applications/` directory. You can do this using the Terminal or your file manager.
3. Ensure executable permissions for the `.desktop` file:


## Installing Dependencies

Before running the Server Manager, ensure that you have Python and pip installed on your system. If you haven't installed them yet, you can download and install them from the following links:
- [Python Installation](https://www.python.org/downloads/)
- [pip Installation](https://pip.pypa.io/en/stable/installation/)

Additionally, you'll need to install the `pexpect` library. 

Navigate to the Server Manager directory and run the following command:
`pip install pexpect`

Once these steps are completed, you're all set to use the Server Manager!

## Note
- SSH Credentials: Ensure you possess the necessary SSH credentials for the servers you intend to connect to.
- Basic Functionality: The server manager primarily focuses on server selection and connection initiation. For more advanced server management tasks, you might need dedicated tools or commands specific to the server's operating system.
