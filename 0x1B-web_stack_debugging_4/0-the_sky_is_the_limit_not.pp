# Define the nginx class
class nginx {
  # Ensure the nginx package is installed and present
  package { 'nginx':
    ensure => present,
  }

  # Ensure the nginx service is running, enabled, and restarted if necessary
  service { 'nginx':
    ensure  => running,
    enable  => true,
    restart => true,
  }

  # Configure the default Nginx configuration file
  file { '/etc/nginx/sites-available/default':
    # Set the content of the file to the desired server block configuration
    content => '
      server {
        # Listen on port 80
        listen 80;
        # Set the server name to localhost
        server_name localhost;
        # Define the location block for the root URL (/)
        location / {
          # Proxy requests to http://localhost:8080
          proxy_pass http://localhost:8080;
          # Set the proxy HTTP version to 1.1
          proxy_http_version 1.1;
          # Set the Upgrade header to allow WebSocket connections
          proxy_set_header Upgrade $http_upgrade;
          # Set the Connection header to "upgrade" for WebSocket connections
          proxy_set_header Connection \'upgrade\';
          # Set the Host header to the original host
          proxy_set_header Host $host;
          # Bypass proxy caching for WebSocket connections
          proxy_cache_bypass $http_upgrade;
        }
      }
    ',
    # Notify the nginx service to restart if the configuration file changes
    notify  => Service['nginx'],
  }
}
