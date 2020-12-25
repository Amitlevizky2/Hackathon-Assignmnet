PORT_NUMBER = 2021
TEAM_NAME = 'Moran&Amit\n'

class Client:
    def __init__(self):
        self.sock = 0
        self.UDP_PORT = 2120
        self.UDP_IP = get_if_addr('eth1')
        self.address = (self.UDP_IP, self.UDP_PORT)
        self.server_addr = 0
    
    def init_connection(self):
        pass

    def start():
        print('Client started, listening for offer requests...')

        while True:
            addr = self.looking_for_server()
            self.connect(addr)
            self.send_name(addr)
            self.game_mode()



    def looking_for_server(self):
        while True:
            data, addr = self.sock.recvfrom()
            if data:
                return addr  # The server address

    def connect(self, addr):
        print(f"Received offer from {addr}, attempting to connect...")
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect((addr, PORT_NUMBER))
        #TODO: maybe should include timeout!

    def send_name(self):
        self.sock.send(TEAM_NAME)

def main():
    client = Client()
    client.start()

if __name__ == '__main__':
    main()