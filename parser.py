import ply.yacc as yacc
import sys, tempfile
from envManager import EnvManager
from lexer import tokens

output = tempfile.TemporaryFile()
env = EnvManager()
error = [False]
entrypoint = [False]
inside_fun = [False]

precedence = (
    ('left', 'AND', 'OR', 'EQ', 'NEQ'),
    ('left', 'GTE', 'LTE', '>', '<'),
    ('left', '+', '-', '$'),
    ('left', '*', '/', '%'),
    ('left', 'UMINUS', '!'),
    ('left', 'INDEX'),
)

def p_program(p):
    '''program : declist start funlist entrypoint stmtlist '''
    output.write(b'STOP')

def p_start(p):
    '''start :'''
    output.write(b'JUMP entrypoint\n')

def p_entrypoint(p):
    '''entrypoint :'''
    output.write(b'entrypoint:\n')

def p_fun(p):
    '''fun : DEF fun_name '(' idlist ')' block 
           | DEF fun_name '(' ')' block '''
    if env.fun_exists(p[2]):
        print('cannot redeclare function')
        error[0] = True
        raise SyntaxError
    env.add_fun(p[2])
    env.pop_fun_scope()
    inside_fun[0] = False

def p_fun_name(p):
    '''fun_name : ID '''
    output.write(f'{p[1]}:\n'.encode('ascii'))
    inside_fun[0] = True
    p[0] = p[1]

# - declaracoes

def p_stmt_print(p):
    '''stmt : PRINT '(' expr ')' ';' '''
    output.write(b'WRITES\n')

def p_stmt_println(p):
    '''stmt : PRINTLN '(' ')' ';' '''
    output.write(b'WRITELN\n')

def p_stmt_while(p):
    '''stmt : WHILE new_label '(' expr ')' jz block '''
    output.write(f'JUMP lbl{p[2]}\n'.encode())
    output.write(f'lbl{p[6]}:\n'.encode())
    env.pop_jz_label()

def p_stmt_ifelse(p):
    '''stmt : IF '(' expr ')' jz block 
            | IF '(' expr ')' jz block ELSE jmp jz_label block '''
    if len(p) == 7:
        output.write(f'lbl{env.get_label()}:\n'.encode('ascii'))
    else:
        output.write(f'lbl{p[8]}:\n'.encode())

def p_jmp(p):
    '''jmp :'''
    env.new_label()
    output.write(f'JUMP lbl{env.get_label()}\n'.encode('ascii'))
    p[0] = env.get_label()

def p_jz(p):
    '''jz :'''
    env.new_label()
    output.write(f'JZ lbl{env.get_label()}\n'.encode('ascii'))
    env.push_jz_label()
    p[0] = env.get_label()

def p_jz_label(p):
    '''jz_label :'''
    output.write(f'lbl{env.pop_jz_label()}:\n'.encode('ascii'))

    
def p_new_label(p):
    '''new_label :'''
    env.new_label()
    output.write(f'lbl{env.get_label()}:\n'.encode())
    p[0] = env.get_label()

def p_declare(p):
    '''var_declare : VAR ID '=' expr ';' 
                   | VAR ID ';' '''
    if env.var_exists(p[2]):
        print(f'cannot redeclare identifier {p[2]}')
        error[0] = True
        raise SyntaxError
    env.add_var(p[2])
    if len(p) == 4:
        output.write(b'PUSHI 0\n')


def p_stmt_assign(p):
    '''stmt : ID '=' expr ';' '''
    if not env.var_exists(p[1]):
        print(f'variable {p[1]} has not been declared')
        error[0] = True
        raise SyntaxError
    address = env.get_var(p[1])
    output.write(f'STOREG {address}\n'.encode('ascii'))

def p_stmt_assign_arr(p):
    '''stmt : arr_id '[' expr ']' '=' expr ';' '''
    output.write(b'STOREN\n')

def p_stmt_arr_id(p):
    '''arr_id : ID '''
    if not env.var_exists(p[1]):
        print(f'variable {p[1]} has not been declared')
        error[0] = True
        raise SyntaxError
    address = env.get_var(p[1])
    output.write(f'PUSHG {address}\n'.encode('ascii'))

def p_stmt_return(p):
    '''stmt : RETURN expr ';' 
            | RETURN ';' '''
    if not inside_fun[0]:
        print('can only return inside of a function')
        error[0] = True
        raise SyntaxError
    output.write(b'RETURN\n')

def p_stmt_printi(p):
    '''stmt : PRINTI '(' expr ')' ';' '''
    output.write(b'WRITEI\n')

def p_stmt_expr(p):
    '''stmt : expr ';' '''
    

# --------------------------

# - expressoes

def p_expr_input(p):
    '''expr : INPUT '(' ')' '''
    output.write(b'READ\n')

def p_expr_str(p):
    '''expr : STR '(' expr ')' '''
    output.write(b'STRI\n')

def p_expr_atoi(p):
    '''expr : ATOI '(' expr ')' '''
    output.write(b'ATOI\n')

def p_expr_alloc(p):
    '''expr : ALLOC '(' expr ')' '''
    output.write(b'ALLOCN\n')

def p_expr_binop(p):
    '''expr : expr '+' expr 
            | expr '-' expr
            | expr '*' expr 
            | expr '/' expr
            | expr '%' expr
            | expr OR expr
            | expr AND expr 
            | expr '>' expr 
            | expr '<' expr 
            | expr GTE expr
            | expr LTE expr 
            | expr EQ expr
            | expr NEQ expr
            | expr '$' expr '''
    ops = {'+': b'ADD\n', 
           '-': b'SUB\n',
           '*': b'MUL\n',
           '/': b'DIV\n',
           '%': b'MOD\n',
           '||': b'OR\n',
           '&&': b'AND\n',
           '>': b'SUP\n',
           '<': b'INF\n',
           '>=': b'SUPEQ\n',
           '<=': b'INFEQ\n',
           '==': b'EQUAL\n',
           '$': b'CONCAT\n',
           '!=': b'EQUAL\nNOT\n'}
    output.write(ops[p[2]])
    if p[2] == '/':
        output.write(b'FTOI\n')

def p_expr_not(p):
    '''expr : '!' expr '''
    output.write(b'NOT\n')

def p_expr_neg(p):
    '''expr : '-' expr %prec UMINUS '''
    output.write(b'PUSHI -1\n')
    output.write(b'MUL\n')

def p_expr_id(p):
    '''expr : ID '''
    if not env.var_exists(p[1]):
        print(f'Unknown identifier {p[1]}')
        error[0] = True
        raise SyntaxError
    address = env.get_var(p[1])
    output.write(f'PUSHG {address}\n'.encode('ascii'))

def p_expr_ind(p):
    '''expr : expr '[' expr ']' %prec INDEX '''
    output.write(b'LOADN\n')

def p_expr_string(p):
    '''expr : STRING '''
    output.write(f'PUSHS {p[1]}\n'.encode('ascii'))

def p_expr_num(p):
    '''expr : NUM '''
    output.write(f'PUSHI {p[1]}\n'.encode('ascii'))

def p_expr_true(p):
    '''expr : TRUE '''
    output.write(b'PUSHI 1\n')

def p_expr_false(p):
    '''expr : FALSE '''
    output.write(b'PUSHI 0\n')

def p_expr_fun(p):
    '''expr : ID '(' exprlist ')' 
            | ID '(' ')' '''
    if not env.fun_exists(p[1]):
        print(f'Unknown function call {p[1]}')
        error[0] = True
        raise SyntaxError
    output.write(f'PUSHA {p[1]}\n'.encode('ascii'))
    output.write(b'CALL\n')
    

def p_expr(p):
    '''expr : '(' expr ')' '''

# ------------------------

def p_declist(p):
    '''declist : declist var_declare
               |'''

def p_funlist(p):
    '''funlist : funlist fun 
               |'''

def p_stmtlist(p):
    '''stmtlist : stmtlist stmt 
                |'''

def p_idlist(p):
    '''idlist : idlist ',' ID
              | ID '''
    if len(p) == 2:
        env.add_fun_var(p[1])
    else:
        env.add_fun_var(p[3])

def p_exprlist(p):
    '''exprlist : exprlist ',' expr
                | expr '''

def p_block(p):
    '''block : '{' stmtlist '}' 
             | stmt '''

def p_error(p):
    error[0] = True
    print(f'Syntax error at token {p.type} line {p.lineno}')

parser = yacc.yacc(start='program')

# linha de comandos

if __name__ == '__main__':
    file = sys.argv[1]
    f = open(file, 'r+')
    try:
        res = parser.parse(f.read())
        if not error[0]:
            output.seek(0)
            print(output.read().decode())
    except Exception as e:
        raise
    output.flush()
    output.close()
    f.close()
