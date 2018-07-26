Intro
-------
This project was a test to build in order to move https://github.com/DevOpsLoft/DevOpsLoft/ to a docker container
I have duplicated the project locally to my own repository and build docker container and pushed it to a VirtualBox ubuntu machine.

The project can run locally on your machine using a VirtualBox machine running Ubuntu

Prerequisite
-------------
1. Make sure you have Vagrant on your machine: https://www.vagrantup.com/docs/installation/
2. Make sure you have VirtualBox on your machine: https://www.virtualbox.org/wiki/Downloads

Instructions:
-------------
1. Clone the respository to a folder on your local machine: 
        git clone https://github.com/noamhasingit/devOpsLoftDocker
2. Change directory to the project folder and run:
       "Vgrant up"
3. Run "Vagrant ssh"
4. Run "curl http://0.0.0.0" to check that docker is up and running

Creating standalone Docker Image:
----------------------
1. Run "Vagrant ssh" 
2. cd /vagrant which is the default Vagrant directory
3. Run "Docker build -t mydevopsloft ." to build the Image
4. Run "Docker run -d -p 80:5000 mydevopsloft:latest" to execute the container
5. Run "curl http://0.0.0.0" to check that docker is up and running

