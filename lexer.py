import ply.lex as lex
import sys
import re

reserved = {
	'while': 'WHILE',
	'if': 'IF',
	'else': 'ELSE',
	'def': 'DEF',
	'int': 'INT',
	'true': 'TRUE',
	'false': 'FALSE',
	'println': 'PRINTLN',
	'printi': 'PRINTI',
	'prints': 'PRINTS',
	'atoi': 'ATOI',
	'string': 'STRING',
	'return': 'RETURN',
	'void': 'VOID',
	'input': 'INPUT'
}

tokens = (
	'ID',
	'ASSIGN',
	'NUM',
	'NOT',
	'NEG',
	'ADD',
	'SUBT',
	'MULT',
	'DIV',
	'EQ',
	'GEQ',
	'LEQ',
	'LT',
	'GT',
	'NEQ',
	'AND',
	'OR',
	'SC',
	'LPAREN',
	'RPAREN',
	'LCURLY',
	'RCURLY',
	'LBRACKET',
	'RBRACKET',
	'COMMA'
) + tuple(reserved.values())


t_ADD = r'\+'
t_SUBT = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'

t_NOT = r'\!'
t_EQ = r'\=\='
t_GEQ = r'\>\='
t_LEQ = r'\<\='
t_LT = r'\<'
t_GT = r'\>'
t_NEQ = r'\!\='
t_AND = r'\&\&'
t_OR = r'\|\|'

t_ASSIGN = r'\='

t_SC = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r'\,'

t_ignore = ' \t'

def t_ID(t):
	r'[a-zA-Z][a-zA-Z0-9_]*'
	t.type = reserved.get(t.value, 'ID')
	return t

def t_NUM(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_STRING(t):
	r'\".*\"'
	t.type = reserved.get(t.value, 'STRING')
	return t

def t_COMMENT(t):
	r'\/\/.*'
	pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
	print(f"Caracter ilegal {t.value[0]}")
	t.lexer.skip(1)

lexer = lex.lex()