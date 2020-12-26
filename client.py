import time
from scapy.arch import get_if_addr
from socket import *

PORT_NUMBER = 2021
TEAM_NAME = 'Moran&Amit\n'
WAITING_SEC = 10
LISTENING_PORT = 13117
ALL_ADRESSES = ''
BUFFER_SIZE = 1024


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
            self.finish_game()

    def looking_for_server(self):
        self.sock.bind((ALL_ADRESSES, LISTENING_PORT))
        while True:
            data, addr = self.sock.recvfrom(BUFFER_SIZE)
            if check_message(data):
                return addr  # The server address

    def connect(self, addr):
        print(f"Received offer from {addr}, attempting to connect...")
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect((addr, PORT_NUMBER))
        self.sock.setblocking(0)
        #TODO: maybe should include timeout!
    
    def send_name(self):
        self.sock.send(TEAM_NAME)

    def check_message(message, name, addr):
        if not data:
            return False
        if message[0:4].encode() != '0xfeedbeef':
            return False
        else if message[4:5].encode() != '0x2':
            return False
        else if not 1 <= int(message[5:7].encode()) <= 65535
            return False
        else:
            return True

    def game_mode(self):
        while True:
            is_game_start_message = self.sock.recv(BUFFER_SIZE)
            if is_game_start_message:
                print(is_game_start_message[0])
                break

        while True: # TODO: If game is over? stop game 
            is_game_start_message = self.sock.recv(BUFFER_SIZE)

            if is_game_start_message:
                print(is_game_start_message[0])
                break

            c = sys.stdin.read(1)
            self.sock.send(c)

    def finish_game(self):
        print('Server disconnected, listening for offer requests...')

def main():
    client = Client()
    client.start()

if __name__ == '__main__':
    main()