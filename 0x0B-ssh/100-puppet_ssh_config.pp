# This Puppet manifest configures the SSH client to use a specific private key and disable password authentication.

# Ensure the SSH config directory exists
file { '/home/ubuntu/.ssh':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0700',
}

# Ensure the SSH config file exists
file { '/home/ubuntu/.ssh/config':
  ensure  => 'file',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => "",
}

# Configure SSH to use the private key
file_line { 'Declare identity file':
  path  => '/home/ubuntu/.ssh/config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^IdentityFile',
}

# Configure SSH to refuse password authentication
file_line { 'Turn off passwd auth':
  path  => '/home/ubuntu/.ssh/config',
  line  => 'PasswordAuthentication no',
  match => '^PasswordAuthentication',
} 
