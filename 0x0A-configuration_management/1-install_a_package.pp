# 1-install_a_package.pp

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install Flask==2.1.0',
  path        => ['/usr/bin', '/usr/local/bin'],
  refreshonly => true,
  require     => Package['python3-pip'],
}

exec { 'create_flask_symlink':
  command  => 'ln -sfn /usr/local/bin/flask /usr/bin/flask',
  path     => ['/usr/bin', '/usr/local/bin'],
  unless   => 'test -L /usr/bin/flask',
  require  => Exec['install_flask'],
  provider => 'shell',
}
