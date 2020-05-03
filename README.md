# frontEndOfCompiler_PHP_to_C

Dependencies:<br>
1.)pyhton3<br>
2.)PLY<br>
<br>
To install PLY on your machine for python3, follow the steps outlined below:<br>
<br>
Download the source code from http://www.dabeaz.com/ply/ply-3.10.tar.gz<br>
Unzip the downloaded zip file<br>
Navigate into the unzipped ply-3.10 folder<br>
Run the following command in your terminal: python setup.py install<br>
If you completed all the above, you should now be able to use the PLY module. You can test it out by opening a python<br> interpreter and typing import ply.lex.<br>

Note: Do not use pip to install PLY, it will install a broken distribution on your machine.<br>

<br><br>

To execute the lexical analyzer run the following command:<br>
python3 php_lex.py<br>
<br>
Note:<br>
please paste the php code on which you want to perform lexical analysis in test_files/variables.php<br>
