"""
created_at_utc  : 2022-10-28T07:23:03Z
created_at_w3c  : 2022-10-28T15:23:03+08:00
PAIA-Desktop    : 2.4.1-competition-tn
MLGame          : 10.0.2
game            : arkanoid
game_version    : 2.3.1
"""

import random
import pickle
import os

_E5_89_8D_E7_90_83x_E5_BA_A7_E6_A8_99 = None
_E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE = None
_E5_89_8D_E7_90_83y_E5_BA_A7_E6_A8_99 = None
_E7_99_BC_E7_90_83_E6_96_B9_E5_90_91 = None
_E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91 = None
_E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C = None
AI_E6_A8_A1_E5_9E_8B = None
_E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91 = None


class MLPlay:
    def __init__(self, ai_name, *args, **kwargs):
        global _E5_89_8D_E7_90_83x_E5_BA_A7_E6_A8_99, _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE, _E5_89_8D_E7_90_83y_E5_BA_A7_E6_A8_99, _E7_99_BC_E7_90_83_E6_96_B9_E5_90_91, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91, _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C, AI_E6_A8_A1_E5_9E_8B, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91
        _E5_89_8D_E7_90_83x_E5_BA_A7_E6_A8_99 = 90
        _E5_89_8D_E7_90_83y_E5_BA_A7_E6_A8_99 = 400
        _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE = random.randint(0 + 20, 200 - 20)
        _E7_99_BC_E7_90_83_E6_96_B9_E5_90_91 = random.randint(1, 100) % 2
        # 載入已經訓練好的AI模型
        with open(os.path.join(os.path.dirname(__file__), 'model' + '.pickle'), 'rb') as f:
            AI_E6_A8_A1_E5_9E_8B = pickle.load(f)
    def update(self, scene_info, keyboard=[], *args, **kwargs):
        global _E5_89_8D_E7_90_83x_E5_BA_A7_E6_A8_99, _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE, _E5_89_8D_E7_90_83y_E5_BA_A7_E6_A8_99, _E7_99_BC_E7_90_83_E6_96_B9_E5_90_91, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91, _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C, AI_E6_A8_A1_E5_9E_8B, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91
        if scene_info['status'] != "GAME_ALIVE":
            return "RESET"
        else:
            if not scene_info['ball_served']:
                while not (_E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE - 30 <= scene_info['platform'][0] and scene_info['platform'][0] <= _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE - 10):
                    if _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE <= scene_info['platform'][0] + 40 / 2:
                        return "MOVE_LEFT"
                    else:
                        return "MOVE_RIGHT"
                if _E7_99_BC_E7_90_83_E6_96_B9_E5_90_91 == 1:
                    return "SERVE_TO_LEFT"
                else:
                    return "SERVE_TO_RIGHT"
            else:
                _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91 = scene_info['ball'][0] - _E5_89_8D_E7_90_83x_E5_BA_A7_E6_A8_99
                _E5_89_8D_E7_90_83x_E5_BA_A7_E6_A8_99 = scene_info['ball'][0]
                # 利用AI模型預測移動方向，1代表向右移動，2代表向左移動
                # 這裡的特徵資料一定要跟遊戲收集的一樣喔!!
                _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C = AI_E6_A8_A1_E5_9E_8B.predict([[scene_info['ball'][0], scene_info['ball'][1], _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91, scene_info['platform'][0]]]).tolist()
                _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91 = _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C[0]
                if _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91 == 1:
                    return "MOVE_LEFT"
                elif _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91 == 2:
                    return "MOVE_RIGHT"
                elif _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91 == 0:
                    return "NONE"
    def reset(self):
        global _E5_89_8D_E7_90_83x_E5_BA_A7_E6_A8_99, _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE, _E5_89_8D_E7_90_83y_E5_BA_A7_E6_A8_99, _E7_99_BC_E7_90_83_E6_96_B9_E5_90_91, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91, _E9_A0_90_E6_B8_AC_E7_B5_90_E6_9E_9C, AI_E6_A8_A1_E5_9E_8B, _E7_A7_BB_E5_8B_95_E6_96_B9_E5_90_91
        _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE = random.randint(0 + 20, 200 - 20)
        _E7_99_BC_E7_90_83_E6_96_B9_E5_90_91 = random.randint(1, 100) % 2
