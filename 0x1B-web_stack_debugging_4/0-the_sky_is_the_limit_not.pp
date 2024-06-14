# Increase the maximum number of connections for Nginx

# Update the default Nginx configuration file to increase the ULIMIT
exec { 'increase-nginx-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin/', '/bin/'],
}

# Restart Nginx to apply the changes
exec { 'restart-nginx':
  command => 'service nginx restart',
  path    => ['/etc/init.d/'],
  require => Exec['increase-nginx-ulimit'],
}
