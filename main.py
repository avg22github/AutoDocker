import docker
import os
import time

client = docker.from_env()

os.system('cat ASCII.txt')

image = 'httpd'
binding = {80: 8080}

print("Downloading Image...")
client.images.pull(image)
time.sleep(3)
print("Image downloaded")
print("Running container..")
client.containers.run(image, detach=True, ports=binding)
time.sleep(3)
print("Container running with the port binding " + str(binding))