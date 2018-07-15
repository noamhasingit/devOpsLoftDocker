Instructions:

Virtual box:
    1. Clone the respository to a folder on your local machine
    2. Run "Vgrant up"
    3. Run "Vagrant ssh"
    4. call curl http://0.0.0.0 to check that docker is up and running

Building Docker Image:

   1. cd /vagrant
   2. Docker build -t mydevopsloft .
   3. Docker run -d -p 80:5000 mydevopsloft:latest

