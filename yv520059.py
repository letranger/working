#!/usr/bin/env python3

"""
created_at_utc  : 2022-10-28T07:18:45Z
created_at_w3c  : 2022-10-28T15:18:45+08:00
PAIA-Desktop    : 2.4.1-competition-tn
MLGame          : 10.0.2
game            : maze_car
game_version    : 3.3.1
"""

import pickle
import os
import math
from numbers import Number

_E7_A9_BA = None
_E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99 = None
_E8_BD_89 = None
_E9_A0_90_E6_B8_AC_E8_BD_89_E9_80_9F = None
ai_1 = None
_E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F = None
ai_2 = None
_E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F = None

# 描述此函式...
def _E9_87_8D_E8_A3_BD_5C():
    global _E7_A9_BA, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E8_BD_89, _E9_A0_90_E6_B8_AC_E8_BD_89_E9_80_9F, ai_1, _E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F, ai_2, _E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F
    _E7_A9_BA = 0
    _E8_BD_89 = 0


class MLPlay:
    def __init__(self, ai_name, *args, **kwargs):
        global _E7_A9_BA, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E8_BD_89, _E9_A0_90_E6_B8_AC_E8_BD_89_E9_80_9F, ai_1, _E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F, ai_2, _E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F
        _E9_87_8D_E8_A3_BD_5C()
        _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99 = []
        _E9_A0_90_E6_B8_AC_E8_BD_89_E9_80_9F = []
        with open(os.path.join(os.path.dirname(__file__), 'model' + '.pickle'), 'rb') as f:
            ai_1 = pickle.load(f)
        with open(os.path.join(os.path.dirname(__file__), 'model2' + '.pickle'), 'rb') as f:
            ai_2 = pickle.load(f)
    def update(self, scene_info, keyboard=[], *args, **kwargs):
        global _E7_A9_BA, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E8_BD_89, _E9_A0_90_E6_B8_AC_E8_BD_89_E9_80_9F, ai_1, _E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F, ai_2, _E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F
        if scene_info['status'] != "GAME_ALIVE":
            return "RESET"
        else:
            if scene_info['L_T_sensor'] > 50 and scene_info['F_sensor'] > 50:
                _E7_A9_BA = 1
            else:
                _E7_A9_BA = math.floor(_E8_BD_89 / 100)
            # 特徵必須跟收集資料的特徵一致
            _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99 = [[scene_info['L_sensor'], scene_info['L_T_sensor'], scene_info['F_sensor'], scene_info['R_T_sensor'], scene_info['R_sensor']]]
            if _E7_A9_BA >= 1:
                # 預測轉速是清單,由AI模型產生
                _E9_A0_90_E6_B8_AC_E8_BD_89_E9_80_9F = ai_2.predict(_E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99).tolist()
            else:
                # 預測轉速是清單,由AI模型產生
                _E9_A0_90_E6_B8_AC_E8_BD_89_E9_80_9F = ai_1.predict(_E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99).tolist()
            _E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F = _E9_A0_90_E6_B8_AC_E8_BD_89_E9_80_9F[0][0]
            _E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F = _E9_A0_90_E6_B8_AC_E8_BD_89_E9_80_9F[0][1]
            if _E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F > _E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F:
                _E8_BD_89 = (_E8_BD_89 if isinstance(_E8_BD_89, Number) else 0) + 1
            elif _E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F < _E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F:
                _E8_BD_89 = (_E8_BD_89 if isinstance(_E8_BD_89, Number) else 0) + -1.5
            return {'left_PWM': _E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F, 'right_PWM': _E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F}
    def reset(self):
        global _E7_A9_BA, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E8_BD_89, _E9_A0_90_E6_B8_AC_E8_BD_89_E9_80_9F, ai_1, _E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F, ai_2, _E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F
        _E9_87_8D_E8_A3_BD_5C()
