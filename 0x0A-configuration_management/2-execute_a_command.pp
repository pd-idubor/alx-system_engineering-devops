# Kill a process 'killmenow'
exec { 'pkill killmenow':
  command => 'pkill killmenow'
}
