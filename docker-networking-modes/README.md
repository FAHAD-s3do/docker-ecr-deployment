# Docker Networking Modes: Bridge, Host, and None

## Objectives
Demonstrate and validate Docker's three core networking modes — bridge, host, and none — on an AWS EC2 instance, illustrating the network isolation trade-offs each mode provides for containerized workloads.

## Tools Used
- Docker
- Nginx (test containers)
- AWS EC2 (Ubuntu host)

## Key Skills Demonstrated
- Docker bridge networking and internal container IP addressing
- Host networking mode and its isolation trade-offs (direct host network stack access)
- None networking mode for network-isolated, security-conscious containers
- Container network inspection via `docker inspect`
- Practical understanding of network isolation boundaries — relevant to container security and lateral movement analysis

## Troubleshooting Log
- **Missing dependency:** `curl` was not pre-installed on the Ubuntu EC2 instance, blocking host-mode network verification. Resolved via `sudo apt install curl -y`.

## Results
| Mode | Behavior Observed |
|---|---|
| Bridge (default) | Container received an isolated internal IP (172.17.0.2) reachable via Docker's virtual bridge |
| Host | Container bypassed Docker networking entirely, directly exposing Nginx on the host's port 80 (`curl localhost` succeeded with no port mapping) |
| None | Container received no network interface beyond loopback — fully isolated from all network communication |
