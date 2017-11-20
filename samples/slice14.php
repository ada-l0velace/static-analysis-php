<?php
$a=5;
$nis=$_POST['nis'];
while ($indarg == "") {
      $query="SELECT *FROM siswa WHERE nis='$nis'";
      while($a < 6){
      	       $indarg = "";
      }
}
$q=mysql_query($query,$koneksi);
?>
