# Puppet manifest to install Flask version 2.1.0 using pip3

# Ensure python3-pip package is installed
package { 'python3-pip':
  ensure => installed,
}

# Execute pip3 to install Flask version 2.1.0
exec { 'install_flask':
  command     => '/usr/bin/pip3 install Flask==2.1.0 Werkzeug==2.1.1',
  path        => ['/usr/bin'],
  refreshonly => true,
  unless      => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
}
