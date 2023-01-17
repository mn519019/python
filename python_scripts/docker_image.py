import docker
# Docker module needs to be installed to use Python SDK

class docker_pull:
    def signin(self,str1,str2,str3):
        try:
            client = docker.from_env()
            client.login(username=str1, password=str2)
            print( "Successfully sign-in Docker Registry \n")
            image = client.images.pull(str3)
            print("Avialbe Docker Images from your hub: \n")
            for image in client.images.list():
                container_id = image.id
                print(client.images.get(image.id))
        except:
            print("Failed to sign-in docker registry")


if __name__ == "__main__" :
    while True:
        str1 = raw_input("Please enter your docker ID: \n")
        str2 = raw_input("please enter your docker password: \n")
        str3 = raw_input("please enter name of the docker image: \n")
        dockerpull = docker_pull()
        dockerpull.signin(str1,str2,str3)
        out = raw_input("Type q to exit the loop: \n")
        if out == 'q':
            break
    print("Docker pulling script is terminated.")
