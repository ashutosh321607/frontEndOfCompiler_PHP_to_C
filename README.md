# frontEndOfCompiler_PHP_to_C

Dependencies:
1.)pyhton3
2.)PLY

To install PLY on your machine for python3, follow the steps outlined below:

Download the source code from http://www.dabeaz.com/ply/ply-3.10.tar.gz
Unzip the downloaded zip file
Navigate into the unzipped ply-3.10 folder
Run the following command in your terminal: python setup.py install
If you completed all the above, you should now be able to use the PLY module. You can test it out by opening a python interpreter and typing import ply.lex.

Note: Do not use pip to install PLY, it will install a broken distribution on your machine.



To execute the lexical analyzer run the following command:
python3 php_lex.py

Note:
please paste the php code on which you want to perform lexical analysis in test_files/variables.php
