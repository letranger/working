"""
created_at_utc  : 2022-10-28T07:11:01Z
created_at_w3c  : 2022-10-28T15:11:01+08:00
PAIA-Desktop    : 2.4.1
MLGame          : 10.0.2
game            : arkanoid
game_version    : 2.3.1
"""

import pickle
import os

_E7_90_83x = None
_E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83 = None
_E7_90_83y = None
_E7_90_83_E4_B8_8Ax = None
_E7_90_83_E4_B8_8Ay = None
x_E7_9B_B8_E6_B8_9B = None
y_E7_9B_B8_E6_B8_9B = None
AI_E6_A8_A1_E5_9E_8B = None
模型資料1 = None
_E8_A1_8C_E5_8B_95 = None


class MLPlay:
    def __init__(self, ai_name, *args, **kwargs):
        global _E7_90_83x, _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83, _E7_90_83y, _E7_90_83_E4_B8_8Ax, _E7_90_83_E4_B8_8Ay, x_E7_9B_B8_E6_B8_9B, y_E7_9B_B8_E6_B8_9B, AI_E6_A8_A1_E5_9E_8B, 模型資料1, _E8_A1_8C_E5_8B_95
        _E7_90_83x = 0
        _E7_90_83y = 0
        _E7_90_83_E4_B8_8Ax = 0
        _E7_90_83_E4_B8_8Ay = 0
        _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83 = False
        # 載入已經訓練好的AI模型
        with open(os.path.join(os.path.dirname(__file__), 'model' + '.pickle'), 'rb') as f:
            AI_E6_A8_A1_E5_9E_8B = pickle.load(f)
    def update(self, scene_info, keyboard=[], *args, **kwargs):
        global _E7_90_83x, _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83, _E7_90_83y, _E7_90_83_E4_B8_8Ax, _E7_90_83_E4_B8_8Ay, x_E7_9B_B8_E6_B8_9B, y_E7_9B_B8_E6_B8_9B, 模型, 模型資料1, _E8_A1_8C_E5_8B_95
        if scene_info['status'] == "GAME_PASS" or scene_info['status'] == "GAME_OVER":
            return "RESET"
        if not _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83:
            _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83 = True
            return "SERVE_TO_LEFT"
        else:
            _E7_90_83x = scene_info['ball'][0]
            _E7_90_83y = scene_info['ball'][1]
            x_E7_9B_B8_E6_B8_9B = _E7_90_83x - _E7_90_83_E4_B8_8Ax
            y_E7_9B_B8_E6_B8_9B = _E7_90_83y - _E7_90_83_E4_B8_8Ay
            _E7_90_83_E4_B8_8Ax = scene_info['ball'][0]
            _E7_90_83_E4_B8_8Ay = scene_info['ball'][0]
            # 利用AI模型預測移動方向，1代表向右移動，2代表向左移動
            # 這裡的特徵資料一定要跟遊戲收集的一樣喔!!
            模型資料1 = 模型.predict([[scene_info['ball'][0], scene_info['ball'][1], scene_info['platform'][0], x_E7_9B_B8_E6_B8_9B, y_E7_9B_B8_E6_B8_9B]]).tolist()
            _E8_A1_8C_E5_8B_95 = 模型資料1[0]
            if _E8_A1_8C_E5_8B_95 == 1:
                return "MOVE_RIGHT"
            elif _E8_A1_8C_E5_8B_95 == 2:
                return "MOVE_LEFT"
    def reset(self):
        global _E7_90_83x, _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83, _E7_90_83y, _E7_90_83_E4_B8_8Ax, _E7_90_83_E4_B8_8Ay, x_E7_9B_B8_E6_B8_9B, y_E7_9B_B8_E6_B8_9B, 模型, 模型資料1!, _E8_A1_8C_E5_8B_95
        _E5_B7_B2_E7_B6_93_E7_99_BC_E7_90_83 = False
