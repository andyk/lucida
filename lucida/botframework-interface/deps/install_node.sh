#!/bin/bash

# To get a version of npm that doesn't throw a "Error: CERT_UNTRUSTED"
# we first need to update the system package source list for npm per
# https://wellingguzman.com/notes/upgrading-nodejs-npm-on-ubuntu-14-04
# and https://stackoverflow.com/questions/21855035/ssl-error-cert-untrusted-while-using-npm-command

# Update the system package source list for npm so we will get node.js v10.
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -

# now install npm
sudo apt-get install npm && sudo npm install -g n && sudo n lts
