#Fixing a Permissions Issue

exec { 'fix_db_charset':
  command => 'sed -i "s/define(\\\'DB_CHARSET\\\', \\'\\');/define(\\\'DB_CHARSET\\\', \\'utf8\\');/g" /var/www/html/wp-config.php',
  path    => ['/bin', '/usr/bin', '/usr/local/bin'],
  onlyif  => 'grep -q "define(\\\'DB_CHARSET\\\', \\'\\');" /var/www/html/wp-config.php',
}
