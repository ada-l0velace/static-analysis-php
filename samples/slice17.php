<?php

$a = "abc";
if ($a == "abc"){
   $nis=$_POST['nis'];
}
elseif($a == "a" . "bc"){
   $nis=$_POST['nis'];
}
$q=mysql_query($query,$koneksi);
?>
