import time
import thread
import random
from scapy.arch import get_if_addr
from socket import *

TEAM_NAME = 'Moran&Amit\n'
WAITING_SEC = 10
BUFFER = 1024
UDP_ADDR_TUPLE = ("", 13117)
MESSAGE_STRUCT = Struct("4c 1c 2c")
BROADCASTING_PORT = 13117
SERVER_TCP_PORT = 2120
DRAW = 0
GROUP1 = 1
GROUP2 = 2


class Server:
    def __init__(self):
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.sock.bind(UDP_ADDR_TUPLE)
        self.SERVER_IP = get_if_addr('eth1') # TODO check how to get the server's ip
        self.address = (self.UDP_IP, self.UDP_PORT)
        self.server_addr = 0
        self.is_game_on = False
        self.team_names = []
        self.groups = {'Group 1': {},
                       'Group 2': {}}
        self.scores = {}  #  {name: score}

        init_tcp()
        init_udp()

    def init_tcp(self):
        server_socket = self.sock.socket(AF_INET,SOCK_STREAM)
        server_socket.bind(('',SERVER_TCP_PORT))
        server_socket.listen(1)
    
    def init_udp(self):
        server_socket = self.sock.socket(AF_INET, SOCK_DGRAM)
        server_socket.bind('', BROADCASTING_PORT)
    
    def start(self):
        while True:
            self.is_game_on = False
            self.groups['Group 1'] = {}
            self.groups['Group 2'] = {}
            self.scores = {}
            thread.start_new_thread(tcp_listen)  #  Start listining to TCP clinets requests (Get names)
            thread.start_new_thread(broadcast)   #  Start broadcasting 'offer' messages
    
    def tcp_listen(self):
        print(f"Server started, listening on IP address {self.SERVER_IP}")
        start_time = time.time()
        while(time.time() - start_time <= 10):
            clinet_socket, addr = self.sock.accept()
            name = clinet_socket.recv(BUFFER)
            group_number = insert_to_group(name, clinet_socket, addr)
            client_socket.settimeout(10.0)
            
            
        group_1_names = [name for name in self.groups['Group 1'].keys()]
        group_2_names = [name for name in self.groups['Group 2'].keys()]

        start_game_message = 'Welcome to Keyboard Spamming Battle Royale.\n'

        group_1_names_str = '\n'.join(group_1_names)
        start_game_message += 'Group 1:\n==\n'
        start_game_message += group_1_names_str


        group_2_names_str = '\n'.join(group_2_names)
        start_game_message += 'Group 2:\n==\n'
        start_game_message += group_2_names_str

        start_game = False

        for key,value in self.groups.items():
            for name,tup in value.items():
                #{name: (client_socket, addr)}
                thread.start_new_thread(self.handle_client, (tup[0], tup[1], start_game_message, name))
        
        start_time = time.time()
        while(time.time() - start_time <= 10):
            self.is_game_on = True
        self.is_game_on = False

        typed_chars_group_1 = self.caculate_typed_chars('Group 1')
        typed_chars_group_2 = self.caculate_typed_chars('Group 2')

        results_message = self.get_results_message(typed_chars_group_1, typed_chars_group_2)

        # send result message to each of the teams(clients)
        # for key,value in self.groups.items():
        #     for value in value.values():
        #         client_socket = value[0]
        #         client_socket.send(results_message)
        #         client_socket.close()
        
        print(results_message)
        


    def insert_to_group(self, name, clinet_socket, addr):
        group_number = random.randint(0,1)
        self.groups['Group ' + str(group_number + 1)][name] = (clinet_socket, addr)
        return group_number + 1

    def handle_client(self, client_socket, addr, start_game_message, name):
        while not self.is_game_on:
            pass
        
        client_socket.send(start_game_message)
        while self.is_game_on:
            try:
                letter = connectionSocket.recv(BUFFER)
                #  Chacek ketter validation
                self.score[name] += 1
            except Exception as error:
                print(error)

    def caculate_typed_chars(group_name):
        typed = 0
        for key,value in self.scores.items():
            if key in self.groups[group_name].keys():
                typed += value
        return typed

    def broadcast(self):
        start_time = time.time() 
        curr_time = start_time
        while(time.time() - start_time <= 10):
            while time.time() - curr_time == 1:
                curr_time = curr_time + 1
                offer_message = '0xfeedbeef' + '0x2' + "" #check what is the third thing
                self.sock.sendto(message, ('<broadcast>', BROADCASTING_PORT)) # TODO sent in broadcast + manage broadcast

def get_results_message(typed_chars_group_1, typed_chars_group_2):
    winner = ''
    winner_group_names = []

    if typed_chars_group_1 > typed_chars_group_2:
        winner = f"group {GROUP1} wins"
        winner_group_names = [name for name in self.groups['Group 1'].keys()]
    elif typed_chars_group_1 < typed_chars_group_2:
        winner = f"group {GROUP2} wins"
        winner_group_names = [name for name in self.groups['Group 2'].keys()]
    else:
        winner = 'Draw. Both groups typed the same number of characters.'
    
    results_message = 'Game over!\n'
    results_message += f'Group 1 typed in {typed_chars_group_1} characters.'
    results_message += f'Group 2 typed in {typed_chars_group_2} characters.\n'
    results_message += winner
    results_message += 'Congratulations to the winners:\n=='
    results_message += '\n'.join(winner_group_names)

def main():
    server = Server()
    server.start()

if __name__ == '__main__':
    main()