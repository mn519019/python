# Docker module needs to be installed to use Python SDK
# This scripts uses pyhon version 2 
# To do so pip install docker

import sys
import docker

class docker_controller:
    def __init__(self,username,password,docker_img):
        self.username = username
        self.password = password
        self.docker_img = docker_img

    def signin(self,username,password):
        try:
            client = docker.from_env()
            client.login(username=self.username, password=self.password)
            print( "Successfully sign-in Docker Registry \n")
        except:
            print("Failed to sign-in docker registry")
            sys.exit(1)

    def docker_pull(self,docker_img):
        print("docker pull")
        client = docker.from_env() 
        image = client.images.pull(docker_img)
        print("Avialbe Docker Images from your hub: \n")
        for image in client.images.list():
            container_id = image.id
            print(client.images.get(image.id))

    def docker_push(self,docker_img):
        client = docker.from_env()
        for line in client.images.push(docker_img,tag="latest",stream=True, decode=True):
            print(line)

    def docker_remove(self,docker_img):
        client = docker.from_env()
        rmi = client.images.remove(docker_img)
        print("Avialbe Docker Images from your hub: \n")
        for image in client.images.list():
            container_id = image.id
            print(client.images.get(image.id))

if __name__ == "__main__" :
    push = {'push','Push', 'PUSH'}
    pull = {'pull','Pull', 'PULL'}
    remove = {'remove', 'Remove', 'REMOVE'}
    while True:
        str1 = raw_input("Please enter your docker ID: \n")
        str2 = raw_input("please enter your docker password: \n")
        str3 = raw_input("please enter name of the docker image: \n")
        controller = docker_controller(str1,str2,str3)
        controller.signin(str1,str2)
        option = raw_input("Type \"push or pull or remove\" to complete the operation: \n ")

        if option in push:
            controller.docker_push(str3)
        elif option in pull: 
            controller.docker_pull(str3)
        elif option in remove:
            controller.docker_remove(str3)
        else:
            print("Required input is not typed.")
            sys.exit(1)

        out = raw_input("Type \"q\" to exit the loop, otherwise type \"y\" \n")
        if out == 'q':
            break
    print("Docker pulling script is terminated.")
