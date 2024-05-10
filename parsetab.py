
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "CHAR COMMENT CR DEPTH DO DOTQUOTE DROP DUP ELSE EMIT IF INT KEY LOOP NAME OPR PLUSLOOP SPACE SPACES SWAP THEN WORDexp : term\n           | function\n           | conditional\n           | loop\n    exp : exp termexp : exp functionexp : exp conditionalterm : factfunction : ':' NAME ';'function : ':' NAME exp ';'conditional : IF ELSE THENconditional : IF exp ELSE THENconditional : IF ELSE exp THENconditional : IF exp ELSE exp THENloop : DO LOOPloop : DO exp LOOPloop : DO PLUSLOOPloop : DO exp PLUSLOOPfact : OPRfact : INTfact : WORDfact : COMMENTfact : '.'fact : DOTQUOTEfact : EMITfact : CHARfact : DUPfact : CRfact : SPACEfact : SPACESfact : SWAPfact : KEYfact : DEPTHfact : DROP"
    
_lr_action_items = {':':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[7,7,-1,-2,-3,-4,-8,7,7,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,7,7,7,-15,7,-17,-9,7,-11,7,7,-16,-18,-10,-13,7,-12,-14,]),'IF':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[8,8,-1,-2,-3,-4,-8,8,8,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,8,8,8,-15,8,-17,-9,8,-11,8,8,-16,-18,-10,-13,8,-12,-14,]),'DO':([0,8,9,29,30,39,],[9,9,9,9,9,9,]),'OPR':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[10,10,-1,-2,-3,-4,-8,10,10,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,10,10,10,-15,10,-17,-9,10,-11,10,10,-16,-18,-10,-13,10,-12,-14,]),'INT':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[11,11,-1,-2,-3,-4,-8,11,11,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,11,11,11,-15,11,-17,-9,11,-11,11,11,-16,-18,-10,-13,11,-12,-14,]),'WORD':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[12,12,-1,-2,-3,-4,-8,12,12,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,12,12,12,-15,12,-17,-9,12,-11,12,12,-16,-18,-10,-13,12,-12,-14,]),'COMMENT':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[13,13,-1,-2,-3,-4,-8,13,13,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,13,13,13,-15,13,-17,-9,13,-11,13,13,-16,-18,-10,-13,13,-12,-14,]),'.':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[14,14,-1,-2,-3,-4,-8,14,14,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,14,14,14,-15,14,-17,-9,14,-11,14,14,-16,-18,-10,-13,14,-12,-14,]),'DOTQUOTE':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[15,15,-1,-2,-3,-4,-8,15,15,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,15,15,15,-15,15,-17,-9,15,-11,15,15,-16,-18,-10,-13,15,-12,-14,]),'EMIT':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[16,16,-1,-2,-3,-4,-8,16,16,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,16,16,16,-15,16,-17,-9,16,-11,16,16,-16,-18,-10,-13,16,-12,-14,]),'CHAR':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[17,17,-1,-2,-3,-4,-8,17,17,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,17,17,17,-15,17,-17,-9,17,-11,17,17,-16,-18,-10,-13,17,-12,-14,]),'DUP':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[18,18,-1,-2,-3,-4,-8,18,18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,18,18,18,-15,18,-17,-9,18,-11,18,18,-16,-18,-10,-13,18,-12,-14,]),'CR':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[19,19,-1,-2,-3,-4,-8,19,19,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,19,19,19,-15,19,-17,-9,19,-11,19,19,-16,-18,-10,-13,19,-12,-14,]),'SPACE':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[20,20,-1,-2,-3,-4,-8,20,20,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,20,20,20,-15,20,-17,-9,20,-11,20,20,-16,-18,-10,-13,20,-12,-14,]),'SPACES':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[21,21,-1,-2,-3,-4,-8,21,21,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,21,21,21,-15,21,-17,-9,21,-11,21,21,-16,-18,-10,-13,21,-12,-14,]),'SWAP':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[22,22,-1,-2,-3,-4,-8,22,22,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,22,22,22,-15,22,-17,-9,22,-11,22,22,-16,-18,-10,-13,22,-12,-14,]),'KEY':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[23,23,-1,-2,-3,-4,-8,23,23,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,23,23,23,-15,23,-17,-9,23,-11,23,23,-16,-18,-10,-13,23,-12,-14,]),'DEPTH':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[24,24,-1,-2,-3,-4,-8,24,24,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,24,24,24,-15,24,-17,-9,24,-11,24,24,-16,-18,-10,-13,24,-12,-14,]),'DROP':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[25,25,-1,-2,-3,-4,-8,25,25,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,25,25,25,-15,25,-17,-9,25,-11,25,25,-16,-18,-10,-13,25,-12,-14,]),'$end':([1,2,3,4,5,6,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,32,34,35,37,40,41,42,43,45,46,],[0,-1,-2,-3,-4,-8,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,-15,-17,-9,-11,-16,-18,-10,-13,-12,-14,]),'ELSE':([2,3,4,5,6,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,31,32,34,35,37,40,41,42,43,45,46,],[-1,-2,-3,-4,-8,30,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,39,-15,-17,-9,-11,-16,-18,-10,-13,-12,-14,]),'LOOP':([2,3,4,5,6,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,32,33,34,35,37,40,41,42,43,45,46,],[-1,-2,-3,-4,-8,32,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,-15,40,-17,-9,-11,-16,-18,-10,-13,-12,-14,]),'PLUSLOOP':([2,3,4,5,6,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,32,33,34,35,37,40,41,42,43,45,46,],[-1,-2,-3,-4,-8,34,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,-15,41,-17,-9,-11,-16,-18,-10,-13,-12,-14,]),';':([2,3,4,5,6,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,32,34,35,36,37,40,41,42,43,45,46,],[-1,-2,-3,-4,-8,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,35,-15,-17,-9,42,-11,-16,-18,-10,-13,-12,-14,]),'THEN':([2,3,4,5,6,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,32,34,35,37,38,39,40,41,42,43,44,45,46,],[-1,-2,-3,-4,-8,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-5,-6,-7,37,-15,-17,-9,-11,43,45,-16,-18,-10,-13,46,-12,-14,]),'NAME':([7,],[29,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'exp':([0,8,9,29,30,39,],[1,31,33,36,38,44,]),'term':([0,1,8,9,29,30,31,33,36,38,39,44,],[2,26,2,2,2,2,26,26,26,26,2,26,]),'function':([0,1,8,9,29,30,31,33,36,38,39,44,],[3,27,3,3,3,3,27,27,27,27,3,27,]),'conditional':([0,1,8,9,29,30,31,33,36,38,39,44,],[4,28,4,4,4,4,28,28,28,28,4,28,]),'loop':([0,8,9,29,30,39,],[5,5,5,5,5,5,]),'fact':([0,1,8,9,29,30,31,33,36,38,39,44,],[6,6,6,6,6,6,6,6,6,6,6,6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> exp","S'",1,None,None,None),
  ('exp -> term','exp',1,'p_exp1','expression_gt.py',9),
  ('exp -> function','exp',1,'p_exp1','expression_gt.py',10),
  ('exp -> conditional','exp',1,'p_exp1','expression_gt.py',11),
  ('exp -> loop','exp',1,'p_exp1','expression_gt.py',12),
  ('exp -> exp term','exp',2,'p_exp2','expression_gt.py',17),
  ('exp -> exp function','exp',2,'p_exp3','expression_gt.py',24),
  ('exp -> exp conditional','exp',2,'p_exp4','expression_gt.py',31),
  ('term -> fact','term',1,'p_term1','expression_gt.py',39),
  ('function -> : NAME ;','function',3,'p_functions1','expression_gt.py',45),
  ('function -> : NAME exp ;','function',4,'p_functions2','expression_gt.py',55),
  ('conditional -> IF ELSE THEN','conditional',3,'p_conditional1','expression_gt.py',66),
  ('conditional -> IF exp ELSE THEN','conditional',4,'p_conditional2','expression_gt.py',72),
  ('conditional -> IF ELSE exp THEN','conditional',4,'p_conditional3','expression_gt.py',78),
  ('conditional -> IF exp ELSE exp THEN','conditional',5,'p_conditional4','expression_gt.py',84),
  ('loop -> DO LOOP','loop',2,'p_loop1','expression_gt.py',90),
  ('loop -> DO exp LOOP','loop',3,'p_loop2','expression_gt.py',103),
  ('loop -> DO PLUSLOOP','loop',2,'p_plusloop1','expression_gt.py',117),
  ('loop -> DO exp PLUSLOOP','loop',3,'p_plusloop2','expression_gt.py',130),
  ('fact -> OPR','fact',1,'p_factOPR','expression_gt.py',147),
  ('fact -> INT','fact',1,'p_factInt','expression_gt.py',175),
  ('fact -> WORD','fact',1,'p_factWord','expression_gt.py',181),
  ('fact -> COMMENT','fact',1,'p_factComment','expression_gt.py',192),
  ('fact -> .','fact',1,'p_factDOT','expression_gt.py',196),
  ('fact -> DOTQUOTE','fact',1,'p_factDOTQUOTE','expression_gt.py',201),
  ('fact -> EMIT','fact',1,'p_factEMIT','expression_gt.py',205),
  ('fact -> CHAR','fact',1,'p_factCHAR','expression_gt.py',210),
  ('fact -> DUP','fact',1,'p_factDUP','expression_gt.py',215),
  ('fact -> CR','fact',1,'p_factCR','expression_gt.py',220),
  ('fact -> SPACE','fact',1,'p_factSPACE','expression_gt.py',224),
  ('fact -> SPACES','fact',1,'p_factSPACES','expression_gt.py',229),
  ('fact -> SWAP','fact',1,'p_factSWAP','expression_gt.py',235),
  ('fact -> KEY','fact',1,'p_factKey','expression_gt.py',240),
  ('fact -> DEPTH','fact',1,'p_factDEPTH','expression_gt.py',246),
  ('fact -> DROP','fact',1,'p_factDROP','expression_gt.py',252),
]
