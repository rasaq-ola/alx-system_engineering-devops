# This Puppet manifest configures Nginx with a custom HTTP header on Ubuntu

package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/conf.d/custom_header.conf':
  ensure  => file,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    add_header X-Served-By \$hostname;
  }",
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/nginx/conf.d/custom_header.conf'],
}
