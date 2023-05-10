# Wordpress site debugging

exec { 'wordpress-fix':
  command => "/bin/sed -i /var/www/html/wp-settings.php \
  -e 's/class-wp-locale.phpp/class-wp-locale.php/'"
  }
