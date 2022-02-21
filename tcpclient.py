import socket
from loguru import logger

target_host = "www.google.com"
target_port = 80

logger.info("We create a socket object")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

logger.info("We connect the client")
client.connect((target_host, target_port))

logger.info("We send some data")
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

logger.info("We receive some data")
response = client.recv(4096)

print(response)
