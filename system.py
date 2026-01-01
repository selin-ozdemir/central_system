import socket
import threading
import json

class CentralSystem:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.robots = {}  # Store connected robots
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Central System running on {self.host}:{self.port}")
    
    def handle_robot(self, conn, addr):
        """Handle incoming robot connections"""
        try:
            # Receive robot registration
            data = conn.recv(1024).decode('utf-8')
            message = json.loads(data)
            
            if message['type'] == 'register':
                robot_name = message['name']
                robot_port = message['port']
                self.robots[robot_name] = {'conn': conn, 'addr': addr, 'port': robot_port}
                print(f"Robot '{robot_name}' registered from {addr}")
                
                # Keep connection open
                while True:
                    pass
        except Exception as e:
            print(f"Error handling robot: {e}")
    
    def send_command(self, robot_name, position):
        """Send command to a specific robot"""
        if robot_name in self.robots:
            command = json.dumps({
                'type': 'command',
                'position': position
            })
            try:
                self.robots[robot_name]['conn'].send(command.encode('utf-8'))
                print(f"Command sent to {robot_name}: go to position {position}")
            except Exception as e:
                print(f"Error sending command: {e}")
        else:
            print(f"Robot '{robot_name}' not found")
    
    def start(self):
        """Start accepting robot connections"""
        # Thread to accept connections
        def accept_connections():
            while True:
                conn, addr = self.server_socket.accept()
                thread = threading.Thread(target=self.handle_robot, args=(conn, addr))
                thread.daemon = True
                thread.start()
        
        accept_thread = threading.Thread(target=accept_connections)
        accept_thread.daemon = True
        accept_thread.start()
        
        # Command interface
        print("\nCommands:")
        print("  send <robot_name> <x> <y>  - Send position command")
        print("  list                        - List connected robots")
        print("  quit                        - Exit\n")
        
        while True:
            try:
                cmd = input("> ").strip().split()
                
                if not cmd:
                    continue
                    
                if cmd[0] == 'quit':
                    break
                elif cmd[0] == 'list':
                    print("Connected robots:", list(self.robots.keys()))
                elif cmd[0] == 'send' and len(cmd) >= 4:
                    robot_name = cmd[1]
                    position = (float(cmd[2]), float(cmd[3]))
                    self.send_command(robot_name, position)
                else:
                    print("Invalid command")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    system = CentralSystem()
    system.start()