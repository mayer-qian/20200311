import json

data = {"routers:": [{"hostname": "R1", "IP": "192.168.1.1", "Interface": "Eth0"},
                     {"hostname": "R2", "IP": "192.168.1.2", "Interface": "Eth1"}]}

a = json.dumps(data, indent=4)
print(a)


#b = json.loads(a)
routers = json.loads(a)
#print(b)
#print(b["routers:"])
#print(b["routers:"][1]['Interface'])

#for router in b["routers:"]:
#    print(router["IP"])

class router_sign():
    def __init__(self, name, ip, interface):
        self.name = name
        self.ip = ip
        self.interface = interface
        self.say_hello()

    def say_hello(self):
        print("{} sign already".format(self.name))

router_list = []

for msg in routers['routers:']:
    router_list.append(router_sign(msg['hostname'], msg['IP'], msg['Interface']))
print(router_list[0].name)



