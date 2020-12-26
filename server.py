import time
from socket import *

TEAM_NAME = 'Moran&Amit\n'
WAITING_SEC = 10
BUFFER = 1024
UDP_ADDR_TUPLE = ("", 3117)
MESSAGE_STRUCT = Struct("4c 1c 2c")


class Server:
    def __init__(self):
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.sock.bind(UDP_ADDR_TUPLE)
        self.SERVER_IP = get_if_addr('eth1') # TODO check how to get the server's ip
        self.address = (self.UDP_IP, self.UDP_PORT)
        self.server_addr = 0
        self.team_names = []
        self.groups = []

    def assign_team_names_to_groups(self):
        for team_name in self.team_names:
            


    def start():
        print(f"Server started, listening on IP address {self.SERVER_IP}")
        curr_time = time.time()
        while time.time() - curr_time == 1:
            curr_time = curr_time + 1
            offer_message = : '0xfeedbeef' + '0x2' + "" #check what is the third thing
            self.sock.sendto(offer_message, addr) # TODO sent in broadcast + manage broadcast




def main():
    server = Server()
    server.start()

if __name__ == '__main__':
    main()