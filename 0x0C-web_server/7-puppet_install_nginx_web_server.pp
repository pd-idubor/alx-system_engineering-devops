#Install and config nginx
include stdlib

$site = 'https://www.youtube.com/watch?v=PCfiqY05BpA'
$aux = "\trewrite ^/redirect_me/$ ${site} permanent;"


exec {'Update':
  command => '/usr/bin/apt-get update'
}

exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
  require => Package['nginx']
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update packages']
}

#Default page
file {'/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World!'
  mode    => '0644',
  owner   => 'root',
  group   => 'root'
}


#Redirection
file_line {'Redirect':
  path    => '/etc/nginx/sites-available/default'
  after   => 'server_name\ _;',
  line    => $aux,
  notify  => Exec['restart nginx'],
  require => File['/var/www/html/index.html']
}
