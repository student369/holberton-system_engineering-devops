# Puppet manifest to update the ulimit for nginx
exec { 'Update /etc/default/nginx':
  path    => '/bin:/usr/bin:/sbin:/usr/sbin',
  command => 'sed -i "/ULIMIT=/c\ULIMIT=\'-n 20000\'" /etc/default/nginx; sudo service nginx restart',
}
