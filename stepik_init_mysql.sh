sudo /etc/init.d/mysql start
mysql -u root -e "create database stepic_web;"
mysql -u root -e "grant all privileges on stepic_web.* to 'web'@'localhost' with grant option;"
python ask/manage.py makemigrations
python ask/manage.py migrate
