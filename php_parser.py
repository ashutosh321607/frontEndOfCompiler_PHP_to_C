import os
import sys
from . import php_lex
from . import phpast as ast
import ply.yacc as yacc

if sys.version_info[0] == 3:
    string_type = str
else:
    string_type = basestring

# Get the token map
tokens = phplex.tokens

precedence = (
    ('left', 'INCLUDE', 'INCLUDE_ONCE', 'EVAL', 'REQUIRE', 'REQUIRE_ONCE'),
    ('left', 'COMMA'),
    ('left', 'LOGICAL_OR'),
    ('left', 'LOGICAL_XOR'),
    ('left', 'LOGICAL_AND'),
    ('right', 'PRINT'),
    ('left', 'EQUALS', 'PLUS_EQUAL', 'MINUS_EQUAL', 'MUL_EQUAL', 'DIV_EQUAL', 'CONCAT_EQUAL', 'MOD_EQUAL', 'AND_EQUAL', 'OR_EQUAL', 'XOR_EQUAL', 'SL_EQUAL', 'SR_EQUAL'),
    ('left', 'QUESTION', 'COLON'),
    ('left', 'BOOLEAN_OR'),
    ('left', 'BOOLEAN_AND'),
    ('left', 'OR'),
    ('left', 'XOR'),
    ('left', 'AND'),
    ('nonassoc', 'IS_EQUAL', 'IS_NOT_EQUAL', 'IS_IDENTICAL', 'IS_NOT_IDENTICAL'),
    ('nonassoc', 'IS_SMALLER', 'IS_SMALLER_OR_EQUAL', 'IS_GREATER', 'IS_GREATER_OR_EQUAL'),
    ('left', 'SL', 'SR'),
    ('left', 'PLUS', 'MINUS', 'CONCAT'),
    ('left', 'MUL', 'DIV', 'MOD'),
    ('right', 'BOOLEAN_NOT'),
    ('nonassoc', 'INSTANCEOF'),
    ('right', 'NOT', 'INC', 'DEC', 'INT_CAST', 'DOUBLE_CAST', 'STRING_CAST', 'ARRAY_CAST', 'OBJECT_CAST', 'BOOL_CAST', 'UNSET_CAST', 'AT'),
    ('right', 'LBRACKET'),
    ('nonassoc', 'NEW', 'CLONE'),
    # ('left', 'ELSEIF'),
    # ('left', 'ELSE'),
    ('left', 'ENDIF'),
    ('right', 'STATIC', 'ABSTRACT', 'FINAL', 'PRIVATE', 'PROTECTED', 'PUBLIC'),
)

