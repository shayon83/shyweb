#!/bin/bash

set -euxo pipefail

sudo useradd -m -p mysite -s /bin/bash mysite
sudo adduser mysite sudo

sudo apt-get update -y
sudo apt-get install -y python3-pip

echo "mysite" | su - mysite
pip3 install --upgrade pip

pip install pipenv

cd banana

pipenv install --dev
