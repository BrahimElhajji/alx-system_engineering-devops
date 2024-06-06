#Fixing a Permissions Issue

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
  onlyif  => 'grep -q phpp /var/www/html/wp-settings.php',
  notify  => Service['apache2'],
}

service { 'apache2':
  ensure => running,
  enable => true,
}
