import ply.lex as lex
import re
from symbol_table import SymbolTable

def col_no(pos,val):
    last_new_line_pos=string.rfind("\n",0,pos)
    final_pos=pos-len(val)-last_new_line_pos
    return final_pos

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
    'IS_NOT_IDENTICAL','SPACESHIP','HERE_NOW_DOC',
    
    'EQUALS','MUL_EQUALS','DIV_EQUAL','MOD_EQUAL','PLUS_EQUAL','MINUS_EQUAL',
    'SL_EQUAL','SR_EQUAL','AND_EQUAL','OR_EQUAL','XOR_EQUAL','CONCAT_EQUAL',
    
    'INC','DEC',
    
    'LPAREN','RPAREN','LBRACKET','RBRACKET','LBRACE','RBRACE','DOLLAR',
    'COMMA','CONCAT','QUESTION','COLON','SEMI_COLON','AT','NULL_COALESCING',
    
    'INLINE_HTML',
    
    'DIR','FILE','LINE','CLASS_C','METHOD_C','NS_C','LOGICAL_AND','LOGICAL_OR','LOGICAL_XOR',
    'STRING','VARIABLE','INT_NUMBER','FLOAT_NUMBER','SINGLE_QUOTE','DOUBLE_QUOTE','IDENTIFIER','FUNCTION_NAME',
    'UNQUOTED_STRING',
    
    
    
)

reserved_map={}
for r in reserved:
    reserved_map[r]=r


def t_ANY_newline(t):
    r'\n+'
    t.lexer.lineno+=len(t.value)
    
def t_begin_php(t):
    r'<[?%](([Pp][Hh][Pp][ \t\r\n]?)|=)?' 
    t.lexer.lineno+=t.value.count("\n")
    t.lexer.push_state('php')


def t_php_end(t):
    r'[?%]>\r?\n?'
    t.lexer.lineno+=t.value.count("\n")
    t.lexer.pop_state()


def t_php_reserved_words(t):
        r'[a-zA-Z_][\w\d_]*'
        t.type=reserved_map.get((t.value).upper(),"IDENTIFIER")
        if(t.type=="IDENTIFIER"):
            if(t.lexer.symbol_table.insert(t.value)!=None):
                t.lexer.symbol_table.set_attribute(t.value,'type',t.type)
                t.lexer.symbol_table.set_attribute(t.value,'line_no',t.lexer.lineno)
                t.lexer.symbol_table.set_attribute(t.value,'col',col_no(t.lexer.lexpos,t.value))
            t.value=(t.value,t.lexer.symbol_table.lookup(t.value))
        else:
            t.value=(t.value,{'type':t.type})
        return t

def t_php_VARIABLE(t):
    r'\$[A-Za-z_][\w_]*'
    
    if(t.lexer.symbol_table.insert(t.value)!=None):
        t.lexer.symbol_table.set_attribute(t.value,'type',t.type)
        t.lexer.symbol_table.set_attribute(t.value,'line_no',t.lexer.lineno)
        t.lexer.symbol_table.set_attribute(t.value,'col',col_no(t.lexer.lexpos,t.value))
    t.value=(t.value,t.lexer.symbol_table.lookup(t.value))
        
    return t

def t_php_UNQUOTED_STRING(t):
    r'^[^\s]+[^$\"\'\n]+|((?<=\\)\")+|((?<=\\)\')+|((?<=\\)$)+'
    if(t.lexer.symbol_table.insert(t.value)!=None):
        t.lexer.symbol_table.set_attribute(t.value,'type',t.type)
        t.lexer.symbol_table.set_attribute(t.value,'line_no',t.lexer.lineno)
        t.lexer.symbol_table.set_attribute(t.value,'col',col_no(t.lexer.lexpos,t.value))
    t.value=(t.value,t.lexer.symbol_table.lookup(t.value))
    return t

t_php_ignore_WHITESAPCE=r'\s'
t_php_ignore_COMMENT=r"(?:\#|//)[^\r\n]*|/\*[\s\S]*?\*/"

def t_php_SPACESHIP(t):
    r'<=>'
    t.value=(t.value,{'type':t.type})
    return t

def t_php_HERE_NOW_DOC(t):
    r'<<<'
    t.value=(t.value,{'type',t.type})
    return t

def t_php_INC(t):
	r'\+\+'
	t.value=(t.value,{'type':t.type})
	return t

def t_php_DEC(t):
	r'--'
	t.value=(t.value,{'type':t.type})
	return t

# t_php_BOOLEAN_AND         = r'&&'
def t_php_BOOLEAN_AND(t):
    r'&&'
    t.value=(t.value,{'type':t.type})
    return t

# t_php_BOOLEAN_OR          = r'\|\|'
def t_php_BOOLEAN_OR(t):
    r'\|\|'
    t.value=(t.value,{'type':t.type})
    return t

# t_php_BOOLEAN_NOT         = r'!'
def t_php_BOOLEAN_NOT(t):
    r'!'
    t.value=(t.value,{'type':t.type})
    return t

# t_php_LESS_THAN_OR_EQUAL     = r'<='
def t_php_LESS_THAN_OR_EQUAL(t):
    r'<='
    t.value=(t.value,{'type':t.type})
    return t

# t_php_GREATER_THAN_OR_EQUAL = r'>='
def t_php_GREATER_THAN_OR_EQUAL(t):
    r'>='
    t.value=(t.value,{'type':t.type})
    return t

# t_php_LESS_THAN           = r'<'
def t_php_LESS_THAN(t):
    r'<'
    t.value=(t.value,{'type':t.type})
    return t

# t_php_GREATER_THAN        = r'>'
def t_php_GREATER_THAN(t):
    r'>'
    t.value=(t.value,{'type':t.type})
    return t

# t_php_IS_EQUAL_TO            = r'=='
def t_php_IS_EQUAL_TO(t):
    r'=='
    t.value=(t.value,{'type':t.type})
    return t

# t_php_IS_NOT_EQUAL        = r'(!=(?!=))|(<>)'
def t_php_IS_NOT_EQUAL(t):
    r'(!=(?!=))|(<>)'
    t.value=(t.value,{'type':t.type})
    return t

# t_php_IS_IDENTICAL        = r'==='
def t_php_IS_IDENTICAL(t):
    r'==='
    t.value=(t.value,{'type':t.type})
    return t

# t_php_IS_NOT_IDENTICAL    = r'!=='
def t_php_IS_NOT_IDENTICAL(t):
    r'!=='
    t.value=(t.value,{'type':t.type})
    return t


def t_php_EQUALS(t):
	r'='
	t.value=(t.value,{'type':t.type})
	return t

def t_php_MUL_EQUAL(t):
	r'\*='
	t.value=(t.value,{'type':t.type})
	return t

def t_php_DIV_EQUAL(t):
	r'/='
	t.value=(t.value,{'type':t.type})
	return t

def t_php_MOD_EQUAL(t):
	r'%='
	t.value=(t.value,{'type':t.type})
	return t

def t_php_PLUS_EQUAL(t):
	r'\+='
	t.value=(t.value,{'type':t.type})
	return t

def t_php_MINUS_EQUAL(t):
	r'-='
	t.value=(t.value,{'type':t.type})
	return t

def t_php_SL_EQUAL(t):
	r'<<='
	t.value=(t.value,{'type':t.type})
	return t

def t_php_SR_EQUAL(t):
	r'>>='
	t.value=(t.value,{'type':t.type})
	return t

def t_php_AND_EQUAL(t):
	r'&='
	t.value=(t.value,{'type':t.type})
	return t

def t_php_OR_EQUAL(t):
	r'\|='
	t.value=(t.value,{'type':t.type})
	return t

def t_php_XOR_EQUAL(t):
	r'\^='
	t.value=(t.value,{'type':t.type})
	return t

def t_php_CONCAT_EQUAL(t):
	r'\.='
	t.value=(t.value,{'type':t.type})
	return t


def t_HERE_NOW_DOC(t):
    r'<<<'
    t.value=(t.value,{'type':type})
    return t

# t_php_PLUS                = r'\+'
def t_php_PLUS(t):
    r'\+'
    t.value=(t.value,{'type':t.type})
    return t

# t_php_MINUS               = r'-'
def t_php_MINUS (t):
    r'-'
    t.value=(t.value,{'type':t.type})
    return t

# t_php_MUL                 = r'\*'
def t_php_MU(t):
    r'\*'
    t.value=(t.value,{'type':t.type})
    return t

# t_php_DIV                 = r'/'
def t_php_DIV(t):
    r'/'
    t.value=(t.value,{'type':t.type})
    return t

# t_php_MOD                 = r'%'
def t_php_MOD(t):
    r'%'
    t.value=(t.value,{'type':t.type})
    return t

# t_php_AND                 = r'&'
def t_php_AND(t):
    r'&'
    t.value=(t.value,{'type':t.type})
    return t

# t_php_OR                  = r'\|'
def t_php_OR(t):
    r'\|'
    t.value=(t.value,{'type':t.type})
    return t

# t_php_NOT                 = r'~'
def t_php_NOT(t):
    r'~'
    t.value=(t.value,{'type':t.type})
    return t

# t_php_XOR                 = r'\^'
def t_php_XOR(t):
    r'\^'
    t.value=(t.value,{'type':t.type})
    return t

# t_php_SL                  = r'<<'
def t_php_SL(t):
    r'<<'
    t.value=(t.value,{'type':t.type})
    return t

# t_php_SR                  = r'>>'
def t_php_SR(t):
    r'>>'
    t.value=(t.value,{'type':t.type})
    return t

def t_php_CONCAT(t):
	r'\.(?!\d|=)'
	t.value=(t.value,{'type':t.type})
	return t

def t_php_LPAREN(t):
	r'\('
	t.value=(t.value,{'type':t.type})
	return t

def t_php_RPAREN(t):
	r'\)'
	t.value=(t.value,{'type':t.type})
	return t

def t_php_DOLLAR(t):
	r'\$'
	t.value=(t.value,{'type':t.type})
	return t

def t_php_COMMA(t):
	r','
	t.value=(t.value,{'type':t.type})
	return t

def t_php_QUESTION(t):
	r'\?'
	t.value=(t.value,{'type':t.type})
	return t

def t_php_COLON(t):
	r':'
	t.value=(t.value,{'type':t.type})
	return t

def t_php_SEMI_COLON(t):
	r';'
	t.value=(t.value,{'type':t.type})
	return t

def t_php_AT(t):
	r'@'
	t.value=(t.value,{'type':t.type})
	return t

def t_php_NS_SEPARATOR(t):
	r'\\'
	t.value=(t.value,{'type':t.type})
	return t


def t_php_ARRAY_CAST(t):
	r'\([\t]*[Aa][Rr][Rr][Aa][Yy][\t]*\)'
	t.value=(t.value,{'type':t.type})
	return t

def t_php_BINARY_CAST(t):
	r'\([\t]*[Bb][Ii][Nn][Aa][Rr][Yy][\t]*\)'
	t.value=(t.value,{'type':t.type})
	return t

def t_php_BOOL_CAST(t):
	r'\([\t]*[Bb][Oo][Oo][Ll]([Ee][Aa][Nn])?[\t]*\)'
	t.value=(t.value,{'type':t.type})
	return t

def t_php_DOUBLE_CAST(t):
	r'\([\t]*([Rr][Ee][Aa][Ll]|[Dd][Oo][Uu][Bb][Ll][Ee]|[Ff][Ll][Oo][Aa][Tt])[\t]*\)'
	t.value=(t.value,{'type':t.type})
	return t

def t_php_INT_CAST(t):
	r'\([\t]*[Ii][Nn][Tt]([Ee][Gg][Ee][Rr])?[\t]*\)'
	t.value=(t.value,{'type':t.type})
	return t

def t_php_OBJECT_CAST(t):
	r'\([\t]*[Oo][Bb][Jj][Ee][Cc][Tt][\t]*\)'
	t.value=(t.value,{'type':t.type})
	return t

def t_php_STRING_CAST(t):
	r'\([\t]*[Ss][Tt][Rr][Ii][Nn][Gg][\t]*\)'
	t.value=(t.value,{'type':t.type})
	return t

def t_php_UNSET_CAST(t):
	r'\([\t]*[Uu][Nn][Ss][Ee][Tt][\t]*\)'
	t.value=(t.value,{'type':t.type})
	return t


def t_php_LBRACE(t):
	r'\{'
	t.value=(t.value,{'type':t.type})
	return t

def t_php_RBRACE(t):
	r'\}'
	t.value=(t.value,{'type':t.type})
	return t

def t_php_LBRACKET(t):
	r'\['
	t.value=(t.value,{'type':t.type})
	return t

def t_php_RBRACKET(t):
	r'\]'
	t.value=(t.value,{'type':t.type})
	return t

def t_INLINE_HTML(t):
    r'([^<]|<(?![?]))+'
    t.value=(t.value,{'type':t.type})
    t.lexer.lineno+=t.value.count('\n')
    return t

def t_php_FLOAT_NUMBER(t):
    r'\d*\.\d+([eE][*-]?\d+)?'
    
    if(t.lexer.symbol_table.insert(t.value)!=None):
        t.lexer.symbol_table.set_attribute(t.value,'type',t.type)
        t.lexer.symbol_table.set_attribute(t.value,'line_no',t.lexer.lineno)
        t.lexer.symbol_table.set_attribute(t.value,'col',col_no(t.lexer.lexpos,t.value))
    t.value=(t.value,t.lexer.symbol_table.lookup(t.value))
    
    return t

def t_php_INT_NUMBER(t):
    r'\d+([eE][*-]?\d+)?'
    if(t.lexer.symbol_table.insert(t.value)!=None):
        t.lexer.symbol_table.set_attribute(t.value,'type',t.type)
        t.lexer.symbol_table.set_attribute(t.value,'line_no',t.lexer.lineno)
        t.lexer.symbol_table.set_attribute(t.value,'col',col_no(t.lexer.lexpos,t.value))
    t.value=(t.value,t.lexer.symbol_table.lookup(t.value))
    return t





def t_php_SINGLE_QUOTE(t):
    r'\''
    t.lexer.push_state('singleQuoted')
    t.value=(t.value,{'type':t.type})
    return t

def t_singleQuoted_STRING(t):
    r"[^']+|((?<=\\)')+"
    if(t.lexer.symbol_table.insert(t.value)!=None):
        t.lexer.symbol_table.set_attribute(t.value,'type',t.type)
        t.lexer.symbol_table.set_attribute(t.value,'line_no',t.lexer.lineno)
        t.lexer.symbol_table.set_attribute(t.value,'col',col_no(t.lexer.lexpos,t.value))
    t.value=(t.value,t.lexer.symbol_table.lookup(t.value))
    return t

def t_singleQuoted_SINGLE_QUOTE(t):
    r"(?<!\\)'"
    t.lexer.pop_state()
    t.value=(t.value,{'type':t.type})
    return t

def t_php_DOUBLE_QUOTE(t):
    r'"'
    t.lexer.push_state('doubleQuoted')
    t.value=(t.value,{'type':t.type})

    return t

def t_doubleQuoted_STRING(t):
    r'[^$"]+|((?<=\\)")+|((?<=\\)$)+'

    if(t.lexer.symbol_table.insert(t.value)!=None):
        t.lexer.symbol_table.set_attribute(t.value,'type',t.type)
        t.lexer.symbol_table.set_attribute(t.value,'line_no',t.lexer.lineno)
        t.lexer.symbol_table.set_attribute(t.value,'col',col_no(t.lexer.lexpos,t.value))
    t.value=(t.value,t.lexer.symbol_table.lookup(t.value))
    
    return t

def t_doubleQuoted_VARIABLE(t):
    r'\$[A-Za-z_][\w_]*'
    
    if(t.lexer.symbol_table.insert(t.value)!=None):
        t.lexer.symbol_table.set_attribute(t.value,'type',t.type)
        t.lexer.symbol_table.set_attribute(t.value,'line_no',t.lexer.lineno)
        t.lexer.symbol_table.set_attribute(t.value,'col',col_no(t.lexer.lexpos,t.value))
    t.value=(t.value,t.lexer.symbol_table.lookup(t.value))
    
    return t

def t_doubleQuoted_DOUBLE_QUOTE(t):
    r'(?<!\\)"'
    t.lexer.pop_state()
    t.value=(t.value,{'type':t.type})
    return t


    
def t_ANY_error(t):
    print('Illegal character at line no. %d and position no. %d, character:%s'% (t.lexer.lineno,col_no(t.lexer.lexpos,t.value),t.value))
    t.lexer.skip(1)
    
    




lexer=lex.lex()
lexer.symbol_table=SymbolTable()

with open('./test_files/variables.php') as f:
    string=""
    lines=f.readlines()
    string="".join(lines)

lexer.input(string)
while(True):
    tok=lexer.token()
    if(tok!=None):
        print(tok.value)
        print("")
    else:
        break