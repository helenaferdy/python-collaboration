from netmiko import ConnectHandler

device = {
        'device_type': 'cisco_xe',
        'host': '198.18.0.72',
        'username': 'cisco',
        'password': 'cisco',
        'secret': 'cisco'
    }


def command(cmd):
    try:
        net_connect = ConnectHandler(**device)
        net_connect.enable()
        output = net_connect.send_command(cmd)
        return output
    except:
        return "error netmiko"


def backup():
    with open('router.log', 'w') as f:
        f.write(command("show run"))


print(command("show ip int br"))
