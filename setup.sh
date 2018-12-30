#!/bin/bash

WEBROOT="/var/www"
APACHE_CONF="/etc/apache2/sites-available"


if [[ $(id -u) -ne 0 ]]
then
	echo "must be root"
	exit
fi

# install stuff
echo "[installing packages]"
apt-get install php7.2 apache2


# move apache2 conf file and setup soft link
echo "[moving conf file]"
cp ./ddh.conf $APACHE_CONF/ddh.conf

echo "[linking file to web root]"
ln -s $(pwd)/ddh $WEBROOT/ddh
