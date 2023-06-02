# Subnet IP Exclusion Tool

Python script to exclude a specific IP address from a given subnet. It splits the subnet into smaller subnets and removes the specified IP address from the resulting list of subnets.

## Prerequisites

- Python 3.x

## Usage

1. Run the script using Python 3.x:

   ```shell
   py exclude-ip.py
   ```

2. Enter the original subnet in the format `<network_address>/<prefix_length>`. For example:

   ```shell
   Original subnet (e.g. 192.168.1.0/24): 192.168.1.0/24
   ```

   Note: The subnet should include the subnet mask.

3. Enter the IP address you want to exclude from the subnet. For example:

   ```shell
   IP to exclude (e.g. 192.168.1.50): 192.168.1.50
   ```

   Note: The IP address should not include the subnet mask.

4. The script will split the subnet and exclude the specified IP address. It will display the resulting subnets without the excluded IP address.

## How it works

1. The script imports the `ipaddress` module, which provides classes for working with IP addresses and networks.

2. The `get_subnet_ip` function prompts the user to enter a valid subnet and IP address. It performs input validation to ensure the entered values are in the correct format and within the subnet.

3. The `split_subnet` function takes a subnet and an IP address as input. It recursively splits the subnet until it reaches the smallest possible subnets that can't be split further. It returns a list of subnets.

4. The `exclude_ip` function calls the `split_subnet` function to obtain the list of subnets. It then removes the specified IP address from the list and returns the updated list.

5. The `main` function calls the `get_subnet_ip` function to retrieve the subnet and IP address. It then calls the `exclude_ip` function to exclude the IP address from the subnet. Finally, it prints the resulting subnets.

6. The script executes the `main` function to start the subnet IP exclusion process.
