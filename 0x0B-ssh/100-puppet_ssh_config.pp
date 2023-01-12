file { '/etc/ssh/ssh_config':
  ensure  => file,
  content => 'Host 75361-web-01\nIdentityFile ~/.ssh/school\nPasswordAuthentication no'
} 
