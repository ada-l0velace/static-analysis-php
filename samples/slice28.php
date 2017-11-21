<?php
$n = 'toze';
$a = $_POST['username'];
if ($n == 'toze'){
  $a = '';
}
if ($n == 'toze') {
  $a = $_GET['john'];
}
else {
  $n = htmlentities($n);
}

echo $a;
?>
