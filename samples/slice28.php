<?php
$n = 'toze';
$a = $_POST['username'];
if ($n == 'toze'){
  $n = '';
}
if ($n == 'toze') {
  $a = $_GET['john'];
}
else {
  $a = htmlentities($a);
}

echo $a;
?>
