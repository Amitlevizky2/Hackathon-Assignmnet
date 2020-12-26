import time
from socket import *

PORT_NUMBER = 2021
TEAM_NAME = 'Moran&Amit\n'
WAITING_SEC = 10

class Client:
    def __init__(self):
        self.sock = 0
        self.UDP_PORT = 2120
        self.UDP_IP = get_if_addr('eth1')
        self.address = (self.UDP_IP, self.UDP_PORT)
        self.server_addr = 0
    
    # def init_connection(self):
    #     pass

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

    def game_mode(self):
        self.sock.send(TEAM_NAME)

    def check_message(message, name, addr):
        if message[0:4].encode() != '0xfeedbeef':
            return ""
        else if message[4:5].encode() != '0x2':
            return "" # TODO think how get offer gets here
        else if message[5:7].encode() != '0xfeedbeef': # TODO didnt understand
            return ""
        else:
            return team_name.decode()

    def game_mode(self):
        start_time = time.time()
        while time.time() - start_time < WAITING_SEC: 
            c = sys.stdin.read(1)
            self.sock.send(c)
            # TODO take care of data coming in over TCP

    def finish_game(self):
        print('Server disconnected, listening for offer requests...')
        return self.looking_for_server()

def main():
    client = Client()
    client.start()

if __name__ == '__main__':
    main()