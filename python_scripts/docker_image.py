import docker
# Docker module needs to be installed to use Python SDK

class docker_pull:
    def signin(self,str1,str2):
        try:
            client = docker.from_env()
            client.login(username=str1, password=str2)
            print( "Successfully sign-in Docker Registry \n")
            #image = client.images.pull("alpine")
            print("Avialbe Docker Images from your hub: \n")
            for image in client.images.list():
                print(image.id)
        except:
            print("Failed to sign-in docker registry")


if __name__ == "__main__" :
    str1 = raw_input("Please enter your docker ID: \n")
    str2 = raw_input("please enter your docker password: \n")
    dockerpull = docker_pull()
    dockerpull.signin(str1,str2)