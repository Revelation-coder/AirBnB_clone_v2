#!/usr/bin/env bash

# Double the number of webservers.
sudo apt-get update
sudo apt-get -y install nginx

# Create and configure index.html
echo 'Holberton School' | sudo tee /var/www/html/index.html > /dev/null

# Create 404.html
echo "Page not found" | sudo tee /var/www/error/404.html > /dev/null

# Add redirect and error_page configurations
sudo sed -i '/server_name _/a location /redirect_me { rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlw\u4? permanent; }' /etc/nginx/sites-available/default
sudo sed -i '/server_name _/a error_page 404 /404.html;\n\tlocation = /404.html {\n\t\troot /var/www/error/;\n\t\tinternal;\n\t}' /etc/nginx/sites-available/default

# Add X-Served-By header
sudo sed -i "/server_name _/a add_header X-Served-By \$HOSTNAME;" /etc/nginx/sites-available/default

# Create necessary directories for web_static deployment
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create index.html for web_static
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership of directories to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration for serving web_static
sudo sed -i '/^\tlocation \/ {$/ i\\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n}' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
