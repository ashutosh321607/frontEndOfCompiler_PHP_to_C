<?php
$txt = "Hello world!";
$x = 5;
$y = 10.5;

echo $txt;
echo "<br>";
echo $x;
echo "<br>";
echo $y;

$x=$y+$x;
echo $x;

for($x=1;$x<=3;$x++)
{
    echo $x;
    if($x==1)
        echo "this is equal to 1";
}

function helloWorld()
{
    echo "hello world!";
}

?>