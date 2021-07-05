#!/usr/local/bin/bash

yum upgrade -y
yum install python3 -y
yum install vim -y
yum install git -y
yum install tree -y
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
dnf install unzip -y
unzip awscliv2.zip
sudo ./aws/install
yum install wget -y
yum install mesa-libGL -y
yum install httpd -y

git clone https://github.com/i-adarsh/Plate-Detection-Model.git
cd Plate-Detection-Model/
mv Object_detection.ipynb yolov3_testing.cfg /var/www/cgi-bin/


git clone https://github.com/i-adarsh/Kubernetes-Python-CGI.git
cd Kubernetes-Python-CGI/
pip3 install --upgrade pip
pip3 install flask
pip3 install boto3
pip3 install scikit-build
pip3 install opencv-python
pip3 install glob2
pip3 install numpy
pip3 install matplotlib
pip3 install torch
pip3 install easyocr
pip3 install imutils


sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm -y
sudo dnf upgrade -y

sudo rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm -y 
sudo subscription-manager repos --enable "rhel-*-optional-rpms" --enable "rhel-*-extras-rpms"
sudo yum update
sudo yum install snapd -y
sudo systemctl enable --now snapd.socket
sudo ln -s /var/lib/snapd/snap /snap
sudo snap install tesseract --edge