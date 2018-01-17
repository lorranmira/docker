**LibreNMS + mySQL + Oxidized Docker**

**Requirements**
* Hostnames need to be in lowercase due to a Ruby bug.


**First Time run**

Once LibreNMS is up and running Go to the API-settings page
http://localhost/api-access/
* create a token for API authorisation.  
* Copy the token text


Now copy this token text into the Oxidized 'config' file.
* If you have bind mounted the volume to the localhost.
browse to that directory.
* If you are not.  Then you must enter the running Oxidized
container with the following:
'sudo docker exec -it librenms_librenms_1 /bin/bash'
Then browse to '/root.config/oxidized'
* Once here open the 'config' file in an editor.  Goto the bottom of the
file and replace the text in 'X-Auth-Token:' with the Token

Oxidized is now setup to source device info from LibreNMS
