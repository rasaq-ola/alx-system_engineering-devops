# This Puppet manifest configures the SSH client to use a specific private key and disable password authentication

# Ensure the SSH client configuration file exists
file { '/etc/ssh/ssh_config':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

# Ensure the IdentityFile setting is present
file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => '    IdentityFile ~/.ssh/school',
  match => '^\s*IdentityFile\s+',
  after => '^Host\s+\*\s*$',
  require => File['/etc/ssh/ssh_config'],
}

# Ensure PasswordAuthentication is disabled
file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  line  => '    PasswordAuthentication no',
  match => '^\s*PasswordAuthentication\s+',
  after => '^Host\s+\*\s*$',
  require => File['/etc/ssh/ssh_config'],
}

# Ensure the Host * entry is present at the beginning
file_line { 'Host entry':
  path  => '/etc/ssh/ssh_config',
  line  => 'Host *',
  match => '^Host\s+\*\s*$',
  before => File_line['Declare identity file'],
  require => File['/etc/ssh/ssh_config'],
}
