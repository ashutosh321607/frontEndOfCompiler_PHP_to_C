import ply.lex as lex
import re
from symbol_table import SymbolTable

states=(
('php','exclusive'),
('sinleQuoted','exclusive'),
('doubleQuoted','exclusive')
)

reserved=(
    'ARRAY', 'AS', 'BREAK', 'CASE', 'CLASS', 'CONST', 'CONTINUE', 'DECLARE',
    'DEFAULT', 'DIE', 'DO', 'ECHO', 'ELSE', 'ELSEIF', 'EMPTY', 'ENDDECLARE',
    'ENDFOR', 'ENDFOREACH', 'ENDIF', 'ENDSWITCH', 'ENDWHILE', 'EVAL', 'EXIT',
    'EXTENDS', 'FOR', 'FOREACH', 'FUNCTION', 'GLOBAL', 'IF', 'INCLUDE',
    'INCLUDE_ONCE', 'INSTANCEOF', 'ISSET', 'LIST', 'NEW', 'PRINT', 'REQUIRE',
    'REQUIRE_ONCE', 'RETURN', 'STATIC', 'SWITCH', 'UNSET', 'USE', 'VAR',
    'WHILE', 'FINAL', 'INTERFACE', 'IMPLEMENTS', 'PUBLIC', 'PRIVATE',
    'PROTECTED', 'ABSTRACT', 'CLONE', 'TRY', 'CATCH', 'THROW', 'NAMESPACE',
    'FINALLY', 'TRAIT', 'YIELD'
)
unparsed=(
    'WHITESPACE',
    'COMMENT'
)

tokens=reserved+unparsed+(
    
    
    'PLUS','MINUS','MUL','DIV','MOD','AND','OR','NOT','XOR','SL',
    'SR','BOOLEAN_AND','BOOLEAN_OR','BOOLEAN_NOT','LESS_THAN','GREATER_THAN','LESS_THAN_OR_EQUAL'
    ,'GRATER_THAN_OR_EQUAL','IS_EQUAL_TO','IS_NOT_EQUAL','IS_IDENTICAL',
    'IS_NOT_IDENTICAL',
    
    'EQUALS','MUL_EQUALS','DIV_EQUAL','MOD_EQUAL','PLUS_EQUAL','MINUS_EQUAL',
    'SL_EQUAL','SR_EQUAL','AND_EQUAL','OR_EQUAL','XOR_EQUAL','CONCAT_EQUAL',
    
    'INC','DEC',
    
    'LPAREN','RPAREN','LBRACKET','RBRACKET','LBRACE','RBRACE','DOLLAR',
    'COMMA','CONCAT','QUESTION','COLON','SEMI_COLON','AT','NULL_COALESCING',
    
    'INLINE_HTML',
    
    'DIR','FILE','LINE','CLASS_C','METHOD_C','NS_C','LOGICAL_AND','LOGICAL_OR','LOGICAL_XOR',
    'STRING','VARIABLE','INT_NUMBER','FLOAT_NUMBER','SINGLE_QUOTE','DOUBLE_QUOTE'
    
    
)

t_php_PLUS                = r'\+'
t_php_MINUS               = r'-'
t_php_MUL                 = r'\*'
t_php_DIV                 = r'/'
t_php_MOD                 = r'%'
t_php_AND                 = r'&'
t_php_OR                  = r'\|'
t_php_NOT                 = r'~'
t_php_XOR                 = r'\^'
t_php_SL                  = r'<<'
t_php_SR                  = r'>>'
t_php_BOOLEAN_AND         = r'&&'
t_php_BOOLEAN_OR          = r'\|\|'
t_php_BOOLEAN_NOT         = r'!'
t_php_LESS_THAN           = r'<'
t_php_GREATER_THAN        = r'>'
t_php_LESS_THAN_OR_EQUAL     = r'<='
t_php_GREATER_THAN_OR_EQUAL = r'>='
t_php_IS_EQUAL_TO            = r'=='
t_php_IS_NOT_EQUAL        = r'(!=(?!=))|(<>)'
t_php_IS_IDENTICAL        = r'==='
t_php_IS_NOT_IDENTICAL    = r'!=='


t_php_EQUALS               = r'='
t_php_MUL_EQUAL            = r'\*='
t_php_DIV_EQUAL            = r'/='
t_php_MOD_EQUAL            = r'%='
t_php_PLUS_EQUAL           = r'\+='
t_php_MINUS_EQUAL          = r'-='
t_php_SL_EQUAL             = r'<<='
t_php_SR_EQUAL             = r'>>='
t_php_AND_EQUAL            = r'&='
t_php_OR_EQUAL             = r'\|='
t_php_XOR_EQUAL            = r'\^='
t_php_CONCAT_EQUAL         = r'\.='

t_php_INC=r'\+\+'
t_php_DEC=r'--'

t_php_CONCAT=r'\.(?!\d|=)'
t_php_LPAREN               = r'\('
t_php_RPAREN               = r'\)'
t_php_DOLLAR               = r'\$'
t_php_COMMA                = r','
t_php_QUESTION             = r'\?'
t_php_COLON                = r':'
t_php_SEMI_COLON           = r';'
t_php_AT                   = r'@'
t_php_NS_SEPARATOR         = r'\\'

t_php_ARRAY_CAST           = r'\([ \t]*[Aa][Rr][Rr][Aa][Yy][ \t]*\)'
t_php_BINARY_CAST          = r'\([ \t]*[Bb][Ii][Nn][Aa][Rr][Yy][ \t]*\)'
t_php_BOOL_CAST            = r'\([ \t]*[Bb][Oo][Oo][Ll]([Ee][Aa][Nn])?[ \t]*\)'
t_php_DOUBLE_CAST          = r'\([ \t]*([Rr][Ee][Aa][Ll]|[Dd][Oo][Uu][Bb][Ll][Ee]|[Ff][Ll][Oo][Aa][Tt])[ \t]*\)'
t_php_INT_CAST             = r'\([ \t]*[Ii][Nn][Tt]([Ee][Gg][Ee][Rr])?[ \t]*\)'
t_php_OBJECT_CAST          = r'\([ \t]*[Oo][Bb][Jj][Ee][Cc][Tt][ \t]*\)'
t_php_STRING_CAST          = r'\([ \t]*[Ss][Tt][Rr][Ii][Nn][Gg][ \t]*\)'
t_php_UNSET_CAST           = r'\([ \t]*[Uu][Nn][Ss][Ee][Tt][ \t]*\)'

t_ignore_WHITESAPCE=r'\s'
t_ignore_php_COMMENT=r'/\*(.|\n)*\*/|(//|\#)([^?\n]|?(?!>))*\n?'


reserved_map={}
for r in reserved:
    reserved_map[r]=r

def t_begin_php(t):
    r'<?((\s)*|(\n)*)php((\s)+|(\n)+)'
    t.lexer.push_state('php')

def t_php_end(t):
    r'?>'
    t.lexer.pop_state('php')
    
def t_INLINE_HTML(t):
    r'([^<]|<(?![?]))+'
    t.value=(t.value,{'type':t.type})
    t.lexer.lineno+=t.value.count('\n')
    return t

def t_php_reserved_words(t):
        r'^[a-zA-Z_][a-zA-Z0-9_]*'
        t.type=reserved_map.get(t.value.upper(),None)
        if(t.type==None):
            print('Illegal Character at pos %d and lineno. %d'%(t.lexer.lexpos,t.lexer.lineno))
        else:
            t.value=(t.value,{'type':t.type})
            return t

def t_php_INT_NUMBER(t):
    r'\d+([eE][*-]?\d+)?'
    if(t.lexer.symbol_table.insert(t.value)!=None):
        t.lexer.symbol_table.set_attribute(t.value,'type',t.type)
    t.value=(t.value,t.lexer.symbol_table.lookup(t.value))
    return t

def t_php_FLOAT_NUMBER(t):
    r'\d*\.\d+([eE][*-]?\d+)?'
    
    if(t.lexer.symbol_table.insert(t.value)!=None):
        t.lexer.symbol_table.set_attribute(t.value,'type',t.type)
    t.value=(t.value,t.lexer.symbol_table.lookup(t.value))
    
    return t

def t_php_varaiable(t):
    r'\$^[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*$'
    
    if(t.lexer.symbol_table.insert(t.value)!=None):
        t.lexer.symbol_table.set_attribute(t.value,'type',t.type)
    t.value=(t.value,t.lexer.symbol_table.lookup(t.value))
        
    return t

def t_php_SINGLE_QUOTE(t):
    r'\''
    t.lexer.push_state('singleQuoted')
    t.value=(t.value,{'type':t.type})
    return t

def t_singleQuoted_STRING(t):
    r"[^']*|((?<=\)')*"
    if(t.lexer.symbol_table.insert(t.value)!=None):
        t.lexer.symbol_table.set_attribute(t.value,'type',t.type)
    t.value=(t.value,t.lexer.symbol_table.lookup(t.value))
    return t

def t_singleQuote_SINGLE_QUOTE(t):
    r"(?<!\)'"
    t.lexer.pop_state()
    t.value=(t.value,{'type':t.type})
    return t

def t_php_DOUBLE_QUOTE(t):
    r'"'
    t.lexer.push_state('doubleQuoted')
    t.value=(t.value,{'type':t.type})

    return t

def t_doubleQuoted_STRING(t):
    r'[^$"]*|((?<=\)")*|((?<=\)$)*'

    if(t.lexer.symbol_table.insert(t.value)!=None):
        t.lexer.symbol_table.set_attribute(t.value,'type',t.type)
    t.value=(t.value,t.lexer.symbol_table.lookup(t.value))
    
    return t

def t_doubleQuoted_VARIABLE(t):
    r'\$^[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*$'
    
    if(t.lexer.symbol_table.insert(t.value)!=None):
        t.lexer.symbol_table.set_attribute(t.value,'type',t.type)
    t.value=(t.value,t.lexer.symbol_table.lookup(t.value))
    
    return t

def t_doubleQuoted_DOUBLE_QUOTE(t):
    r'(?<!\)"'
    t.value=(t.value,{'type':t.type})
    return t

def t_ANY_newline(t):
    r'\n+'
    t.lexer.lineno+=len(t.value)
    
def t_php_error(t):
    print('Illegal character at line no. %d and position no. %d'% (t.lexer.lineno,t.lexer.lexpos))
    t.lexer.skip(1)
    
    
lexer=lex.lex()
lexer.symbol_table=SymbolTable()

