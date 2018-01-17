<?php

$config['bad_if_regexp'][] = '/^docker[-\w].*$/';
$config['bad_if_regexp'][] = '/^lxcbr[0-9]+$/';
$config['bad_if_regexp'][] = '/^veth.*$/';
$config['bad_if_regexp'][] = '/^virbr.*$/';
$config['bad_if_regexp'][] = '/^lo$/';
$config['bad_if_regexp'][] = '/^macvtap.*$/';
$config['bad_if_regexp'][] = '/gre.*$/';
$config['bad_if_regexp'][] = '/tun[0-9]+$/';

