DISTRO_CODE     = kinetic
#
# Checkmk build specific packages  below
#
OS_PACKAGES     =
OS_PACKAGES    += libcap2-bin # needed for setting special file permissions
OS_PACKAGES    += cron # needed for sites cron jobs
OS_PACKAGES    += time # needed for mk-job
OS_PACKAGES    += traceroute # needed for Checkmk parent scan
OS_PACKAGES    += curl
OS_PACKAGES    += dialog
OS_PACKAGES    += dnsutils
OS_PACKAGES    += graphviz
OS_PACKAGES    += apache2
OS_PACKAGES    += apache2-utils # contains htpasswd2
OS_PACKAGES    += libevent-2.1-7a
OS_PACKAGES    += libltdl7
OS_PACKAGES    += libnl-3-200
OS_PACKAGES    += libpango-1.0-0
OS_PACKAGES    += libperl5.34
OS_PACKAGES    += libreadline8
OS_PACKAGES    += libuuid1
OS_PACKAGES    += libxml2
OS_PACKAGES    += php-cli
OS_PACKAGES    += php-cgi
OS_PACKAGES    += php-gd
OS_PACKAGES    += php-sqlite3
OS_PACKAGES    += php-json
OS_PACKAGES    += php-pear
OS_PACKAGES    += rsync
OS_PACKAGES    += smbclient
OS_PACKAGES    += rpcbind # otherwise missing path in util.pm
OS_PACKAGES    += unzip
OS_PACKAGES    += xinetd
OS_PACKAGES    += freeradius-utils
#
# Checkmk build specific packages below
#
OS_PACKAGES    += libpcap0.8 # needed for cmc
OS_PACKAGES    += rpm # needed by msitools/Agent Bakery
OS_PACKAGES    += binutils # needed by msitools/Agent Bakery
OS_PACKAGES    += lcab # needed for creating MSI packages
OS_PACKAGES    += libgsf-1-114 # needed by msitools/Agent Bakery
OS_PACKAGES    += libglib2.0-0 # needed by msitools/Agent Bakery
OS_PACKAGES    += cpio # needed for Agent bakery (solaris pkgs)
OS_PACKAGES    += libfl2 # needed by heirloom-pkgtools
OS_PACKAGES    += poppler-utils # needed for preview of PDF in reporting
OS_PACKAGES    += libffi8ubuntu1 # needed for pyOpenSSL and dependant
OS_PACKAGES    += libpq5
USERADD_OPTIONS   =
ADD_USER_TO_GROUP = gpasswd -a %(user)s %(group)s
PACKAGE_INSTALL   = apt-get -y update ; apt-get -y install
ACTIVATE_INITSCRIPT = update-rc.d %s defaults
APACHE_CONF_DIR   = /etc/apache2/conf.d
APACHE_INIT_NAME  = apache2
APACHE_USER       = www-data
APACHE_GROUP      = www-data
APACHE_VERSION    = 2.4.46
APACHE_CTL        = /usr/sbin/apache2ctl
APACHE_MODULE_DIR = /usr/lib/apache2/modules
APACHE_MODULE_DIR_64 = /usr/lib/apache2/modules
HTPASSWD_BIN      = /usr/bin/htpasswd
APACHE_ENMOD      = a2enmod %s
PHP_FCGI_BIN      = /usr/bin/php-cgi
BECOME_ROOT       = sudo su -c
ARCH              = $(shell dpkg --print-architecture)
MOUNT_OPTIONS     =
INIT_CMD          = /etc/init.d/%(name)s %(action)s