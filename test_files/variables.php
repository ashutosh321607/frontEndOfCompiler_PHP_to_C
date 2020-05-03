<?php 

$x=0;
$y=5;
$z=$x+$y;

$a=<<<EOT
asdfg@@@asd ${x} {$y} ghjkghjkbhj hjkyhujyu
EOT;

$x=$y[$z+$y];

echo <<<'EOT'
My name is "$name". I am printing some $foo->foo.
Now, I am printing some {$foo->bar[1]}.
This should not print a capital 'A': \x41
EOT;

?>