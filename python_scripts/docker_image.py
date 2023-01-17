import sys
import docker
# Docker module needs to be installed to use Python SDK

class docker_controller:
    def __init__(self,username,password,dock_img):
        self.username = None
        self.password = None
        self.dock_img = None

    def signin(self, name, pswd):
        try:
            client = docker.from_env()
            client.login(username=self.username, password=self.password)
            print( "Successfully sign-in Docker Registry \n")
        except:
            print("Failed to sign-in docker registry")
            sys.exit(1)

    def docker_pull(self, docker_img):
        print("docker pull")
        client = docker.from_env()
        image = client.images.pull(docker_img)
        print("Avialbe Docker Images from your hub: \n")
        for image in client.images.list():
            container_id = image.id
            print(client.images.get(image.id))

    def docker_push():
        print("docker push")

if __name__ == "__main__" :
    while True:
        str1 = raw_input("Please enter your docker ID: \n")
        str2 = raw_input("please enter your docker password: \n")
        str3 = raw_input("please enter name of the docker image: \n")
        controller = docker_controller(str1,str2,str3)
        controller.signin(str1,str2)
        controller.docker_pull(str3)
        out = raw_input("Type \"q\" to exit the loop, otherwise type \"y\" \n")
        if out == 'q':
            break
    print("Docker pulling script is terminated.")
