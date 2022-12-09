# Executing a command to kill a process name killmenow
exec { 'pkill':
  command  => 'pkill -f killmenow',
  path     =>  '/usr/bin',
  provider => shell
}