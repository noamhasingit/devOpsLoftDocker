#!/bin/bash

echo "Getting updates..."
apt-get update

echo "Installing Python3..."
apt-get install -y python3

echo "Installing pip..."
apt-get install -y python3-pip

echo "Upgrading pip..."
pip3 install --upgrade pip

echo "Installing virtualenv..."
pip install virtualenv

echo "Setting virtual environment..."
virtualenv -p python3 venv
source venv/bin/activate

# echo "Installing additional pips from requirements.txt..."
# pip install -r /vagrant/requirements.txt

# cd /vagrant
# nohup python3 application.py > /dev/null 2>&1 &
echo "Install Docker"
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

apt-get install docker-ce

docker build -t mydevopsloft .
docker run -d -p 80:5000 mydevopsloft:latest

curl http://0.0.0.0

echo "Vagrant UP script completed!"
