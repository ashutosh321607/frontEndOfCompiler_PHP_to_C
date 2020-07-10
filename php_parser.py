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



# *************

def p_expr_clone(p):
    'expr : CLONE expr'

def p_expr_list_assign(p):
    'expr : LIST LPAREN assignment_list RPAREN EQUALS expr'

def p_assignment_list(p):
    '''assignment_list : assignment_list COMMA assignment_list_element
                       | assignment_list_element'''

def p_assignment_list_element(p):
    '''assignment_list_element : variable
                               | empty
                               | LIST LPAREN assignment_list RPAREN'''

def p_variable(p):
    'variable :  base_variable_with_function_calls'

def p_base_variable_with_function_calls(p):
    '''base_variable_with_function_calls : base_variable
                                         | function_call'''

def p_function_call(p):
    'function_call : namespace_name LPAREN function_call_parameter_list RPAREN'

def p_function_call_variable(p):
    'function_call : variable_without_objects LPAREN function_call_parameter_list RPAREN'

def p_function_call_backtick_shell_exec(p):
    'function_call : BACKTICK encaps_list BACKTICK'

def p_method_or_not(p):
    '''method_or_not : LPAREN function_call_parameter_list RPAREN
                     | empty'''

def p_variable_properties(p):
    '''variable_properties : variable_properties variable_property
                           | empty'''

def p_base_variable(p):
    'base_variable : simple_indirect_reference'

def p_simple_indirect_reference(p):
    '''simple_indirect_reference : DOLLAR simple_indirect_reference
                                 | reference_variable'''

def p_variable_array_offset(p):
    'variable : variable LBRACKET dim_offset RBRACKET'

def p_reference_variable_array_offset(p):
    'reference_variable : reference_variable LBRACKET dim_offset RBRACKET'

def p_reference_variable_string_offset(p):
    'reference_variable : reference_variable LBRACE expr RBRACE'

def p_reference_variable_compound_variable(p):
    'reference_variable : compound_variable'

def p_expr_string_offset(p):
    'expr : expr LBRACE dim_offset RBRACE'

def p_compound_variable(p):
    '''compound_variable : VARIABLE
                         | DOLLAR LBRACE expr RBRACE'''

def p_dim_offset(p):
    '''dim_offset : expr
                  | empty'''

def p_variable_without_objects(p):
    'variable_without_objects : simple_indirect_reference'

def p_expr_scalar(p):
    'expr : scalar'

def p_expr_array(p):
    '''expr : ARRAY LPAREN array_pair_list RPAREN
            | LBRACKET array_pair_list RBRACKET'''

def p_array_pair_list(p):
    '''array_pair_list : empty
                       | non_empty_array_pair_list possible_comma'''

def p_non_empty_array_pair_list_item(p):
    '''non_empty_array_pair_list : non_empty_array_pair_list COMMA AND variable
                                 | non_empty_array_pair_list COMMA expr
                                 | AND variable
                                 | expr'''

def p_non_empty_array_pair_list_pair(p):
    '''non_empty_array_pair_list : non_empty_array_pair_list COMMA expr DOUBLE_ARROW AND variable
                                 | non_empty_array_pair_list COMMA expr DOUBLE_ARROW expr
                                 | expr DOUBLE_ARROW AND variable
                                 | expr DOUBLE_ARROW expr'''

def p_possible_comma(p):
    '''possible_comma : empty
                      | COMMA'''

def p_function_call_parameter_list(p):
    '''function_call_parameter_list : function_call_parameter_list COMMA function_call_parameter
                                    | function_call_parameter'''

def p_function_call_parameter_list_empty(p):
    'function_call_parameter_list : empty'

def p_function_call_parameter(p):
    '''function_call_parameter : expr
                               | AND variable'''

def p_expr_function(p):
    'expr : FUNCTION is_reference LPAREN parameter_list RPAREN lexical_vars LBRACE inner_statement_list RBRACE'

def p_lexical_vars(p):
    '''lexical_vars : USE LPAREN lexical_var_list RPAREN
                    | empty'''

def p_lexical_var_list(p):
    '''lexical_var_list : lexical_var_list COMMA AND VARIABLE
                        | lexical_var_list COMMA VARIABLE
                        | AND VARIABLE
                        | VARIABLE'''


def p_expr_assign_op(p):
    '''expr : variable PLUS_EQUAL expr
            | variable MINUS_EQUAL expr
            | variable MUL_EQUAL expr
            | variable DIV_EQUAL expr
            | variable CONCAT_EQUAL expr
            | variable MOD_EQUAL expr
            | variable AND_EQUAL expr
            | variable OR_EQUAL expr
            | variable XOR_EQUAL expr
            | variable SL_EQUAL expr
            | variable SR_EQUAL expr'''

def p_expr_binary_op(p):
    '''expr : expr BOOLEAN_AND expr
            | expr BOOLEAN_OR expr
            | expr LOGICAL_AND expr
            | expr LOGICAL_OR expr
            | expr LOGICAL_XOR expr
            | expr AND expr
            | expr OR expr
            | expr XOR expr
            | expr CONCAT expr
            | expr PLUS expr
            | expr MINUS expr
            | expr MUL expr
            | expr DIV expr
            | expr SL expr
            | expr SR expr
            | expr MOD expr
            | expr IS_IDENTICAL expr
            | expr IS_NOT_IDENTICAL expr
            | expr IS_EQUAL_TO expr
            | expr IS_NOT_EQUAL expr
            | expr LESS_THAN expr
            | expr LESS_THAN_OR_EQUAL expr
            | expr GREATER_THAN expr
            | expr GRATER_THAN_OR_EQUAL expr
            | expr INSTANCEOF expr
            | expr INSTANCEOF STATIC'''

def p_expr_unary_op(p):
    '''expr : PLUS expr
            | MINUS expr
            | NOT expr
            | BOOLEAN_NOT expr'''

# *************