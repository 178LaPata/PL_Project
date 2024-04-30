
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'INT WORDfds : factfds : fds factfact : INT'
    
_lr_action_items = {'INT':([0,1,2,3,4,],[3,3,-1,-3,-2,]),'$end':([1,2,3,4,],[0,-1,-3,-2,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'fds':([0,],[1,]),'fact':([0,1,],[2,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> fds","S'",1,None,None,None),
  ('fds -> fact','fds',1,'p_mano','expression_gt.py',7),
  ('fds -> fds fact','fds',2,'p_fds1','expression_gt.py',12),
  ('fact -> INT','fact',1,'p_factInt','expression_gt.py',20),
]
