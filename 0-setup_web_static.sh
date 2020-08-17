#!/usr/bin/env bash
# script that sets up your web servers for the
# deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data
sed -i '/listen 80 default_server;/ a /\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
