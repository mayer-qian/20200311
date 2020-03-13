import time

class SERVER():
    def __init__(self):
        self.url = 'yeslab.com'
        self.data = {'route':['to_192.168.0.0', 'to_172.8.0.0']}
        self.keys = list(self.data.keys())
        self.announce()
    def announce(self):
        print("my ip: {}".format(self.url))
        print("my services: {}".format(self.keys))
    def response(self, receive):
        msg =  receive()
        print("SERVER API Processing")
        time.sleep(2)
        if msg == self.url + '/' + self.keys[0]:
            return self.data['route']
server = SERVER()

