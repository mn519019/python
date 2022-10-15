# Take the form of w.x.y.z:port
# port range must be in(1,xxxxx)
import re

def validate_ip4(str):
    print("Validating the given ipv4 form...")
    result = True
    # Regex 
    match = re.search(r'([\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}):([\d]{1,5})', str)
    port_match = re.search(r':([\d]{1,})', str)
    port_check = port_match.span()[1]-port_match.span()[0]

    if match is None:
        result = False
        print("Please check your ip address!!!", result)
    elif (port_check -1) > 5:
        result = False
        print("Please check your port!!!", result)
        #print("Checking the ip result of ",port_match)
        #rint("Checking the port length.. ",port_check-1)
    else:
        return result

# Test Case
print("Result: ",validate_ip4('10.17.25.50:10000')) # Expecting True
print("Result2: ",validate_ip4('100.171.255.250:880')) # Expecting True
print("Result3: ",validate_ip4('100.171.255.250:882220')) # Expecting False
print("Result3: ",validate_ip4('100.171.2551.250:882220')) # Expecting False
