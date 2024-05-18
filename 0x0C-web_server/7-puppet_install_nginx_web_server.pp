# 7-puppet_install_nginx_web_server.pp
# This Puppet manifest installs nginx and configures a custom page, a 301 redirect, and a custom 404 page

# Ensure the package 'nginx' is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the nginx service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  require   => Package['nginx'],
}

# Define the content of the custom root page
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Create a custom 404 error page
file { '/var/www/html/custom_404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
  require => Package['nginx'],
}

# Define the nginx server configuration with redirection using inline template
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => @("EOF")
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    root /var/www/html;
    index index.html;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /custom_404.html;
    location = /custom_404.html {
        internal;
    }
}
| EOF
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure the nginx configuration is valid
exec { 'validate_nginx_config':
  command     => '/usr/sbin/nginx -t',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
  notify      => Service['nginx'],
}
