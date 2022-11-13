"""
created_at_utc  : 2022-10-28T07:10:06Z
created_at_w3c  : 2022-10-28T15:10:06+08:00
PAIA-Desktop    : 2.4.1-competition-tn
MLGame          : 10.0.2
game            : maze_car
game_version    : 3.3.1
"""

import pickle
import os
import math
from numbers import Number
import sys
import io

_E6_97_8B_E8_BD_89_E9_87_8F = None
_E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99 = None
_E7_A9_BA_E6_9B_A0_E5_9C_B0_E5_9C_96 = None
Model預測 = None
Model預測數據1 = None
Model1 = None
Model預測數據2 = None
Model2 = None

if sys.stdout == sys.__stdout__:
    sys.stdout = io.TextIOWrapper(open(sys.stdout.fileno(), 'wb', 0), encoding='utf-8', write_through=True)


class MLPlay:
    def __init__(self, ai_name, *args, **kwargs):
        global _E6_97_8B_E8_BD_89_E9_87_8F, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E7_A9_BA_E6_9B_A0_E5_9C_B0_E5_9C_96, Model預測, Model預測數據1, Model1, Model預測數據2, Model2
        _E6_97_8B_E8_BD_89_E9_87_8F = 0
        _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99 = []
        Model預測 = []
        with open(os.path.join(os.path.dirname(__file__), 'model' + '.pickle'), 'rb') as f:
            Model1 = pickle.load(f)
        with open(os.path.join(os.path.dirname(__file__), 'model2' + '.pickle'), 'rb') as f:
            Model2 = pickle.load(f)
    def update(self, scene_info, keyboard=[], *args, **kwargs):
        global _E6_97_8B_E8_BD_89_E9_87_8F, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E7_A9_BA_E6_9B_A0_E5_9C_B0_E5_9C_96, Model預測, Model預測數據1, Model1, Model預測數據2, Model2
        if scene_info['status'] != "GAME_ALIVE":
            return "RESET"
        else:
            if scene_info['L_T_sensor'] > 50 and scene_info['F_sensor'] > 50:
                _E7_A9_BA_E6_9B_A0_E5_9C_B0_E5_9C_96 = 123
            else:
                _E7_A9_BA_E6_9B_A0_E5_9C_B0_E5_9C_96 = math.floor(_E6_97_8B_E8_BD_89_E9_87_8F + 120)
            # 特徵必須跟收集資料的特徵一致
            _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99 = [[scene_info['L_sensor'], scene_info['L_T_sensor'], scene_info['F_sensor'], scene_info['R_T_sensor'], scene_info['R_sensor']]]
            if _E7_A9_BA_E6_9B_A0_E5_9C_B0_E5_9C_96 >= 1:
                # 預測轉速是清單,由AI模型產生
                Model預測 = Model2.predict(_E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99).tolist()
            else:
                # 預測轉速是清單,由AI模型產生
                Model預測 = Model1.predict(_E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99).tolist()
            Model預測數據1 = Model預測[0][0]
            Model預測數據2 = Model預測[0][1]
            if Model預測數據1 > Model預測數據2:
                _E6_97_8B_E8_BD_89_E9_87_8F = (_E6_97_8B_E8_BD_89_E9_87_8F if isinstance(_E6_97_8B_E8_BD_89_E9_87_8F, Number) else 0) + 1
            elif Model預測數據1 < Model預測數據2:
                _E6_97_8B_E8_BD_89_E9_87_8F = (_E6_97_8B_E8_BD_89_E9_87_8F if isinstance(_E6_97_8B_E8_BD_89_E9_87_8F, Number) else 0) + -2
            print(_E6_97_8B_E8_BD_89_E9_87_8F)
            print(_E7_A9_BA_E6_9B_A0_E5_9C_B0_E5_9C_96)
            return {'left_PWM': Model預測數據1, 'right_PWM': Model預測數據2}
    def reset(self):
        global _E6_97_8B_E8_BD_89_E9_87_8F, _E7_89_B9_E5_BE_B5_E8_B3_87_E6_96_99, _E7_A9_BA_E6_9B_A0_E5_9C_B0_E5_9C_96, Model預測, Model預測數據1, Model1, Model預測數據2, Model2
        pass
