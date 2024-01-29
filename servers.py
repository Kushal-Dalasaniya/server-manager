servers = [
    {'name': 'server 1', 'host': '000.000.00.000', 'username': 'ubuntu', 'password': 'password'},
    {'name': 'server 2', 'host': '000.00.000.00', 'username': 'ubuntu', 'password': 'password'},
    {'name': 'Server 3', 'host': '00.000.00.000', 'username': 'ubuntu', 'pem_path':'your pem file path'},
    {'name': 'Server 4', 'host': '00.000.00.000', 'username': 'ubuntu', 'password': 'password'},
    # Add more servers as needed 
]
# In a real-life scenario, your server should be secured either by a password or a PEM file. If you have a password, add it to the servers array. Alternatively, if you have a PEM file, specify the file path here.