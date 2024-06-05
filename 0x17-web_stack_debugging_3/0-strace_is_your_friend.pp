#Fixing a Permissions Issue

file { '/var/www/html/wp-settings.php':
  ensure  => file,
  content => template('wp-settings.php.erb'),
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/var/www/html/wp-settings.php'],
}
