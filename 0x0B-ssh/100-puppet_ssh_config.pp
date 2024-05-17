# This Puppet manifest ensures the SSH client configuration uses the private key ~/.ssh/school and disables password authentication

# Ensure the SSH configuration file exists
file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
}

# Ensure the IdentityFile setting is present
file_line { 'Declare identity file':
  path  => '/home/ubuntu/.ssh/config',
  line  => '    IdentityFile ~/.ssh/school',
  match => '^\s*IdentityFile\s+',
  after => '^Host\s+\*\s*$',
  require => File['/home/ubuntu/.ssh/config'],
}

# Ensure PasswordAuthentication is disabled
file_line { 'Turn off passwd auth':
  path  => '/home/ubuntu/.ssh/config',
  line  => '    PasswordAuthentication no',
  match => '^\s*PasswordAuthentication\s+',
  after => '^Host\s+\*\s*$',
  require => File['/home/ubuntu/.ssh/config'],
}

# Ensure the Host * entry is present at the beginning
file_line { 'Host entry':
  path  => '/home/ubuntu/.ssh/config',
  line  => 'Host *',
  match => '^Host\s+\*\s*$',
  before => File_line['Declare identity file'],
  require => File['/home/ubuntu/.ssh/config'],
}
