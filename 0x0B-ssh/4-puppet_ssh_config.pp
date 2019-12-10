# A Puppet script to modify the SSH config file.
file { '/home/vagrant/.ssh/config':
  content => 'Host *
#   ForwardAgent no
#   ForwardX11 no
#   ForwardX11Trusted yes
#  SSH Configuration file
   PasswordAuthentication no
   IdentityFile ~/.ssh/holberton'
}
