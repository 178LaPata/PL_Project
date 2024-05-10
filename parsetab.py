
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "CHAR COMMENT CR DEPTH DO DOTQUOTE DROP DUP ELSE EMIT IF INT KEY LOOP NAME OPR PLUSLOOP SPACE SPACES SWAP THEN WORDexp : term\n           | function\n           | conditional\n           | loop\n    exp : exp termexp : exp functionexp : exp conditionalexp : exp loopterm : factfunction : ':' NAME ';'function : ':' NAME exp ';'conditional : IF ELSE THENconditional : IF exp ELSE THENconditional : IF ELSE exp THENconditional : IF exp ELSE exp THENloop : DO LOOPloop : DO exp LOOPloop : DO PLUSLOOPloop : DO exp PLUSLOOPfact : OPRfact : INTfact : WORDfact : COMMENTfact : '.'fact : DOTQUOTEfact : EMITfact : CHARfact : DUPfact : CRfact : SPACEfact : SPACESfact : SWAPfact : KEYfact : DEPTHfact : DROP"
    
_lr_action_items = {':':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[7,7,-1,-2,-3,-4,-9,7,7,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,7,7,7,-16,7,-18,-10,7,-12,7,7,-17,-19,-11,-14,7,-13,-15,]),'IF':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[8,8,-1,-2,-3,-4,-9,8,8,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,8,8,8,-16,8,-18,-10,8,-12,8,8,-17,-19,-11,-14,8,-13,-15,]),'DO':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[9,9,-1,-2,-3,-4,-9,9,9,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,9,9,9,-16,9,-18,-10,9,-12,9,9,-17,-19,-11,-14,9,-13,-15,]),'OPR':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[10,10,-1,-2,-3,-4,-9,10,10,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,10,10,10,-16,10,-18,-10,10,-12,10,10,-17,-19,-11,-14,10,-13,-15,]),'INT':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[11,11,-1,-2,-3,-4,-9,11,11,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,11,11,11,-16,11,-18,-10,11,-12,11,11,-17,-19,-11,-14,11,-13,-15,]),'WORD':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[12,12,-1,-2,-3,-4,-9,12,12,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,12,12,12,-16,12,-18,-10,12,-12,12,12,-17,-19,-11,-14,12,-13,-15,]),'COMMENT':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[13,13,-1,-2,-3,-4,-9,13,13,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,13,13,13,-16,13,-18,-10,13,-12,13,13,-17,-19,-11,-14,13,-13,-15,]),'.':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[14,14,-1,-2,-3,-4,-9,14,14,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,14,14,14,-16,14,-18,-10,14,-12,14,14,-17,-19,-11,-14,14,-13,-15,]),'DOTQUOTE':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[15,15,-1,-2,-3,-4,-9,15,15,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,15,15,15,-16,15,-18,-10,15,-12,15,15,-17,-19,-11,-14,15,-13,-15,]),'EMIT':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[16,16,-1,-2,-3,-4,-9,16,16,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,16,16,16,-16,16,-18,-10,16,-12,16,16,-17,-19,-11,-14,16,-13,-15,]),'CHAR':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[17,17,-1,-2,-3,-4,-9,17,17,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,17,17,17,-16,17,-18,-10,17,-12,17,17,-17,-19,-11,-14,17,-13,-15,]),'DUP':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[18,18,-1,-2,-3,-4,-9,18,18,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,18,18,18,-16,18,-18,-10,18,-12,18,18,-17,-19,-11,-14,18,-13,-15,]),'CR':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[19,19,-1,-2,-3,-4,-9,19,19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,19,19,19,-16,19,-18,-10,19,-12,19,19,-17,-19,-11,-14,19,-13,-15,]),'SPACE':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[20,20,-1,-2,-3,-4,-9,20,20,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,20,20,20,-16,20,-18,-10,20,-12,20,20,-17,-19,-11,-14,20,-13,-15,]),'SPACES':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[21,21,-1,-2,-3,-4,-9,21,21,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,21,21,21,-16,21,-18,-10,21,-12,21,21,-17,-19,-11,-14,21,-13,-15,]),'SWAP':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[22,22,-1,-2,-3,-4,-9,22,22,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,22,22,22,-16,22,-18,-10,22,-12,22,22,-17,-19,-11,-14,22,-13,-15,]),'KEY':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[23,23,-1,-2,-3,-4,-9,23,23,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,23,23,23,-16,23,-18,-10,23,-12,23,23,-17,-19,-11,-14,23,-13,-15,]),'DEPTH':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[24,24,-1,-2,-3,-4,-9,24,24,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,24,24,24,-16,24,-18,-10,24,-12,24,24,-17,-19,-11,-14,24,-13,-15,]),'DROP':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[25,25,-1,-2,-3,-4,-9,25,25,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,25,25,25,-16,25,-18,-10,25,-12,25,25,-17,-19,-11,-14,25,-13,-15,]),'$end':([1,2,3,4,5,6,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,33,35,36,38,41,42,43,44,46,47,],[0,-1,-2,-3,-4,-9,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,-16,-18,-10,-12,-17,-19,-11,-14,-13,-15,]),'ELSE':([2,3,4,5,6,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,32,33,35,36,38,41,42,43,44,46,47,],[-1,-2,-3,-4,-9,31,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,40,-16,-18,-10,-12,-17,-19,-11,-14,-13,-15,]),'LOOP':([2,3,4,5,6,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,33,34,35,36,38,41,42,43,44,46,47,],[-1,-2,-3,-4,-9,33,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,-16,41,-18,-10,-12,-17,-19,-11,-14,-13,-15,]),'PLUSLOOP':([2,3,4,5,6,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,33,34,35,36,38,41,42,43,44,46,47,],[-1,-2,-3,-4,-9,35,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,-16,42,-18,-10,-12,-17,-19,-11,-14,-13,-15,]),';':([2,3,4,5,6,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,33,35,36,37,38,41,42,43,44,46,47,],[-1,-2,-3,-4,-9,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,36,-16,-18,-10,43,-12,-17,-19,-11,-14,-13,-15,]),'THEN':([2,3,4,5,6,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,33,35,36,38,39,40,41,42,43,44,45,46,47,],[-1,-2,-3,-4,-9,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-5,-6,-7,-8,38,-16,-18,-10,-12,44,46,-17,-19,-11,-14,47,-13,-15,]),'NAME':([7,],[30,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'exp':([0,8,9,30,31,40,],[1,32,34,37,39,45,]),'term':([0,1,8,9,30,31,32,34,37,39,40,45,],[2,26,2,2,2,2,26,26,26,26,2,26,]),'function':([0,1,8,9,30,31,32,34,37,39,40,45,],[3,27,3,3,3,3,27,27,27,27,3,27,]),'conditional':([0,1,8,9,30,31,32,34,37,39,40,45,],[4,28,4,4,4,4,28,28,28,28,4,28,]),'loop':([0,1,8,9,30,31,32,34,37,39,40,45,],[5,29,5,5,5,5,29,29,29,29,5,29,]),'fact':([0,1,8,9,30,31,32,34,37,39,40,45,],[6,6,6,6,6,6,6,6,6,6,6,6,]),}

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
  ('exp -> exp loop','exp',2,'p_exp5','expression_gt.py',38),
  ('term -> fact','term',1,'p_term1','expression_gt.py',46),
  ('function -> : NAME ;','function',3,'p_functions1','expression_gt.py',52),
  ('function -> : NAME exp ;','function',4,'p_functions2','expression_gt.py',62),
  ('conditional -> IF ELSE THEN','conditional',3,'p_conditional1','expression_gt.py',73),
  ('conditional -> IF exp ELSE THEN','conditional',4,'p_conditional2','expression_gt.py',79),
  ('conditional -> IF ELSE exp THEN','conditional',4,'p_conditional3','expression_gt.py',85),
  ('conditional -> IF exp ELSE exp THEN','conditional',5,'p_conditional4','expression_gt.py',91),
  ('loop -> DO LOOP','loop',2,'p_loop1','expression_gt.py',97),
  ('loop -> DO exp LOOP','loop',3,'p_loop2','expression_gt.py',114),
  ('loop -> DO PLUSLOOP','loop',2,'p_plusloop1','expression_gt.py',131),
  ('loop -> DO exp PLUSLOOP','loop',3,'p_plusloop2','expression_gt.py',147),
  ('fact -> OPR','fact',1,'p_factOPR','expression_gt.py',166),
  ('fact -> INT','fact',1,'p_factInt','expression_gt.py',194),
  ('fact -> WORD','fact',1,'p_factWord','expression_gt.py',200),
  ('fact -> COMMENT','fact',1,'p_factComment','expression_gt.py',211),
  ('fact -> .','fact',1,'p_factDOT','expression_gt.py',215),
  ('fact -> DOTQUOTE','fact',1,'p_factDOTQUOTE','expression_gt.py',220),
  ('fact -> EMIT','fact',1,'p_factEMIT','expression_gt.py',224),
  ('fact -> CHAR','fact',1,'p_factCHAR','expression_gt.py',229),
  ('fact -> DUP','fact',1,'p_factDUP','expression_gt.py',234),
  ('fact -> CR','fact',1,'p_factCR','expression_gt.py',239),
  ('fact -> SPACE','fact',1,'p_factSPACE','expression_gt.py',243),
  ('fact -> SPACES','fact',1,'p_factSPACES','expression_gt.py',248),
  ('fact -> SWAP','fact',1,'p_factSWAP','expression_gt.py',254),
  ('fact -> KEY','fact',1,'p_factKey','expression_gt.py',259),
  ('fact -> DEPTH','fact',1,'p_factDEPTH','expression_gt.py',265),
  ('fact -> DROP','fact',1,'p_factDROP','expression_gt.py',271),
]
