#To run a container
docker run <container_name>

#To check list of running containers
docker container ps


#To check list of exited containers
docker container ps -a

#To remove a container
docker rm <container_id>

#To check list of all images
docker images

#To remove an image
docker rmi <image_name>


#To run a  container  in the background
docker run -d <container name>
#example: docker run -d ubuntu

#To make  sure the container is not exited , make it sleep
docker  container  sleep <seconds>
#example: docker run ubuntu sleep 100


#To pull images  and not to run
docker pull <image>


#To execute a container(Make sure the container is running in the backend using docker  run -d and then execute some command.)
docker  exec <container ID> <commands to execute>
#example: docker run -d ubuntu sleep 100 ; docker exec 982820382a cat /etc/*release
