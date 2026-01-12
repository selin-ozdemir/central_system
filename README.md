# Central Robot Management System

A command-and-control system that manages a network of distributed robot processes, featuring dynamic registration, command routing, and real-time position updates. This project demonstrates practical applications of distributed systems architecture and inter-process communication.

## 🎯 Overview

This system acts as a central hub for coordinating multiple robot agents. Robots register themselves with the central system when they come online, and the system can route position commands to specific robots by name. The architecture simulates real-world scenarios in robotics, IoT, and distributed automation.

## ✨ Key Features

- **Dynamic Robot Registration**: Robots automatically register with the central system upon initialization
- **Command Routing**: Send commands to specific robots by name or ID
- **Real-Time Position Updates**: Track and update robot positions in real-time
- **Process Management**: Handles multiple robot processes concurrently
- **Name-Based Addressing**: Intuitive robot identification system
- **Scalable Architecture**: Can manage dozens of robot agents simultaneously

## 🏗️ System Architecture

```
                    ┌──────────────────────┐
                    │  Central Command     │
                    │     System           │
                    │  (Main Controller)   │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴──────────┐
                    │   Robot Registry    │
                    │  (Active Robots)    │
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
┌───────▼────────┐   ┌─────────▼────────┐   ┌────────▼────────┐
│  Robot Process │   │  Robot Process   │   │  Robot Process  │
│   "Alpha"      │   │    "Beta"        │   │   "Gamma"       │
│  (x, y, theta) │   │  (x, y, theta)   │   │  (x, y, theta)  │
└────────────────┘   └──────────────────┘   └─────────────────┘
```

## 🛠️ Technologies Used

- **Python 3.x**: Core programming language
- **Inter-Process Communication (IPC)**: Message passing between processes
- **Process Management**: Python's multiprocessing module
- **Data Structures**: Efficient robot registry and command queue management

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher

### Steps

1. Clone the repository:
```bash
git clone https://github.com/selin-ozdemir/central_system.git
cd central_system
```

2. Run the central command system:
```bash
python central_system.py
```

3. In separate terminals, launch robot processes:
```bash
python robot.py --name Alpha --x 0 --y 0
python robot.py --name Beta --x 10 --y 5
python robot.py --name Gamma --x -3 --y 7
```

## 📖 How It Works

### Central System
1. **Initialize**: Starts the main control loop and registry
2. **Accept Registrations**: Listens for robot processes coming online
3. **Maintain Registry**: Keeps track of all active robots and their states
4. **Route Commands**: Receives commands and forwards them to the appropriate robot
5. **Monitor Status**: Tracks robot health and connection status

### Robot Processes
1. **Startup**: Robot process initializes with a unique name
2. **Registration**: Registers with the central system
3. **Listen for Commands**: Waits for position update commands
4. **Execute Commands**: Updates position based on received instructions
5. **Report Status**: Sends acknowledgment back to central system

### Command Protocol
```python
# Send position command to specific robot
command = {
    'robot_name': 'Alpha',
    'command_type': 'move',
    'position': {
        'x': 15.5,
        'y': 20.3,
        'theta': 90  # orientation in degrees
    }
}
```

## 💡 Technical Concepts Demonstrated

- **Distributed Systems**: Multiple independent processes working together
- **Service Discovery**: Automatic robot registration and deregistration
- **Message Passing**: Inter-process communication protocol
- **Command Pattern**: Structured command routing and execution
- **State Management**: Tracking system state across distributed components
- **Process Coordination**: Managing lifecycle of multiple concurrent processes

## 📊 Real-World Applications

This architecture pattern is used in:
- **Warehouse Robotics**: Managing fleets of autonomous mobile robots (AMRs)
- **Drone Swarms**: Coordinating multiple UAVs for delivery or surveillance
- **Smart Manufacturing**: Controlling robotic arms and automated machinery
- **IoT Networks**: Managing distributed sensor and actuator networks
- **Autonomous Vehicles**: Fleet management and coordination

## 🧪 Example Usage

```python
# Start central system
$ python central_system.py
Central System initialized. Waiting for robots...

# Register robots
$ python robot.py --name Rover1 --x 0 --y 0
Robot 'Rover1' registered at position (0, 0, 0°)

$ python robot.py --name Rover2 --x 5 --y 5
Robot 'Rover2' registered at position (5, 5, 0°)

# Send command from central system
> move Rover1 to (10, 15, 45)
Command sent to Rover1
Rover1 acknowledged: Moving to (10, 15, 45°)
```

## 🔮 Future Enhancements

- [ ] Add collision detection and avoidance
- [ ] Implement path planning algorithms (A*, Dijkstra)
- [ ] Create visualization dashboard for robot positions
- [ ] Add support for compound commands (waypoint following)
- [ ] Implement fault tolerance and automatic recovery
- [ ] Add real-time telemetry and logging
- [ ] Build RESTful API for external control
- [ ] Integrate with ROS (Robot Operating System)

## 🎓 Educational Value

This project teaches:
- How distributed systems coordinate
- Process-based concurrency in Python
- Design patterns for command and control systems
- Practical robotics software architecture
- Message-based communication protocols

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Enhanced error handling and edge cases
- Performance optimization for large robot fleets
- Additional command types (patrol, follow, dock)
- Unit tests and integration tests

## 👩‍💻 Author

**Selin Ozdemir**
- GitHub: [@selin-ozdemir](https://github.com/selin-ozdemir)
- Email: somqh@umsystem.edu

## 📚 Related Projects

- [Distributed_Clients](https://github.com/selin-ozdemir/Distributed_Clients) - Multi-client chat system

## 📄 License

This project is open source and available under the MIT License.

---

*Inspired by real-world robotics and distributed automation systems*
