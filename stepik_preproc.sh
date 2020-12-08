sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6

sudo pip3 uninstall django
sudo pip3 install django
sudo ln -sf /usr/bin/python3.6 /usr/bin/python
sudo ln -sf /usr/bin/python3.6 /usr/bin/python3

export PYTHONPATH=/usr/local/lib/python3.4/dist-packages

