exec { 'kill_killmenow_process':
  command     => 'pkill killmenow',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
}
