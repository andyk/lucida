#!/bin/bash
sudo add-apt-repository -y ppa:jonathonf/python-3.6
sudo apt-get -y update
sudo apt-get -y install python3.6
sudo apt-get -y install python3-pip

sudo pip3 install virtualenv
virtualenv python_3_6 -p /usr/bin/python3.6
source python_3_6/bin/activate
pip install --upgrade distribute
pip install --upgrade pip
pip install -r python3_requirements.txt
deactivate
