<?php

$config['oxidized']['enabled']         = true;
$config['oxidized']['url']             = 'http://oxidized:8888';
$config['oxidized']['features']['versioning'] = true;

$config['oxidized']['group_support'] = true;
$config['oxidized']['default_group'] = 'default';

$config['oxidized']['ignore_types'] = array('allied');
$config['oxidized']['ignore_os'] = array('linux');

### NOTE: Requires: $config['enable_syslog'] = 1;
#save config when "wr" performed on device and log sent to syslog
# $config['enable_syslog_hooks'] = 1;
# $config['os']['ios']['syslog_hook'][] = Array('regex' => '/%SYS-(SW[0-9]+-)?5-CONFIG_I/', 'script' => '/opt/librenms/scripts/syslog-notify-oxidized.php');
# $config['os']['awplus']['syslog_hook'][] = Array('regex' => '/\]wr/', 'script' => '/opt/librenms/scripts/syslog-notify-oxidized.php');
