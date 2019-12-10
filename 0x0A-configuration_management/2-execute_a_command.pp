# A Puppet script to kill the killmenow process
exec { 'pkill killmenow':
  path   => ['/usr/bin', '/usr/sbin']
}
