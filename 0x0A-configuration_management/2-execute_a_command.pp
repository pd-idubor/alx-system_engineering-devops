# Executes a command
exec { 'pkill killmenow':
  command => "/usr/bin/pkill 'killmenow'",
}
