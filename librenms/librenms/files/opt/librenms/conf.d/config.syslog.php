<?php

### NOTE: Requires: $config['enable_syslog'] = 1;
#save config when "wr" performed on device and log sent to syslog
$config['enable_syslog_hooks'] = 1;
$config['os']['ios']['syslog_hook'][] = Array('regex' => '/%SYS-(SW[0-9]+-)?5-CONFIG_I/', 'script' => '/opt/librenms/scripts/syslog-notify-oxidized.php');
$config['os']['awplus']['syslog_hook'][] = Array('regex' => '/Startup-config saved on/', 'script' => '/opt/librenms/scripts/syslog-notify-oxidized.php');