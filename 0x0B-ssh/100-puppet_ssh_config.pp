# File: ssh_config.pp

# Ensure the IdentityFile option is set in the SSH client configuration
file_line { 'IdentityFile option':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}

# Ensure the PasswordAuthentication option is set to 'no' in the SSH client configuration
file_line { 'Disable password login':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}
