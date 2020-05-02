Thanks for Sharing your homework
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
