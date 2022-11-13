import random
from numbers import Number
import sys
import io
import pickle
import os

_E9_81_8E_E9_97_9C_E7_B4_AF_E8_A8_88 = None
_E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE = None
_E5_89_8D_E7_90_83x_E5_BA_A7_E6_A8_99 = None
_E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99 = None
_E7_99_BC_E7_90_83_E6_96_B9_E5_90_91 = None
pickledump1 = None
_E5_89_8D_E7_90_83y_E5_BA_A7_E6_A8_99 = None
_E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99 = None
_E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91 = None
_E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99 = None
_E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91 = None
pickledump2 = None
_E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8 = None
_E9_A0_90_E6_B8_AC_E8_90_BD_E9_BB_9E = None

if sys.stdout == sys.__stdout__:
    sys.stdout = io.TextIOWrapper(open(sys.stdout.fileno(), 'wb', 0), encoding='utf-8', write_through=True)

# 收集資料
def 蒐集資料func():
    global _E9_81_8E_E9_97_9C_E7_B4_AF_E8_A8_88, _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE, _E5_89_8D_E7_90_83x_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99, _E7_99_BC_E7_90_83_E6_96_B9_E5_90_91, pickledump1, _E5_89_8D_E7_90_83y_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91, _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91, pickledump2, _E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8, _E9_A0_90_E6_B8_AC_E8_90_BD_E9_BB_9E
    # 特徵可以自行增加!
    pickledump1.append([_E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91, _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99])
    pickledump2.append(_E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91)

# 儲存資料
def 儲存pickle():
    global _E9_81_8E_E9_97_9C_E7_B4_AF_E8_A8_88, _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE, _E5_89_8D_E7_90_83x_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99, _E7_99_BC_E7_90_83_E6_96_B9_E5_90_91, pickledump1, _E5_89_8D_E7_90_83y_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91, _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91, pickledump2, _E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8, _E9_A0_90_E6_B8_AC_E8_90_BD_E9_BB_9E
    with open(os.path.join(os.path.dirname(__file__), 'feature' + str(_E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8) + '.pickle'), 'wb') as f:
        pickle.dump(pickledump1, f)
    with open(os.path.join(os.path.dirname(__file__), 'target' + str(_E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8) + '.pickle'), 'wb') as f:
        pickle.dump(pickledump2, f)

# 平台移動判斷,請自行修改判斷方法~
def 判斷平台移動func():
    global _E9_81_8E_E9_97_9C_E7_B4_AF_E8_A8_88, _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE, _E5_89_8D_E7_90_83x_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99, _E7_99_BC_E7_90_83_E6_96_B9_E5_90_91, pickledump1, _E5_89_8D_E7_90_83y_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91, _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91, pickledump2, _E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8, _E9_A0_90_E6_B8_AC_E8_90_BD_E9_BB_9E
    _E9_A0_90_E6_B8_AC_E7_90_83_E7_9A_84_E8_90_BD_E9_BB_9E()
    if _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99 > _E9_A0_90_E6_B8_AC_E8_90_BD_E9_BB_9E:
        _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91 = 1
    elif _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99 < _E9_A0_90_E6_B8_AC_E8_90_BD_E9_BB_9E:
        _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91 = 2
    else:
        _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91 = 0

# 預測球的落點，採用等腰三角形算法，可自行修改其他演算法
def _E9_A0_90_E6_B8_AC_E7_90_83_E7_9A_84_E8_90_BD_E9_BB_9E():
    global _E9_81_8E_E9_97_9C_E7_B4_AF_E8_A8_88, _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE, _E5_89_8D_E7_90_83x_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99, _E7_99_BC_E7_90_83_E6_96_B9_E5_90_91, pickledump1, _E5_89_8D_E7_90_83y_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91, _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91, pickledump2, _E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8, _E9_A0_90_E6_B8_AC_E8_90_BD_E9_BB_9E
    if _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91 < 0:
        if _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99 - (400 - _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99) >= 0:
            _E9_A0_90_E6_B8_AC_E8_90_BD_E9_BB_9E = _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99 - (400 - _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99)
        else:
            _E9_A0_90_E6_B8_AC_E8_90_BD_E9_BB_9E = (400 - _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99) - _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99
    elif _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91 > 0:
        if _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99 + (400 - _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99) <= 200:
            _E9_A0_90_E6_B8_AC_E8_90_BD_E9_BB_9E = _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99 + (400 - _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99)
        else:
            _E9_A0_90_E6_B8_AC_E8_90_BD_E9_BB_9E = _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99 - _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99


class MLPlay:
    def __init__(self, ai_name, *args, **kwargs):
        global _E9_81_8E_E9_97_9C_E7_B4_AF_E8_A8_88, _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE, _E5_89_8D_E7_90_83x_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99, _E7_99_BC_E7_90_83_E6_96_B9_E5_90_91, pickledump1, _E5_89_8D_E7_90_83y_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91, _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91, pickledump2, _E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8, _E9_A0_90_E6_B8_AC_E8_90_BD_E9_BB_9E
        _E9_81_8E_E9_97_9C_E7_B4_AF_E8_A8_88 = 0
        _E5_89_8D_E7_90_83x_E5_BA_A7_E6_A8_99 = 93
        _E5_89_8D_E7_90_83y_E5_BA_A7_E6_A8_99 = 395
        pickledump1 = []
        pickledump2 = []
        # 隨機位置發球
        _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE = random.randint(0 + 20, 200 - 20)
        # 隨機方向發球
        _E7_99_BC_E7_90_83_E6_96_B9_E5_90_91 = random.randint(1, 100) % 2
        _E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8 = 1
    def update(self, scene_info, keyboard=[], *args, **kwargs):
        global _E9_81_8E_E9_97_9C_E7_B4_AF_E8_A8_88, _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE, _E5_89_8D_E7_90_83x_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99, _E7_99_BC_E7_90_83_E6_96_B9_E5_90_91, pickledump1, _E5_89_8D_E7_90_83y_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91, _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91, pickledump2, _E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8, _E9_A0_90_E6_B8_AC_E8_90_BD_E9_BB_9E
        if scene_info['status'] != "GAME_ALIVE":
            # 只收集過關得資料
            if scene_info['status'] == "GAME_PASS":
                儲存pickle()
                _E9_81_8E_E9_97_9C_E7_B4_AF_E8_A8_88 = (_E9_81_8E_E9_97_9C_E7_B4_AF_E8_A8_88 if isinstance(_E9_81_8E_E9_97_9C_E7_B4_AF_E8_A8_88, Number) else 0) + 1
            return "RESET"
        else:
            _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99 = scene_info['ball'][0]
            _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99 = scene_info['ball'][1]
            _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99 = scene_info['platform'][0]
            # 是否已發球
            if not scene_info['ball_served']:
                while not (_E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE - 30 <= _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99 and _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99 <= _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE - 10):
                    if _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE <= _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99 + 40 / 2:
                        return "MOVE_LEFT"
                    else:
                        return "MOVE_RIGHT"
                if _E7_99_BC_E7_90_83_E6_96_B9_E5_90_91 == 1:
                    return "SERVE_TO_LEFT"
                else:
                    return "SERVE_TO_RIGHT"
            else:
                _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91_E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91 = _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99 - _E5_89_8D_E7_90_83x_E5_BA_A7_E6_A8_99
                _E5_89_8D_E7_90_83x_E5_BA_A7_E6_A8_99 = _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99
                判斷平台移動func()
                蒐集資料func()
                if _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91 < 2:
                    return "MOVE_LEFT"
                elif _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91 > 1:
                    return "MOVE_RIGHT"
                else:
                    return "NONE"
                if _E9_A0_90_E6_B8_AC_E8_90_BD_E9_BB_9E > _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99:
                    return "MOVE_LEFT"
                if _E9_A0_90_E6_B8_AC_E8_90_BD_E9_BB_9E < _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99:
                    return "MOVE_RIGHT"
    def reset(self):
        global _E9_81_8E_E9_97_9C_E7_B4_AF_E8_A8_88, _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE, _E5_89_8D_E7_90_83x_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84x_E5_BA_A7_E6_A8_99, _E7_99_BC_E7_90_83_E6_96_B9_E5_90_91, pickledump1, _E5_89_8D_E7_90_83y_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84y_E5_BA_A7_E6_A8_99, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91, _E5_B9_B3_E5_8F_B0_E7_9A_84x_E5_BA_A7_E6_A8_99, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91, pickledump2, _E8_B3_87_E6_96_99_E8_A8_88_E6_95_B8, _E9_A0_90_E6_B8_AC_E8_90_BD_E9_BB_9E
        # 隨機位置發球
        _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE = random.randint(0 + 20, 200 - 20)
        # 隨機方向發球
        _E7_99_BC_E7_90_83_E6_96_B9_E5_90_91 = random.randint(1, 100) % 2
        print('遊戲過關：' + str(_E9_81_8E_E9_97_9C_E7_B4_AF_E8_A8_88))
