# done
def find_class_and_subnet(ip_address): 
    # Split the IP address into octets 
    octets = ip_address.split(".") 
     
    # Convert the first octet to an integer 
    first_octet = int(octets[0]) 
     
    # Determine the class of the IP address 
    if 0 <= first_octet <= 127: 
        ip_class = "A" 
        subnet_mask = "255.0.0.0" 
    elif 128 <= first_octet <= 191: 
        ip_class = "B" 
        subnet_mask = "255.255.0.0" 
    elif 192 <= first_octet <= 223: 
        ip_class = "C" 
        subnet_mask = "255.255.255.0" 
    elif 224 <= first_octet <= 239: 
        ip_class = "D" 
        subnet_mask = "Reserved for Multicast" 
    elif 240 <= first_octet <= 255: 
        ip_class = "E" 
        subnet_mask = "Reserved for Future Use" 
    else: 
        ip_class = "Invalid" 
        subnet_mask = "N/A" 
 
    return ip_class, subnet_mask 
 
# Input IP address 
ip_address = input("Enter an IP address: ") 
 
# Find the class and subnet mask 
ip_class, subnet_mask = find_class_and_subnet(ip_address) 
 
print(f"IP Address: {ip_address}") 
print(f"Class: {ip_class}") 
print(f"Subnet Mask: {subnet_mask}") 
