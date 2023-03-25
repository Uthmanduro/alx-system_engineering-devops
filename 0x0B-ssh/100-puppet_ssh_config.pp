#using puppet to make changes to my configuration file
file { '/etc/ssh/ssh_config':
ensure  => file,
content => 'Host 54.237.35.136\n    IdentityFile ~/.ssh/school\n    PasswordAuthentication no',
replace => false,
}
