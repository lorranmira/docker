<?php

$config['oxidized']['enabled']         = TRUE;
$config['oxidized']['url']             = 'http://127.0.0.1:8888';

$config['oxidized']['group_support'] = true;
$config['oxidized']['default_group'] = 'default';

### NOTE: Requires: $config['enable_syslog'] = 1;
#save config when "wr" performed on device and log sent to syslog
# $config['enable_syslog_hooks'] = 1;
# $config['os']['ios']['syslog_hook'][] = Array('regex' => '/%SYS-(SW[0-9]+-)?5-CONFIG_I/', 'script' => '/opt/librenms/scripts/syslog-notify-oxidized.php');
# $config['os']['awplus']['syslog_hook'][] = Array('regex' => '/\]wr/', 'script' => '/opt/librenms/scripts/syslog-notify-oxidized.php');

