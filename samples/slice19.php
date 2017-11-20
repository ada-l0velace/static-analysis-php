<?php
$a = 2;
if ($a == 4){
   $nis=$_POST['ais'];
}
elseif($a <= 1){
   $nis=$_POST['bis'];
}
elseif($a <=4){
	while($a <=4){
			 break;		 
			 $nis=$_POST['cis'];
   }
}
elseif($a < 1){
   $nis=$_POST['dis'];
}
elseif($a > 4){
   $nis=$_POST['eis'];
}
elseif($a <=4 + 2){
   $nis=$_POST['fis'];
}
$q=mysql_query($nis,$koneksi);
?>
