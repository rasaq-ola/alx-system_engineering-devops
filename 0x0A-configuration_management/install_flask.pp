# Puppet manifest to install Flask version 2.1.0 on Ubuntu 20.04 LTS

# Ensure python3-pip package is installed
package { 'python3-pip':
  ensure => installed,
}

# Execute pip3 to install Flask version 2.1.0
exec { 'install_flask':
  command     => '/usr/bin/pip3 install Flask==2.1.0',
  path        => ['/usr/bin'],
  refreshonly => true,
  unless      => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
}

# Ensure Flask package is installed and its version is 2.1.0
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Exec['install_flask'],
}
