sudo /etc/init.d/mysql start
mysql -u root -e "create database stepik_web;"
mysql -u root -e "grant all privileges on stepik_web.* to 'web'@'localhost' with grant option;"
python ask/manage.py makemigrations
python ask/manage.py migrate
