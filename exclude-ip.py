#!/usr/bin/python3
import ipaddress

def get_subnet_ip():
    # Prompt for a valid subnet
    while True:
        subnet_input = input("Original subnet (e.g. 192.168.1.0/24): ")

        try:
            # Convert string input to IP Network
            subnet = ipaddress.ip_network(subnet_input, strict = True)

            # Checks for subnet mask
            if subnet.prefixlen == 32:
                print("Please include the subnet mask (e.g. 192.168.1.0/24)")
            else:
                break

        # Validates input is a valid subnet
        except ValueError:
            print("Please enter a valid network, with subnet mask (e.g. 192.168.1.0/24)")

    while True:
        # Prompt for a valid host IP
        ip_input = input("IP to exclude (e.g. 192.168.1.50): ")

        try:
            # Convert string input to IP Address
            ip = ipaddress.ip_address(ip_input)

            # Checks if IP is in Subnet, exits script if not
            if not ip in subnet:
                print(f"{ip} is not in {subnet}.")
                exit()
            else:
                break

        except ValueError:
            print("Please enter a valid single IP, without subnet mask (e.g. 192.168.1.50)")

    return subnet, ip

def split_subnet(subnet, ip):
    # If the subnet can't be split further, return it
    if subnet.prefixlen == 32:
        return [subnet]

    # Calculate the prefix for the new subnets
    new_prefix = subnet.prefixlen + 1

    # Create the two new subnets
    subnet1 = ipaddress.ip_network(f"{subnet.network_address}/{new_prefix}")
    subnet2_start = int(subnet.network_address) + 2**(32 - new_prefix)
    subnet2 = ipaddress.ip_network(f"{ipaddress.ip_address(subnet2_start)}/{new_prefix}")

    # Recursively split the subnet that contains the IP
    if ip in subnet1:
        return split_subnet(subnet1, ip) + [subnet2]
    else:
        return [subnet1] + split_subnet(subnet2, ip)

def exclude_ip(subnet, ip):
    # Split the subnet
    new_subnets = split_subnet(subnet, ip)

    # Remove the IP from the list of new subnets
    new_subnets = [str(new_subnet) for new_subnet in new_subnets if ip not in new_subnet]

    return new_subnets

def main():
    subnet, ip = get_subnet_ip()
    print(*exclude_ip(subnet, ip), sep='\n')

# Execute function
main()
