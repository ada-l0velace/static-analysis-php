<?php

$a=$_POST['username'];
print($a);
printf("%s",$a);
echo $_POST['username'];
file_put_contents("File.txt", $a);
file_get_contents("File.txt");
file_get_contents('http://www.google.com/');
if ($a == "a") {
   exit($a);
}
die($a);
?>
