#Fixing a Permissions Issue

if !('puppetlabs/stdlib' in $::installed_modules) {
  package { 'puppetlabs-stdlib':
    ensure => present,
    provider => 'puppet_gem',
  }
}

file_line { 'fix-wordpress':
  path  => '/var/www/html/wp-settings.php',
  match => 'phpp',
  line  => 'php',
  notify => Service['apache2'],
}

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File_line['fix-wordpress'],
}
