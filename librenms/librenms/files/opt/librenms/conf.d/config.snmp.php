<?php
### Default snmpv2 community <-- Matt edit
$config['snmp']['community'][] = "librenms";

## SNMPv3 Auto Details <--- Matt edit
$config['snmp']['v3'][0]['authlevel'] = 'AuthPriv';
$config['snmp']['v3'][0]['authname'] = 'librenms';
$config['snmp']['v3'][0]['authpass'] = 'librenms';
$config['snmp']['v3'][0]['authalgo'] = 'sha';
$config['snmp']['v3'][0]['cryptopass'] = 'librenms';
$config['snmp']['v3'][0]['cryptoalgo'] = 'AES';
