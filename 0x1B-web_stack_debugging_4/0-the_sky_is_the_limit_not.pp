# Fix number of maximum open files per process

exec { 'fix-nginx':
  command => "/bin/sed -i /etc/default/nginx -e 's/15/4096/'",
}

exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
  require => Exec['fix-nginx']
}
