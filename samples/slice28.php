<?php
$n = 'toze';
$a = $_POST['username'];
if ($n == 'toze'){
  $n = '';
}
if ($n == 'toze') {
  $n = $_GET['john'];
}
else {
  $n = htmlentities($n);
}

echo $n;
?>
