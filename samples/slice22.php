<?php
$a = 2;
if ($a == 4){
   $nis=$_POST['ais'];
}
elseif($a <= 1){
   $nis=$_POST['bis'];
}
elseif($a ==4){
   $nis=$_POST['cis'];
}
elseif($a < 1){
   $nis=$_POST['dis'];
}
elseif($a > 4){
   $nis=$_POST['eis'];
}
elseif($a <=(5 + $a) * ($a+6) * (10/5)){
   $nis=$_POST['fis'];
}
$q=mysql_query($nis,$koneksi);
?>
