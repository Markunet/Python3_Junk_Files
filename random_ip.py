import random

# Function to generate a random IP
def random_ip(base_network="10.0.0."):
    # Generate a random number between 1 and 254
    last_octet = random.randint(1, 254)
    # Convert int to str
    last_octet_str = str(last_octet)
    # Print the IP address
    print(f"IP address: {base_network + last_octet_str}")
    # Print empty line
    print("")

# Call with positional argument
random_ip("172.16.0.")
