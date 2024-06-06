#Fixing a Permissions Issue

exec { 'strace-apache':
  command => "strace -f -e trace=network -s 1000 -p $(pidof apache2) 2>&1 | grep -i 'error'",
  path    => '/usr/bin/',
}

exec { 'fix-wordpress':
  command => "sudo find / -name 'wp-config.php' -exec sed -i 's/define(\\'DB_CHARSET\\', \\''\\');/define(\\'DB_CHARSET\\', \\'utf8\\');/g' {} +",
  path    => '/usr/bin/',
  require => Exec['strace-apache'],
}
