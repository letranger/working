"""
created_at_utc  : 2022-10-28T06:43:42Z
created_at_w3c  : 2022-10-28T14:43:42+08:00
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
模型資料1 = None
模型 = None
模型資枓2 = None


class MLPlay:
    def __init__(self, ai_name, *args, **kwargs):
        global _E5_89_8D_E7_90_83x_E5_BA_A7_E6_A8_99, _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE, _E5_89_8D_E7_90_83y_E5_BA_A7_E6_A8_99, _E7_99_BC_E7_90_83_E6_96_B9_E5_90_91, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91, 模型資料1, 模型, 模型資枓2
        _E5_89_8D_E7_90_83x_E5_BA_A7_E6_A8_99 = 90
        _E5_89_8D_E7_90_83y_E5_BA_A7_E6_A8_99 = 400
        _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE = random.randint(0 + 20, 200 - 20)
        _E7_99_BC_E7_90_83_E6_96_B9_E5_90_91 = random.randint(1, 100) % 2
        # 載入已經訓練好的AI模型
        with open(os.path.join(os.path.dirname(__file__), 'model' + '.pickle'), 'rb') as f:
            模型 = pickle.load(f)
    def update(self, scene_info, keyboard=[], *args, **kwargs):
        global _E5_89_8D_E7_90_83x_E5_BA_A7_E6_A8_99, _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE, _E5_89_8D_E7_90_83y_E5_BA_A7_E6_A8_99, _E7_99_BC_E7_90_83_E6_96_B9_E5_90_91, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91, 模型資料1, 模型, 模型資枓2
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
                模型資料1 = 模型.predict([[scene_info['ball'][0], scene_info['ball'][1], _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91, scene_info['platform'][0]]]).tolist()
                模型資枓2 = 模型資料1[0]
                if 模型資枓2 == 1:
                    return "MOVE_LEFT"
                elif 模型資枓2 == 2:
                    return "MOVE_RIGHT"
                elif 模型資枓2 == 0:
                    return "NONE"
    def reset(self):
        global _E5_89_8D_E7_90_83x_E5_BA_A7_E6_A8_99, _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE, _E5_89_8D_E7_90_83y_E5_BA_A7_E6_A8_99, _E7_99_BC_E7_90_83_E6_96_B9_E5_90_91, _E7_90_83_E7_9A_84x_E6_96_B9_E5_90_91, 模型資料1, 模型, 模型資枓2
        _E7_99_BC_E7_90_83_E4_BD_8D_E7_BD_AE = random.randint(0 + 20, 200 - 20)
        _E7_99_BC_E7_90_83_E6_96_B9_E5_90_91 = random.randint(1, 100) % 2
