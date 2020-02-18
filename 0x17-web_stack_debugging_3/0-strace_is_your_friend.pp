# Puppet manifest to correct a typo in wp-settings.php
exec { 'Update /var/www/html/wp-settings.php':
  path    => '/bin:/usr/bin:/sbin:/usr/sbin',
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
}
