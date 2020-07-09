import os
import sys
import php_lex
import ply.yacc as yacc

# Get the token map
tokens = php_lex.tokens

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

def p_start(p):
    'start : top_statement_list'

def p_top_statement_list(p):
    '''top_statement_list : top_statement_list top_statement
                          | empty'''

def p_top_statement(p):
    '''top_statement : statement
                     | function_declaration_statement
                     | HALT_COMPILER LPAREN RPAREN SEMI_COLON
                     | CONST constant_declarations SEMI_COLON'''
                     
def p_constant_declartions(p):
    ''' constant_declarations : constant_declarations COMMA constant_declaration
                             | constant_declaration'''
def p_constant_declaration(p):
    '''constant_declaration : IDENTIFIER EQUALS static_expr'''

def p_inner_statment_list(p):
    ''' inner_statement_list : inner_statement_list inner_statement
                            | empty'''
                            
def p_inner_statment(p):
    ''' inner_statement : statement
                       | function_declaration_statement'''

def p_inner_statement_yield(p):
    ''' inner_statement : YIELD SEMI_COLON
                       | YIELD expr SEMI_COLON'''

def p_statement_block(p):
    '''statement : LBRACE inner_statement_list RBRACE '''
    
def p_statement_if(p):
    '''statement : IF LPAREN expr RPAREN statement elseif_list else_single
                 | IF LPAREN expr RPAREN COLON inner_statement_list new_elseif_list new_else_single ENDIF SEMI_COLON '''

def p_statement_while(p):
    ''' statement : WHILE LPAREN expr RPAREN while_statement'''
    
def p_statement_do_while(p):
    '''statement : DO statement WHILE LPAREN expr RPAREN SEMI_COLON'''
    
def p_statement_for(p):
    ''' statement : FOR LPAREN for_expr SEMI_COLON for_expr SEMI_COLON for_expr RPAREN for_statement'''
    
def p_statement_switch(p):
    '''statement : SWITCH LPAREN expr RPAREN switch_case_list '''
    
def p_statement_break(p):
    '''statement : BREAK SEMI_COLON
                 | BREAK expr SEMI_COLON '''
                 
def p_statement_continue(p):
    '''statement : CONTINUE SEMI_COLON
                 | CONTINUE expr SEMI_COLON '''
                 
def p_statement_return(p):
    '''statement : RETURN SEMI_COLON
                 | RETURN expr SEMI_COLON '''

def p_statement_global(p):
    ''' statement : GLOBAL global_var_list SEMI_COLON'''

def p_statement_static(p):
    ''' statement : STATIC static_var_list SEMI_COLON'''
    
def p_statement_echo(p):
    '''statement : ECHO echo_expr_list SEMI_COLON '''
def p_statement_inline_html(p):
    ''' statement : ECHO echo_expr_list SEMI_COLON'''
def p_statement_expr(p):
    ''' statement : expr SEMI_COLON'''
    
def p_statement_unset(p):
    '''statement : UNSET LPAREN unset_variables RPAREN SEMI_COLON '''
    
def p_statement_empty_stmt(p):
    '''statement : SEMI_COLON '''
    
def p_elif_list(p):
    '''elseif_list : empty
                   | elseif_list ELSEIF LPAREN expr RPAREN statement'''

def p_else_single(p):
    '''else_single : empty
                   | ELSE statement '''

def p_new_elseif_list(p):
    ''' new_elseif_list : empty
                       | new_elseif_list ELSEIF LPAREN expr RPAREN COLON inner_statement_list'''
                       
def p_new_else_single(p):
    '''new_else_single : empty
                       | ELSE COLON inner_statement_list '''

def p_while_statement(p):
    '''while_statement : statement
                       | COLON inner_statement_list ENDWHILE SEMI_COLON '''
                       
def p_for_expr(p):
    '''for_expr : empty
                | non_empty_for_expr '''
                
def p_nonempty_for_expr(p):
    '''non_empty_for_expr : non_empty_for_expr COMMA expr
                          | expr '''
def p_for_statement(p):
    '''for_statement : statement
                     | COLON inner_statement_list ENDFOR SEMI_COLON '''

def p_switch_case_list(p):
    '''switch_case_list : LBRACE case_list RBRACE
                        | LBRACE SEMI_COLON case_list RBRACE '''

def p_switch_case_list_colon(p):
    '''switch_case_list : COLON case_list ENDSWITCH SEMI_COLON
                        | COLON SEMI_COLON case_list ENDSWITCH SEMI_COLON '''
    
def p_case_list(p):
    '''case_list : empty
                 | case_list CASE expr case_separator inner_statement_list
                 | case_list DEFAULT case_separator inner_statement_list '''
def p_case_separator(p):
    '''case_separator : COLON
                      | SEMI_COLON '''
def p_global_var_list(p):
    '''global_var_list : global_var_list COMMA global_var
                       | global_var '''                      
                       
def p_global_var(p):
    '''global_var : VARIABLE
                  | DOLLAR variable
                  | DOLLAR LBRACE expr RBRACE '''
                  
def p_static_var_list(p):
    '''static_var_list : static_var_list COMMA static_var
                       | static_var '''       
                       
def p_static_var(p):
    '''static_var : VARIABLE EQUALS static_scalar
                  | VARIABLE ''' 
                  
def p_echo_expr_list(p):
    '''echo_expr_list : echo_expr_list COMMA expr
                      | expr '''
                      
def p_unset_variables(p):
    '''unset_variables : unset_variables COMMA unset_variable
                       | unset_variable '''
                       
def p_unset_variable(p):
    '''unset_variable : variable '''
    
def p_function_declaration_statment(p):
    '''function_declaration_statement : FUNCTION is_reference IDENTIFIER LPAREN parameter_list RPAREN LBRACE inner_statement_list RBRACE '''
    
def p_is_reference(p):
    '''is_reference : AND
                    | empty '''

def p_parameter_list(p):
    '''parameter_list : non_empty_parameter_list 
                      | empty '''
                      
def p_non_empty_parameter_list(p):
    '''non_empty_parameter_list: non_empty_parameter_list COMMA parameter 
                                | parameter'''
                                
def p_parameter(p):
    '''parameter : VARIABLE
                 | AND VARIABLE
                 | VARIABLE EQUALS static_scalar
                 | AND VARIABLE EQUALS static_scalar '''

def p_expr_variable(p):
    'expr : variable'

def p_expr_assign(p):
    '''expr : variable EQUALS expr
            | variable EQUALS AND expr '''
            
def p_ctor_arguments(p):
    ''' ctor_arguments : LPAREN function_call_parameter_list RPAREN
                      | empty'''
