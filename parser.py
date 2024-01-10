import re
import sys
from ply import yacc
from lexer import tokens

def p_program(p):
	'program : declist funlist codeblock'
	if parser.success:
		p[0] = p[1] + p[2] + p[3] + 'STOP'

def p_codeblock1(p):
	'codeblock : stmlist'
	if parser.success:
		p[0] = p[1]

def p_codeblock2(p):
	'codeblock : '
	if parser.success:
		p[0] = ''

def p_declist_1(p):
	'declist : dec declist'
	if parser.success:
		p[0] = p[1] + p[2]

def p_declist_2(p):
	'declist : '
	if parser.success:
		p[0] = ''

def p_dec1(p):
	'dec : dec_int'
	if parser.success:
		p[0] = p[1]

def p_dec2(p):
	'dec : dec_arr'
	if parser.success:
		p[0] = p[1]

def p_dec3(p):
	'dec : dec_mat'
	if parser.success:
		p[0] = p[1]

def p_dec_int(p):
	'dec_int : INT ID SC'
	if parser.success:
		name = p[2]
		if name in parser.dict['funcs']:
			print(f'Error: Identifier already declared as function {name}.')
			parser.success = False
		elif name in parser.dict['vars']:
			print(f'Error: Identifier already declared as variable {name}')
			parser.success = False	
	if parser.success:
		parser.dict['vars'].update({name: 
			{'size': 0,
			 'count': parser.count
			}
		 }
		)
		parser.count += 1
	p[0] = 'PUSHI 0\n'

def p_def_arr(p):
	'dec_arr : INT ID LBRACKET NUM RBRACKET SC'
	if parser.success:
		name = p[2]
		size = p[4]
		if name in parser.dict['funcs']: 
			print(f'Error: Identifier already declared as function {name}.')
			parser.success = False
		elif name in parser.dict['vars']:
			print(f'Error: Identifier already declared as variable {name}')
			parser.success = False
	if parser.success:
		parser.dict['vars'].update({name:
			{'size': size,
			 'count': parser.count
			}
		}
		)
		parser.count += size
	p[0] = f'PUSHN {size}\n'

def p_def_mat(p):
	'dec_mat : INT ID LBRACKET NUM RBRACKET LBRACKET NUM RBRACKET SC'
	if parser.success:
		name = p[2]
		row = p[4]
		col = p[7]
		if name in parser.dict['funcs']:
			print(f'Error: Identifier already declared as function {name}.')
			parser.success = False
		elif name in parser.dict['vars']:
			print(f'Error: Identifier already declared as variable {name}')
			parser.success = False
	if parser.success:
		parser.dict['vars'].update({name:
			{'size': row*col,
			 'count': parser.count,
			 'row':row,
			 'col':col
			}
		}
		)
		parser.count += row*col
	p[0] = f'PUSHN {row*col}\n'

def p_funlist1(p):
	'funlist : fun funlist'
	if parser.success:
		p[0] = p[1] + p[2]

def p_funlist2(p):
	'funlist : '
	if parser.success:
		p[0] = ''

def p_fun1(p):
	'fun : DEF ID LPAREN idlist RPAREN INT LCURLY stmlist RETURN exprl SC RCURLY'
	name = p[2]
	if parser.success:
		if name in parser.dict['funcs']:
			print(f'Error: Cannot redeclare function {name}')
			parser.success = False
		if name in parser.dict['vars']:
			print(f'Error: Identifier already declared as variable {name}')
			parser.success = False
	if parser.success:
		lbl = parser.label
		lbl_next = parser.label + 1
		parser.label += 2
		arguments = p[4].split('\n')
		parser.dict['funcs'].update({name:
			{'name': p[2],
			 'arguments': arguments,
			 'statements': p[8],
			 'lbl': lbl 
			}
		}
		)
	if parser.success:
		p[0] = f'JUMP lbl{lbl_next}\nlbl{lbl}:\n{p[8]}{p[10]}RETURN\nlbl{lbl_next}:\n'

def p_fun2(p):
	'fun : DEF ID LPAREN idlist RPAREN VOID LCURLY stmlist RETURN SC RCURLY'
	name = p[2]
	if parser.success:
		if name in parser.dict['funcs']:
			print(f'Error: Cannot redeclare function {name}')
			parser.success = False
		if name in parser.dict['vars']:
			print(f'Error: Identifier already declared as variable {name}')
			parser.success = False
	if parser.success:
		lbl = parser.label
		lbl_next = parser.label + 1
		parser.label += 2
		arguments = p[4].split('\n')
		parser.dict['funcs'].update({name:
			{'name': p[2],
			 'arguments': arguments,
			 'statements': p[8],
			 'lbl': lbl 
			}
		}
		)
		p[0] = f'JUMP lbl{lbl_next}\nlbl{lbl}:\n{p[8]}RETURN\nlbl{lbl_next}:\n'

def p_idlist1(p):
	'idlist : ID cont'
	if parser.success:
		p[0] = p[1] + '\n' + p[2]

def p_idlist2(p):
	'idlist : '
	if parser.success:
		p[0] = ''

def p_cont1(p):
	'cont : COMMA ID cont'
	if parser.success:
		p[0] = p[2] + '\n' + p[3]

def p_cont2(p):
	'cont : '
	if parser.success:
		p[0] = ''

def p_stmlist1(p):
	'stmlist : stmt stmlist'
	if parser.success:
		p[0] = p[1] + p[2]

def p_stmlist2(p):
	'stmlist : stmt'
	if parser.success:
		p[0] = p[1]

def p_stmt1(p):
	'stmt : PRINTI LPAREN exprl RPAREN SC'
	if parser.success:
		p[0] = p[3] + 'WRITEI\n'

def p_stmt2(p):
	'stmt : PRINTLN LPAREN RPAREN SC'
	if parser.success:
		p[0] = 'WRITELN\n'

def p_stmt3(p):
	'stmt : PRINTS LPAREN STRING RPAREN SC'
	if parser.success:
		p[0] = f'PUSHS {p[3]}\nWRITES\n'

def p_stmt4(p):
	'stmt : WHILE LPAREN exprl RPAREN block'
	if parser.success:
		lbl_ini = parser.label
		lbl_end = parser.label + 1
		parser.label += 2
		p[0] = f'lbl{lbl_ini}:\n{p[3]}JZ lbl{lbl_end}\n{p[5]}JUMP lbl{lbl_ini}\nlbl{lbl_end}:\n'

def p_stmt5(p):
	'stmt : ID ASSIGN exprl SC'
	if parser.success:
		name = p[1]
		if name in parser.dict['vars']:
			address = parser.dict['vars'][name]['count']
		elif name in parser.dict['funcs']:
			print(f'Error: Identifier is function not variable {name}')
			parser.success = False
		else:
			print('Error: Variable not declared.')
			parser.success = False
	if parser.success:
		p[0] = f'{p[3]}STOREG {address}\n'

def p_stmt6(p):
	'stmt : ID LBRACKET exprl RBRACKET ASSIGN exprl SC'
	if parser.success:
		name = p[1]
		if name in parser.dict['vars']:
			address = parser.dict['vars'][name]['count']
		elif name in parser.dict['funcs']:
			print(f'Error: Identifier is function not array {name}')
			parser.success = False
		else:
			print('Error: Array not declared.')
			parser.success = False
	if parser.success:
		p[0] = f'PUSHGP\nPUSHI {address}\nPADD\n{p[3]}{p[6]}STOREN\n'

def p_stmt7(p):
	'stmt : ID LBRACKET exprl RBRACKET LBRACKET exprl RBRACKET ASSIGN exprl SC'
	if parser.success:
		name = p[1]
		row = p[3]
		col = p[6]
		if name in parser.dict['vars']:
			address = parser.dict['vars'][name]['count']
			tot_col = parser.dict['vars'][name]['col']
		elif name in parser.dict['funcs']:
			print(f'Error: Identifier is function not matrix {name}')
			parser.success = False
		else:
			print('Error: Matrix not declared.')
			parser.success = False
		if parser.success:
			p[0] = f'PUSHGP\nPUSHI {address}\n{row}PUSHI {tot_col}\nMUL\nADD\nPADD\n{col}{p[9]}STOREN\n'

def p_stmt8(p):
	'stmt : IF LPAREN exprl RPAREN block ELSE block'
	if parser.success:
		lbl_else = parser.label
		lbl_end = parser.label + 1
		parser.label += 2
		p[0] = f'{p[3]}JZ lbl{lbl_else}\n{p[5]}JUMP lbl{lbl_end}\nlbl{lbl_else}:\n{p[7]}lbl{lbl_end}:\n'

def p_stmt9(p):
	'stmt : IF LPAREN exprl RPAREN block'
	if parser.success:
		lbl_end = parser.label
		parser.label += 1
		p[0] = f'{p[3]}JZ lbl{lbl_end}\n{p[5]}lbl{lbl_end}:\n'

def p_stmt10(p):
	'stmt : INPUT LPAREN RPAREN SC'
	p[0] = 'READ\n'

def p_stmt11(p):
	'stmt : exprl SC'
	p[0] = f'{p[1]}'

def p_block1(p):
	'block : LCURLY stmlist RCURLY'
	if parser.success:
		p[0] = p[2]

def p_block2(p):
	'block : LCURLY stmt RCURLY'
	if parser.success:
		p[0] = p[2]

def p_block3(p):
	'block : stmt'
	if parser.success:
		p[0] = p[1]

def p_exprl1(p):
	'exprl : expr oprl exprl'
	if parser.success:
		p[0] = p[1] + p[3] + p[2]

def p_exprl2(p):
	'exprl : expr'
	if parser.success:
		p[0] = p[1]

def p_expr1(p):
	'expr : expr opra term'
	if parser.success:
		p[0] = p[1] + p[3] + p[2]

def p_expr2(p):
	'expr : term'
	if parser.success:
		p[0] = p[1]

def p_term1(p):
	'term : term oprm factor'
	if parser.success:
		p[0] = p[1] + p[3] + p[2]

def p_term2(p):
	'term : factor'
	if parser.success:
		p[0] = p[1]

def p_factor1(p):
	'factor : LPAREN expr RPAREN'
	if parser.success:
		p[0] = p[2]

def p_factor2(p):
	'factor : ID'
	if parser.success:
		name = p[1]
		if name in parser.dict['vars']:
			address = parser.dict['vars'][name]['count']
		elif name in parser.dict['funcs']:
			print(f'Error: Identifier is function not variable {name}')
			parser.success = False
		else:
			print('Error: Variable not declared.')
			parser.success = False
	if parser.success:
		p[0] = f'PUSHG {address}\n'

def p_factor3(p):
	'factor : NUM'
	if parser.success:
		p[0] = f'PUSHI {p[1]}\n'

def p_factor4(p):
	'factor : NOT exprl'
	if parser.success:
		p[0] = p[2] + 'NOT\n'

def p_factor5(p):
	'factor : NEG exprl'
	if parser.success:
		p[0] = 'PUSHI 0\n' + p[2] + 'SUB\n'

def p_factor6(p):
	'factor : ID LBRACKET exprl RBRACKET'
	if parser.success:
		name = p[1]
		if name in parser.dict['vars']:
			address = parser.dict['vars'][name]['count']
		elif name in parser.dict['funcs']:
			print(f'Error: Identifier is function not array {name}')
			parser.success = False
		else:
			print('Error: Array not declared.')
			parser.success = False
	if parser.success:
		p[0] = f'PUSHGP\nPUSHI {address}\nPADD\n{p[3]}LOADN\n'

def p_factor7(p):
	'factor : ID LBRACKET exprl RBRACKET LBRACKET exprl RBRACKET'
	if parser.success:
		name = p[1]
		row = p[3]
		col = p[6]
		if name in parser.dict['vars']:
			address = parser.dict['vars'][name]['count']
			tot_col = parser.dict['vars'][name]['col']
		elif name in parser.dict['funcs']:
			print(f'Error: Identifier is function not matrix {name}')
			parser.success = False
		else:
			print('Error: Matrix not defined.')
			parser.success = False
	if parser.success:
		p[0] = f'PUSHGP\nPUSHI {address}\n{row}PUSHI {tot_col}\nMUL\nADD\nPADD\n{col}LOADN\n'

def p_factor8(p):
	'factor : ATOI LPAREN argatoi RPAREN'
	if parser.success:
		p[0] = f'{p[3]}\nATOI\n'

def p_factor9(p):
	'factor : ID LPAREN exprllist RPAREN'
	if parser.success:
		name = p[1]
		args = p[3]
		if name in parser.dict['funcs']:
			lbl = parser.dict['funcs'][name]['lbl']
		elif name in parser.dict['vars']:
			print(f'Error: Identifier is variable not function {name}')
			parser.success = False
		else:
			print('Error: Function not declared.')
			parser.success = False
	if parser.success:
		args = args.split('\n')
		res_args = ''
		for arg in args:
			res_args += f'{arg}\n'
		res_args = res_args[:-1]
		for arg in reversed(parser.dict['funcs'][name]['arguments']):
			if arg not in ['', '\n']:
				address = parser.dict['vars'][arg]['count']
				res_args += f'STOREG {address}\n'
	if parser.success:
		if len(res_args) > 0:
			p[0] = res_args + f'PUSHA lbl{lbl}\nCALL\n'
		else:
			p[0] = f'\nPUSHA lbl{lbl}\nCALL\n'

def p_factor10(p):
	'factor : TRUE'
	p[0] = 'PUSHI 1\n'

def p_factor11(p):
	'factor : FALSE'
	p[0] = 'PUSHI 0\n'

def p_exprllist1(p):
	'exprllist : exprl contexprllist'
	p[0] = p[1] + p[2]

def p_exprllist2(p):
	'exprllist : '
	p[0] = ''

def p_contexprllist(p):
	'contexprllist : COMMA exprl contexprllist'
	p[0] = p[2] + p[3]

def p_contexprllist2(p):
	'contexprllist : '
	p[0] = ''

def p_argatoi1(p):
	'argatoi : STRING'
	if parser.success:
		p[0] = f'PUSHS {p[1]}'

def p_argatoi2(p):
	'argatoi : INPUT LPAREN RPAREN'
	if parser.success:
		p[0] = f'READ'

def p_opra1(p):
	'opra : ADD'
	if parser.success:
		p[0] = 'ADD\n'

def p_opra2(p):
	'opra : SUBT'
	if parser.success:
		p[0] = 'SUB\n'

def p_oprm1(p):
	'oprm : MULT'
	if parser.success:
		p[0] = 'MUL\n'

def p_oprm2(p):
	'oprm : DIV'
	if parser.success:
		p[0] = 'DIV\nFTOI\n'

def p_oprl1(p):
	'oprl : EQ'
	if parser.success:
		p[0] = 'EQUAL\n'

def p_oprl2(p):
	'oprl : GEQ'
	if parser.success:
		p[0] = 'SUPEQ\n'

def p_oprl3(p):
	'oprl : LEQ'
	if parser.success:
		p[0] = 'INFEQ\n'

def p_oprl4(p):
	'oprl : LT'
	if parser.success:
		p[0] = 'INF\n'

def p_oprl5(p):
	'oprl : GT'
	if parser.success:
		p[0] = 'SUP\n'

def p_oprl6(p):
	'oprl : NEQ'
	if parser.success:
		p[0] = 'EQUAL\nNOT\n'

def p_oprl7(p):
	'oprl : AND'
	if parser.success:
		p[0] = 'AND\n'

def p_oprl8(p):
	'oprl : OR'
	if parser.success:
		p[0] = 'OR\n'

def p_error(p):
	parser.success = False
	print(f'Error: Error in line {parser.line}\n{p}')

parser = yacc.yacc(start='program')
parser.count = 0
parser.label = 0
parser.line = 0

parser.dict = {
	'vars': {},
	'funcs': {}
}

if __name__ == '__main__':
	file = sys.argv[1]
	f = open(file, 'r+')
	parser.success = True
	res = parser.parse(f.read())
	print(res)
	f.close()