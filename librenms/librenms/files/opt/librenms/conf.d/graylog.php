<?php

$config['graylog']['server']   = getenv('BASE_URL');
$config['graylog']['port']     = 9000;
$config['graylog']['username'] = 'admin';
$config['graylog']['password'] = 'admin';
$config['graylog']['version']  = '2.4';
$config['graylog']['timezone'] = getenv('TZ');