import time
from scapy.arch import get_if_addr
from socket import *
from struct import *
from getch import getch

PORT_NUMBER = 2120
TEAM_NAME = 'Moran&Amit\n'
WAITING_SEC = 10
LISTENING_PORT = 13117
ALL_ADRESSES = ''
BUFFER_SIZE = 1024
MESSAGE_COOKIE = 0xfeedbeef
MESSAGE_TYPE = 2
MESSAGE_STRUCT = struct.Struct("lbh")
TEAM_NAME_STRUCT = struct.Struct("<32s")
OFFER = 2

class Client:
    def __init__(self):
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        self.UDP_PORT = 2120
        self.UDP_IP = get_if_addr('eth1')
        self.address = (self.UDP_IP, self.UDP_PORT)
        self.server_addr = 0
    
    # def init_connection(self):
    #     pass

    def start(self):
        print('Client started, listening for offer requests...')
        while True:
            print("In start client method")
            addr = self.looking_for_server()
            self.connect(addr)
            self.send_name()
            self.game_mode()
            self.finish_game()

    def looking_for_server(self):
        self.sock.bind(('', LISTENING_PORT))
        while True:
            print("In looking for server")
            data, addr = self.sock.recvfrom(BUFFER_SIZE)
            print(f"ADDR: {addr}\n DATA: {data}")
            if self.check_message(data):
                return addr  # The server address

    def connect(self, addr):
        print(f"Received offer from {addr}, attempting to connect...")
        self.sock = socket(AF_INET, SOCK_STREAM)
        print(addr, PORT_NUMBER)
        self.sock.connect((addr[0], PORT_NUMBER))
        self.sock.setblocking(0)
        #TODO: maybe should include timeout!
    
    def send_name(self):
        # team_message = TEAM_NAME_STRUCT.pack(TEAM_NAME)
        self.sock.send(TEAM_NAME.encode())

    def check_message(self, data):
        # cookie = data[:4]
        # type_m = data[4:5]
        # port = data[5:7]

        try:
            cookie, type_m, port = MESSAGE_STRUCT.unpack(data)

            # print(data)
            print(f'cookie: {cookie}\n type: {type_m}, port: {port}')

            if not data:
                return False
            if cookie != MESSAGE_COOKIE:
                return False
            elif type_m != MESSAGE_TYPE:
                return False
            elif not 1 <= port <= 65535:
                return False
            else:
                return True
        except Exception as e:
            print (e)
            return False

    def game_mode(self):
        print("In start game_mode method")
        while True:
            try:
                is_game_start_message = self.sock.recv(BUFFER_SIZE)
                if is_game_start_message:
                    print(is_game_start_message.decode())
                    break
            except Exception as error:
                pass
        
        while True:
            c = getch()
            self.sock.send(c.encode())
            

    def finish_game(self):
        print('Server disconnected, listening for offer requests...')

def main():
    client = Client()
    client.start()

if __name__ == '__main__':
    main()