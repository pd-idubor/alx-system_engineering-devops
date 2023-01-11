# Kill a process 'killmenow'
exec { 'killmenow':
  command => pkill
}
