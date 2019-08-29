<?php

$config['oxidized']['enabled'] = true;
$config['oxidized']['url'] = getenv('BASE_URL').':8888';
$config['oxidized']['features']['versioning'] = true;

$config['oxidized']['group_support'] = true;
$config['oxidized']['default_group'] = 'default';

$config['oxidized']['ignore_types'] = array('allied');
$config['oxidized']['ignore_os'] = array('linux');

