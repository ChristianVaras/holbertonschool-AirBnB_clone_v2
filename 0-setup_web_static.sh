#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

sudo apt -y update
sudo apt -y upgrade
sudo apt -y install nginx
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
chown -R ubuntu:ubuntu /data/
echo "Hello World" | tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current

search="^\t\}$"
adding="\t\}\n\n\tlocation \/hbnb_static\/ \{\n\t\talias \/data\/web_static\/current\/;\n\t\}"

sudo sed -i "0,/$search/s//$adding/" /etc/nginx/sites-available/default
sudo service nginx restart
