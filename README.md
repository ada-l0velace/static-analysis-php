## Parse of php to json

### NPM INSTALL
```
sudo apt-get install nodejs
```
### INSTALL DEPENDENCIES

```bash
$ npm install
```

### RUN PHP_PARSER TO JSON

```bash
$ nodejs main.js
```

All files will be saved in the folder **samples/**

## Analyser of slices

### USAGE

```bash
$ python main.py <jsonfile>
```

### EXAMPLE

for the php slice0.php

```php
<?php
$nis=mysql_real_escape_string($_POST['nis']);
$query="SELECT *FROM siswa WHERE nis='$nis'";
$q=mysql_query($query,$koneksi);
?>
```


```zsh
$ python main.py samples/slice0.json 
No SQL injection vulnerabilities found in $q=mysql_query($query,$koneksi)
****************************** START FLOW  *****************************************
{Input $_POST['nis']}
    $nis=mysql_real_escape_string(u'$_POST'[u'nis'])
{Input $_POST['nis']}
    $query="SELECT *FROM siswa WHERE nis='"$nis"'"
{Sanitization mysql_real_escape_string}
    $nis=mysql_real_escape_string(u'$_POST'[u'nis'])
{Sink mysql_query}
    $q=mysql_query($query,$koneksi)
******************************* END FLOW  ******************************************

```
