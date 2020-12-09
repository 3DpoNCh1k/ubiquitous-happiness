python -m pip install django
python -m pip install mysqlclient

sudo echo "#!/bin/sh
exit 0" > /usr/sbin/policy-rc.d

sudo apt-get update
sudo apt-get install mysql-server-5.6


