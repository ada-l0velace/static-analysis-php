<?php

$a = "abc";
if ($a == "abc"){
   $nis=$_POST['nis'];
}
elseif($a == "a" . "b"){
   $nis=$_POST['nis'];
}
$q=mysql_query($nis,$koneksi);
?>
