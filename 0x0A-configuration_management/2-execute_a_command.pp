#creates a manifest that kills a process
exec { 'kill_me_now':
command => '/usr/bin/pkill killmenow',
onlyif  => '/usr/bin/pgrep killmenow',
}
