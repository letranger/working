#!/usr/bin/env python3

"""
created_at_utc  : 2022-10-28T06:36:01Z
created_at_w3c  : 2022-10-28T14:36:01+08:00
PAIA-Desktop    : 2.4.1-competition-tn
MLGame          : 10.0.2
game            : maze_car
game_version    : 3.3.1
"""

感應器1 = None
_E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F = None
感應器2 = None
_E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F = None
感應器3 = None

# 後退
def 後退():
    global 感應器1, _E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F, 感應器2, _E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F, 感應器3
    _E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F = -10
    _E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F = -150

# 前進
def 前進():
    global 感應器1, _E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F, 感應器2, _E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F, 感應器3
    _E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F = 255
    _E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F = 255

# 左轉
def 左轉():
    global 感應器1, _E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F, 感應器2, _E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F, 感應器3
    _E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F = 0
    _E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F = 255

# 右轉
def 右轉():
    global 感應器1, _E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F, 感應器2, _E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F, 感應器3
    _E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F = 255
    _E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F = 0


class MLPlay:
    def __init__(self, ai_name, *args, **kwargs):
        global 感應器1, _E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F, 感應器2, _E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F, 感應器3
        感應器1 = 0
        感應器2 = 0
        感應器3 = 0
        _E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F = 0
        _E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F = 0
    def update(self, scene_info, keyboard=[], *args, **kwargs):
        global 感應器1, _E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F, 感應器2, _E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F, 感應器3
        感應器1 = scene_info['L_T_sensor']
        感應器2 = scene_info['F_sensor']
        感應器3 = scene_info['R_T_sensor']
        # 請自行設計自走策略或新增其它的函式喔!
        if 感應器2 <= 5:
            後退()
        elif 感應器1 >= 25:
            左轉()
        elif 感應器3 >= 50:
            右轉()
        else:
            前進()
        return {'left_PWM': _E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F, 'right_PWM': _E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F}
    def reset(self):
        global 感應器1, _E5_B7_A6_E8_BC_AA_E8_BD_89_E9_80_9F, 感應器2, _E5_8F_B3_E8_BC_AA_E8_BD_89_E9_80_9F, 感應器3
        pass
