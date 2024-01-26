# OpenSSL Heartbleed Exploit Example

Repo contains files needed to build and run Docker container with a version of OpenSSL vulnerable to the Heartbleed exploit.

Repo also contains Python script demonstrating exploit.

Note: Tests were run on Ubuntu 22.04 machine with Docker installed.

## Testing Steps

1. Build and run Docker container

```bash
cd docker
bash ./docker_build
bash ./docker_run
```

2. Install Python dependency (hexdump) script uses to display bytes (memory) returned from server

```bash
python3 -m pip install hexdump
```

3. Run Python script

```bash
python3 ./heartbleed.py
```

When script runs it will display byte counts sent and received followed by a hex dump of the bytes received from the malformed Heartbeat Request.

Normally a Heartbeat Reply would be an echo back of the Heartbeat Request. We will see that the number of bytes received following the Heartbeat Request is a much larger number of bytes. These bytes contain the Heartbeat Reply followed by the server memory.

The malformed Heartbeat Request sends a payload to echo back of 0 bytes, but a payload length of 65,535. This will result in up to 65,535 bytes (64KB) of server memory being sent back with the Heartbeat Reply. In my testing I never received the full 64 KB back but did consistently receive 40KB+ of server memory back.
