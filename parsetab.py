
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "programleftANDOREQNEQleftGTELTE><left+-$left*/%leftUMINUS!leftINDEXALLOC AND ATOI DEF ELSE EQ FALSE FREE GTE ID IF INPUT LTE NEQ NUM OR PRINT PRINTI PRINTLN RETURN STR STRING TRUE VAR WHILEprogram : declist start funlist entrypoint stmtlist start :entrypoint :fun : DEF fun_name '(' idlist ')' block \n           | DEF fun_name '(' ')' block fun_name : ID stmt : PRINT '(' expr ')' ';' stmt : PRINTLN '(' ')' ';' stmt : WHILE new_label '(' expr ')' jz block stmt : IF '(' expr ')' jz block \n            | IF '(' expr ')' jz block ELSE jmp jz_label block jmp :jz :jz_label :new_label :var_declare : VAR ID '=' expr ';' \n                   | VAR ID ';' stmt : ID '=' expr ';' stmt : expr '[' expr ']' '=' expr ';' stmt : RETURN expr ';' \n            | RETURN ';' stmt : PRINTI '(' expr ')' ';' stmt : expr ';' stmt : FREE '(' expr ')' ';' expr : ALLOC '(' NUM ')' expr : INPUT '(' ')' expr : STR '(' expr ')' expr : ATOI '(' expr ')' expr : expr '+' expr \n            | expr '-' expr\n            | expr '*' expr \n            | expr '/' expr\n            | expr '%' expr\n            | expr OR expr\n            | expr AND expr \n            | expr '>' expr \n            | expr '<' expr \n            | expr GTE expr\n            | expr LTE expr \n            | expr EQ expr\n            | expr NEQ expr\n            | expr '$' expr expr : '!' expr expr : '-' expr %prec UMINUS expr : ID expr : expr '[' expr ']' %prec INDEX expr : STRING expr : NUM expr : TRUE expr : FALSE expr : ID '(' exprlist ')' \n            | ID '(' ')' expr : '(' expr ')' declist : declist var_declare\n               |funlist : funlist fun \n               |stmtlist : stmtlist stmt \n                |idlist : idlist ',' ID\n              | ID exprlist : exprlist ',' expr\n                | expr block : '{' stmtlist '}' \n             | stmt "
    
_lr_action_items = {'VAR':([0,2,4,12,41,],[-55,5,-54,-17,-16,]),'DEF':([0,2,3,4,6,9,12,41,66,72,107,112,114,123,126,129,133,137,138,139,142,143,144,148,],[-55,-2,-57,-54,10,-56,-17,-16,-23,-21,-20,-5,-65,-8,-18,-4,-7,-22,-24,-64,-10,-19,-9,-11,]),'PRINT':([0,2,3,4,6,8,9,12,13,29,41,66,72,76,107,110,112,113,114,123,125,126,129,131,133,135,136,137,138,139,141,142,143,144,145,146,147,148,],[-55,-2,-57,-54,-3,-59,-56,-17,30,-58,-16,-23,-21,30,-20,30,-5,-59,-65,-8,-13,-18,-4,30,-7,-13,30,-22,-24,-64,30,-10,-19,-9,-12,-14,30,-11,]),'PRINTLN':([0,2,3,4,6,8,9,12,13,29,41,66,72,76,107,110,112,113,114,123,125,126,129,131,133,135,136,137,138,139,141,142,143,144,145,146,147,148,],[-55,-2,-57,-54,-3,-59,-56,-17,32,-58,-16,-23,-21,32,-20,32,-5,-59,-65,-8,-13,-18,-4,32,-7,-13,32,-22,-24,-64,32,-10,-19,-9,-12,-14,32,-11,]),'WHILE':([0,2,3,4,6,8,9,12,13,29,41,66,72,76,107,110,112,113,114,123,125,126,129,131,133,135,136,137,138,139,141,142,143,144,145,146,147,148,],[-55,-2,-57,-54,-3,-59,-56,-17,33,-58,-16,-23,-21,33,-20,33,-5,-59,-65,-8,-13,-18,-4,33,-7,-13,33,-22,-24,-64,33,-10,-19,-9,-12,-14,33,-11,]),'IF':([0,2,3,4,6,8,9,12,13,29,41,66,72,76,107,110,112,113,114,123,125,126,129,131,133,135,136,137,138,139,141,142,143,144,145,146,147,148,],[-55,-2,-57,-54,-3,-59,-56,-17,34,-58,-16,-23,-21,34,-20,34,-5,-59,-65,-8,-13,-18,-4,34,-7,-13,34,-22,-24,-64,34,-10,-19,-9,-12,-14,34,-11,]),'ID':([0,2,3,4,5,6,8,9,10,11,12,13,19,24,25,29,36,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,60,61,64,65,66,69,70,72,73,74,76,104,107,110,111,112,113,114,116,123,125,126,129,131,133,134,135,136,137,138,139,141,142,143,144,145,146,147,148,],[-55,-2,-57,-54,7,-3,-59,-56,15,16,-17,35,16,16,16,-58,16,77,16,-16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-23,16,16,-21,16,16,35,16,-20,35,130,-5,-59,-65,16,-8,-13,-18,-4,35,-7,16,-13,35,-22,-24,-64,35,-10,-19,-9,-12,-14,35,-11,]),'RETURN':([0,2,3,4,6,8,9,12,13,29,41,66,72,76,107,110,112,113,114,123,125,126,129,131,133,135,136,137,138,139,141,142,143,144,145,146,147,148,],[-55,-2,-57,-54,-3,-59,-56,-17,36,-58,-16,-23,-21,36,-20,36,-5,-59,-65,-8,-13,-18,-4,36,-7,-13,36,-22,-24,-64,36,-10,-19,-9,-12,-14,36,-11,]),'PRINTI':([0,2,3,4,6,8,9,12,13,29,41,66,72,76,107,110,112,113,114,123,125,126,129,131,133,135,136,137,138,139,141,142,143,144,145,146,147,148,],[-55,-2,-57,-54,-3,-59,-56,-17,37,-58,-16,-23,-21,37,-20,37,-5,-59,-65,-8,-13,-18,-4,37,-7,-13,37,-22,-24,-64,37,-10,-19,-9,-12,-14,37,-11,]),'FREE':([0,2,3,4,6,8,9,12,13,29,41,66,72,76,107,110,112,113,114,123,125,126,129,131,133,135,136,137,138,139,141,142,143,144,145,146,147,148,],[-55,-2,-57,-54,-3,-59,-56,-17,38,-58,-16,-23,-21,38,-20,38,-5,-59,-65,-8,-13,-18,-4,38,-7,-13,38,-22,-24,-64,38,-10,-19,-9,-12,-14,38,-11,]),'ALLOC':([0,2,3,4,6,8,9,11,12,13,19,24,25,29,36,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,60,61,64,65,66,69,70,72,73,74,76,104,107,110,112,113,114,116,123,125,126,129,131,133,134,135,136,137,138,139,141,142,143,144,145,146,147,148,],[-55,-2,-57,-54,-3,-59,-56,18,-17,18,18,18,18,-58,18,18,-16,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-23,18,18,-21,18,18,18,18,-20,18,-5,-59,-65,18,-8,-13,-18,-4,18,-7,18,-13,18,-22,-24,-64,18,-10,-19,-9,-12,-14,18,-11,]),'INPUT':([0,2,3,4,6,8,9,11,12,13,19,24,25,29,36,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,60,61,64,65,66,69,70,72,73,74,76,104,107,110,112,113,114,116,123,125,126,129,131,133,134,135,136,137,138,139,141,142,143,144,145,146,147,148,],[-55,-2,-57,-54,-3,-59,-56,21,-17,21,21,21,21,-58,21,21,-16,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-23,21,21,-21,21,21,21,21,-20,21,-5,-59,-65,21,-8,-13,-18,-4,21,-7,21,-13,21,-22,-24,-64,21,-10,-19,-9,-12,-14,21,-11,]),'STR':([0,2,3,4,6,8,9,11,12,13,19,24,25,29,36,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,60,61,64,65,66,69,70,72,73,74,76,104,107,110,112,113,114,116,123,125,126,129,131,133,134,135,136,137,138,139,141,142,143,144,145,146,147,148,],[-55,-2,-57,-54,-3,-59,-56,22,-17,22,22,22,22,-58,22,22,-16,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,-23,22,22,-21,22,22,22,22,-20,22,-5,-59,-65,22,-8,-13,-18,-4,22,-7,22,-13,22,-22,-24,-64,22,-10,-19,-9,-12,-14,22,-11,]),'ATOI':([0,2,3,4,6,8,9,11,12,13,19,24,25,29,36,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,60,61,64,65,66,69,70,72,73,74,76,104,107,110,112,113,114,116,123,125,126,129,131,133,134,135,136,137,138,139,141,142,143,144,145,146,147,148,],[-55,-2,-57,-54,-3,-59,-56,23,-17,23,23,23,23,-58,23,23,-16,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-23,23,23,-21,23,23,23,23,-20,23,-5,-59,-65,23,-8,-13,-18,-4,23,-7,23,-13,23,-22,-24,-64,23,-10,-19,-9,-12,-14,23,-11,]),'!':([0,2,3,4,6,8,9,11,12,13,19,24,25,29,36,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,60,61,64,65,66,69,70,72,73,74,76,104,107,110,112,113,114,116,123,125,126,129,131,133,134,135,136,137,138,139,141,142,143,144,145,146,147,148,],[-55,-2,-57,-54,-3,-59,-56,25,-17,25,25,25,25,-58,25,25,-16,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-23,25,25,-21,25,25,25,25,-20,25,-5,-59,-65,25,-8,-13,-18,-4,25,-7,25,-13,25,-22,-24,-64,25,-10,-19,-9,-12,-14,25,-11,]),'-':([0,2,3,4,6,8,9,11,12,13,16,17,19,20,24,25,26,27,28,29,31,35,36,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,58,60,61,62,63,64,65,66,69,70,71,72,73,74,76,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,100,101,102,104,105,106,107,108,109,110,112,113,114,115,116,117,118,119,120,122,123,124,125,126,129,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,],[-55,-2,-57,-54,-3,-59,-56,24,-17,24,-45,43,24,-48,24,24,-47,-49,-50,-58,43,-45,24,24,-16,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,43,24,24,-44,-43,24,24,-23,24,24,43,-21,24,24,24,-52,43,-29,-30,-31,-32,-33,43,43,43,43,43,43,43,43,-42,43,-53,-26,43,43,43,43,24,43,43,-20,43,43,24,-5,-59,-65,-51,24,-46,-25,-27,-28,-46,-8,43,-13,-18,-4,24,43,-7,24,-13,24,-22,-24,-64,43,24,-10,-19,-9,-12,-14,24,-11,]),'STRING':([0,2,3,4,6,8,9,11,12,13,19,24,25,29,36,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,60,61,64,65,66,69,70,72,73,74,76,104,107,110,112,113,114,116,123,125,126,129,131,133,134,135,136,137,138,139,141,142,143,144,145,146,147,148,],[-55,-2,-57,-54,-3,-59,-56,26,-17,26,26,26,26,-58,26,26,-16,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-23,26,26,-21,26,26,26,26,-20,26,-5,-59,-65,26,-8,-13,-18,-4,26,-7,26,-13,26,-22,-24,-64,26,-10,-19,-9,-12,-14,26,-11,]),'NUM':([0,2,3,4,6,8,9,11,12,13,19,24,25,29,36,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,60,61,64,65,66,69,70,72,73,74,76,104,107,110,112,113,114,116,123,125,126,129,131,133,134,135,136,137,138,139,141,142,143,144,145,146,147,148,],[-55,-2,-57,-54,-3,-59,-56,20,-17,20,20,20,20,-58,20,20,-16,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,96,20,20,20,20,-23,20,20,-21,20,20,20,20,-20,20,-5,-59,-65,20,-8,-13,-18,-4,20,-7,20,-13,20,-22,-24,-64,20,-10,-19,-9,-12,-14,20,-11,]),'TRUE':([0,2,3,4,6,8,9,11,12,13,19,24,25,29,36,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,60,61,64,65,66,69,70,72,73,74,76,104,107,110,112,113,114,116,123,125,126,129,131,133,134,135,136,137,138,139,141,142,143,144,145,146,147,148,],[-55,-2,-57,-54,-3,-59,-56,27,-17,27,27,27,27,-58,27,27,-16,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-23,27,27,-21,27,27,27,27,-20,27,-5,-59,-65,27,-8,-13,-18,-4,27,-7,27,-13,27,-22,-24,-64,27,-10,-19,-9,-12,-14,27,-11,]),'FALSE':([0,2,3,4,6,8,9,11,12,13,19,24,25,29,36,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,60,61,64,65,66,69,70,72,73,74,76,104,107,110,112,113,114,116,123,125,126,129,131,133,134,135,136,137,138,139,141,142,143,144,145,146,147,148,],[-55,-2,-57,-54,-3,-59,-56,28,-17,28,28,28,28,-58,28,28,-16,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,-23,28,28,-21,28,28,28,28,-20,28,-5,-59,-65,28,-8,-13,-18,-4,28,-7,28,-13,28,-22,-24,-64,28,-10,-19,-9,-12,-14,28,-11,]),'(':([0,2,3,4,6,8,9,11,12,13,14,15,16,18,19,21,22,23,24,25,29,30,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,60,61,64,65,66,68,69,70,72,73,74,76,104,107,110,112,113,114,116,123,125,126,129,131,133,134,135,136,137,138,139,141,142,143,144,145,146,147,148,],[-55,-2,-57,-54,-3,-59,-56,19,-17,19,39,-6,40,57,19,59,60,61,19,19,-58,64,67,-15,69,40,19,73,74,19,-16,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-23,104,19,19,-21,19,19,19,19,-20,19,-5,-59,-65,19,-8,-13,-18,-4,19,-7,19,-13,19,-22,-24,-64,19,-10,-19,-9,-12,-14,19,-11,]),'$end':([0,1,2,3,4,6,8,9,12,13,29,41,66,72,107,112,114,123,126,129,133,137,138,139,142,143,144,148,],[-55,0,-2,-57,-54,-3,-59,-56,-17,-1,-58,-16,-23,-21,-20,-5,-65,-8,-18,-4,-7,-22,-24,-64,-10,-19,-9,-11,]),'=':([7,35,122,],[11,70,134,]),';':([7,16,17,20,26,27,28,31,35,36,62,63,71,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,97,98,103,106,115,117,118,119,120,121,122,127,128,140,],[12,-45,41,-48,-47,-49,-50,66,-45,72,-44,-43,107,-52,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-53,-26,123,126,-51,-46,-25,-27,-28,133,-46,137,138,143,]),'+':([16,17,20,26,27,28,31,35,58,62,63,71,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,100,101,102,105,106,108,109,115,117,118,119,120,122,124,132,140,],[-45,42,-48,-47,-49,-50,42,-45,42,-44,-43,42,-52,42,-29,-30,-31,-32,-33,42,42,42,42,42,42,42,42,-42,42,-53,-26,42,42,42,42,42,42,42,42,-51,-46,-25,-27,-28,-46,42,42,42,]),'*':([16,17,20,26,27,28,31,35,58,62,63,71,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,100,101,102,105,106,108,109,115,117,118,119,120,122,124,132,140,],[-45,44,-48,-47,-49,-50,44,-45,44,-44,-43,44,-52,44,44,44,-31,-32,-33,44,44,44,44,44,44,44,44,44,44,-53,-26,44,44,44,44,44,44,44,44,-51,-46,-25,-27,-28,-46,44,44,44,]),'/':([16,17,20,26,27,28,31,35,58,62,63,71,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,100,101,102,105,106,108,109,115,117,118,119,120,122,124,132,140,],[-45,45,-48,-47,-49,-50,45,-45,45,-44,-43,45,-52,45,45,45,-31,-32,-33,45,45,45,45,45,45,45,45,45,45,-53,-26,45,45,45,45,45,45,45,45,-51,-46,-25,-27,-28,-46,45,45,45,]),'%':([16,17,20,26,27,28,31,35,58,62,63,71,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,100,101,102,105,106,108,109,115,117,118,119,120,122,124,132,140,],[-45,46,-48,-47,-49,-50,46,-45,46,-44,-43,46,-52,46,46,46,-31,-32,-33,46,46,46,46,46,46,46,46,46,46,-53,-26,46,46,46,46,46,46,46,46,-51,-46,-25,-27,-28,-46,46,46,46,]),'OR':([16,17,20,26,27,28,31,35,58,62,63,71,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,100,101,102,105,106,108,109,115,117,118,119,120,122,124,132,140,],[-45,47,-48,-47,-49,-50,47,-45,47,-44,-43,47,-52,47,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,47,-53,-26,47,47,47,47,47,47,47,47,-51,-46,-25,-27,-28,-46,47,47,47,]),'AND':([16,17,20,26,27,28,31,35,58,62,63,71,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,100,101,102,105,106,108,109,115,117,118,119,120,122,124,132,140,],[-45,48,-48,-47,-49,-50,48,-45,48,-44,-43,48,-52,48,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,48,-53,-26,48,48,48,48,48,48,48,48,-51,-46,-25,-27,-28,-46,48,48,48,]),'>':([16,17,20,26,27,28,31,35,58,62,63,71,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,100,101,102,105,106,108,109,115,117,118,119,120,122,124,132,140,],[-45,49,-48,-47,-49,-50,49,-45,49,-44,-43,49,-52,49,-29,-30,-31,-32,-33,49,49,-36,-37,-38,-39,49,49,-42,49,-53,-26,49,49,49,49,49,49,49,49,-51,-46,-25,-27,-28,-46,49,49,49,]),'<':([16,17,20,26,27,28,31,35,58,62,63,71,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,100,101,102,105,106,108,109,115,117,118,119,120,122,124,132,140,],[-45,50,-48,-47,-49,-50,50,-45,50,-44,-43,50,-52,50,-29,-30,-31,-32,-33,50,50,-36,-37,-38,-39,50,50,-42,50,-53,-26,50,50,50,50,50,50,50,50,-51,-46,-25,-27,-28,-46,50,50,50,]),'GTE':([16,17,20,26,27,28,31,35,58,62,63,71,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,100,101,102,105,106,108,109,115,117,118,119,120,122,124,132,140,],[-45,51,-48,-47,-49,-50,51,-45,51,-44,-43,51,-52,51,-29,-30,-31,-32,-33,51,51,-36,-37,-38,-39,51,51,-42,51,-53,-26,51,51,51,51,51,51,51,51,-51,-46,-25,-27,-28,-46,51,51,51,]),'LTE':([16,17,20,26,27,28,31,35,58,62,63,71,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,100,101,102,105,106,108,109,115,117,118,119,120,122,124,132,140,],[-45,52,-48,-47,-49,-50,52,-45,52,-44,-43,52,-52,52,-29,-30,-31,-32,-33,52,52,-36,-37,-38,-39,52,52,-42,52,-53,-26,52,52,52,52,52,52,52,52,-51,-46,-25,-27,-28,-46,52,52,52,]),'EQ':([16,17,20,26,27,28,31,35,58,62,63,71,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,100,101,102,105,106,108,109,115,117,118,119,120,122,124,132,140,],[-45,53,-48,-47,-49,-50,53,-45,53,-44,-43,53,-52,53,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,53,-53,-26,53,53,53,53,53,53,53,53,-51,-46,-25,-27,-28,-46,53,53,53,]),'NEQ':([16,17,20,26,27,28,31,35,58,62,63,71,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,100,101,102,105,106,108,109,115,117,118,119,120,122,124,132,140,],[-45,54,-48,-47,-49,-50,54,-45,54,-44,-43,54,-52,54,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,54,-53,-26,54,54,54,54,54,54,54,54,-51,-46,-25,-27,-28,-46,54,54,54,]),'$':([16,17,20,26,27,28,31,35,58,62,63,71,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,100,101,102,105,106,108,109,115,117,118,119,120,122,124,132,140,],[-45,55,-48,-47,-49,-50,55,-45,55,-44,-43,55,-52,55,-29,-30,-31,-32,-33,55,55,55,55,55,55,55,55,-42,55,-53,-26,55,55,55,55,55,55,55,55,-51,-46,-25,-27,-28,-46,55,55,55,]),'[':([16,17,20,26,27,28,31,35,58,62,63,71,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,99,100,101,102,105,106,108,109,115,117,118,119,120,122,124,132,140,],[-45,56,-48,-47,-49,-50,65,-45,56,-44,-43,56,-52,56,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,56,-53,-26,56,56,56,56,56,56,56,56,-51,-46,-25,-27,-28,-46,56,56,56,]),')':([16,20,26,27,28,39,40,58,59,62,63,67,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,96,97,98,99,100,101,105,108,109,115,117,118,119,120,124,130,132,],[-45,-48,-47,-49,-50,76,79,97,98,-44,-43,103,110,-61,115,-52,-63,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,118,-53,-26,119,120,121,125,127,128,-51,-46,-25,-27,-28,135,-60,-62,]),',':([16,20,26,27,28,62,63,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,97,98,115,117,118,119,120,130,132,],[-45,-48,-47,-49,-50,-44,-43,111,-61,116,-52,-63,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-53,-26,-51,-46,-25,-27,-28,-60,-62,]),']':([16,20,26,27,28,62,63,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,98,102,115,117,118,119,120,],[-45,-48,-47,-49,-50,-44,-43,-52,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,117,-53,-26,122,-51,-46,-25,-27,-28,]),'}':([29,66,72,107,113,114,123,126,131,133,137,138,139,142,143,144,148,],[-58,-23,-21,-20,-59,-65,-8,-18,139,-7,-22,-24,-64,-10,-19,-9,-11,]),'ELSE':([66,72,107,114,123,126,133,137,138,139,142,143,144,148,],[-23,-21,-20,-65,-8,-18,-7,-22,-24,-64,145,-19,-9,-11,]),'{':([76,110,125,135,136,141,145,146,147,],[113,113,-13,-13,113,113,-12,-14,113,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declist':([0,],[2,]),'start':([2,],[3,]),'var_declare':([2,],[4,]),'funlist':([3,],[6,]),'entrypoint':([6,],[8,]),'fun':([6,],[9,]),'stmtlist':([8,113,],[13,131,]),'fun_name':([10,],[14,]),'expr':([11,13,19,24,25,36,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,60,61,64,65,69,70,73,74,76,104,110,116,131,134,136,141,147,],[17,31,58,62,63,71,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,99,100,101,102,105,106,108,109,31,124,31,132,31,140,31,31,31,]),'stmt':([13,76,110,131,136,141,147,],[29,114,114,29,114,114,114,]),'new_label':([33,],[68,]),'idlist':([39,],[75,]),'exprlist':([40,],[78,]),'block':([76,110,136,141,147,],[112,129,142,144,148,]),'jz':([125,135,],[136,141,]),'jmp':([145,],[146,]),'jz_label':([146,],[147,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declist start funlist entrypoint stmtlist','program',5,'p_program','parser.py',22),
  ('start -> <empty>','start',0,'p_start','parser.py',26),
  ('entrypoint -> <empty>','entrypoint',0,'p_entrypoint','parser.py',30),
  ('fun -> DEF fun_name ( idlist ) block','fun',6,'p_fun','parser.py',34),
  ('fun -> DEF fun_name ( ) block','fun',5,'p_fun','parser.py',35),
  ('fun_name -> ID','fun_name',1,'p_fun_name','parser.py',45),
  ('stmt -> PRINT ( expr ) ;','stmt',5,'p_stmt_print','parser.py',53),
  ('stmt -> PRINTLN ( ) ;','stmt',4,'p_stmt_println','parser.py',57),
  ('stmt -> WHILE new_label ( expr ) jz block','stmt',7,'p_stmt_while','parser.py',61),
  ('stmt -> IF ( expr ) jz block','stmt',6,'p_stmt_ifelse','parser.py',67),
  ('stmt -> IF ( expr ) jz block ELSE jmp jz_label block','stmt',10,'p_stmt_ifelse','parser.py',68),
  ('jmp -> <empty>','jmp',0,'p_jmp','parser.py',75),
  ('jz -> <empty>','jz',0,'p_jz','parser.py',81),
  ('jz_label -> <empty>','jz_label',0,'p_jz_label','parser.py',88),
  ('new_label -> <empty>','new_label',0,'p_new_label','parser.py',93),
  ('var_declare -> VAR ID = expr ;','var_declare',5,'p_declare','parser.py',99),
  ('var_declare -> VAR ID ;','var_declare',3,'p_declare','parser.py',100),
  ('stmt -> ID = expr ;','stmt',4,'p_stmt_assign','parser.py',110),
  ('stmt -> expr [ expr ] = expr ;','stmt',7,'p_stmt_assign_arr','parser.py',119),
  ('stmt -> RETURN expr ;','stmt',3,'p_stmt_return','parser.py',123),
  ('stmt -> RETURN ;','stmt',2,'p_stmt_return','parser.py',124),
  ('stmt -> PRINTI ( expr ) ;','stmt',5,'p_stmt_printi','parser.py',132),
  ('stmt -> expr ;','stmt',2,'p_stmt_expr','parser.py',136),
  ('stmt -> FREE ( expr ) ;','stmt',5,'p_stmt_free','parser.py',139),
  ('expr -> ALLOC ( NUM )','expr',4,'p_expr_alloc','parser.py',148),
  ('expr -> INPUT ( )','expr',3,'p_expr_input','parser.py',152),
  ('expr -> STR ( expr )','expr',4,'p_expr_str','parser.py',156),
  ('expr -> ATOI ( expr )','expr',4,'p_expr_atoi','parser.py',160),
  ('expr -> expr + expr','expr',3,'p_expr_binop','parser.py',164),
  ('expr -> expr - expr','expr',3,'p_expr_binop','parser.py',165),
  ('expr -> expr * expr','expr',3,'p_expr_binop','parser.py',166),
  ('expr -> expr / expr','expr',3,'p_expr_binop','parser.py',167),
  ('expr -> expr % expr','expr',3,'p_expr_binop','parser.py',168),
  ('expr -> expr OR expr','expr',3,'p_expr_binop','parser.py',169),
  ('expr -> expr AND expr','expr',3,'p_expr_binop','parser.py',170),
  ('expr -> expr > expr','expr',3,'p_expr_binop','parser.py',171),
  ('expr -> expr < expr','expr',3,'p_expr_binop','parser.py',172),
  ('expr -> expr GTE expr','expr',3,'p_expr_binop','parser.py',173),
  ('expr -> expr LTE expr','expr',3,'p_expr_binop','parser.py',174),
  ('expr -> expr EQ expr','expr',3,'p_expr_binop','parser.py',175),
  ('expr -> expr NEQ expr','expr',3,'p_expr_binop','parser.py',176),
  ('expr -> expr $ expr','expr',3,'p_expr_binop','parser.py',177),
  ('expr -> ! expr','expr',2,'p_expr_not','parser.py',197),
  ('expr -> - expr','expr',2,'p_expr_neg','parser.py',201),
  ('expr -> ID','expr',1,'p_expr_id','parser.py',206),
  ('expr -> expr [ expr ]','expr',4,'p_expr_ind','parser.py',215),
  ('expr -> STRING','expr',1,'p_expr_string','parser.py',219),
  ('expr -> NUM','expr',1,'p_expr_num','parser.py',223),
  ('expr -> TRUE','expr',1,'p_expr_true','parser.py',227),
  ('expr -> FALSE','expr',1,'p_expr_false','parser.py',231),
  ('expr -> ID ( exprlist )','expr',4,'p_expr_fun','parser.py',235),
  ('expr -> ID ( )','expr',3,'p_expr_fun','parser.py',236),
  ('expr -> ( expr )','expr',3,'p_expr','parser.py',246),
  ('declist -> declist var_declare','declist',2,'p_declist','parser.py',251),
  ('declist -> <empty>','declist',0,'p_declist','parser.py',252),
  ('funlist -> funlist fun','funlist',2,'p_funlist','parser.py',255),
  ('funlist -> <empty>','funlist',0,'p_funlist','parser.py',256),
  ('stmtlist -> stmtlist stmt','stmtlist',2,'p_stmtlist','parser.py',259),
  ('stmtlist -> <empty>','stmtlist',0,'p_stmtlist','parser.py',260),
  ('idlist -> idlist , ID','idlist',3,'p_idlist','parser.py',263),
  ('idlist -> ID','idlist',1,'p_idlist','parser.py',264),
  ('exprlist -> exprlist , expr','exprlist',3,'p_exprlist','parser.py',271),
  ('exprlist -> expr','exprlist',1,'p_exprlist','parser.py',272),
  ('block -> { stmtlist }','block',3,'p_block','parser.py',275),
  ('block -> stmt','block',1,'p_block','parser.py',276),
]
