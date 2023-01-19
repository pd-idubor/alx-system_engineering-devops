# Install and config Nginx
include stdlib

$site= 'https://www.youtube.com/watch?v=QH2-TGUlwu4'
$aux = "\trewrite ^/redirect_me/$ ${site} permanent;"
$head = "add_header X-Served-By \$hostname;"


exec { 'update packages':
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

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World!',
  mode    => '0644',
  owner   => 'root',
  group   => 'root'
}

file_line { 'Set 301 redirection':
  ensure   => 'present',
  after    => 'server_name\ _;',
  path     => '/etc/nginx/sites-available/default',
  multiple => true,
  line     => $aux,
  notify   => Exec['restart nginx'],
  require  => File['/var/www/html/index.html']
}

file_line { 'Set header':
  ensure   => 'present',
  after    => 'http {',
  path     => '/etc/nginx/nginx.conf',
  multiple => true,
  line     => $head,
  notify   => Exec['restart nginx'],
  require  => File['/var/www/html/index.html']
}
