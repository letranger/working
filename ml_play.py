#!/usr/bin/env python3

"""
The template of the main script of the machine learning process
"""
import pygame
from sklearn import neighbors
import os
import sys
import io
import pickle
import csv
import random
# Describe this function...
class MLPlay:
    def __init__(self, *args, **kwargs):
        """
        Constructor
        """
        self.model = None
        DIR = os.path.dirname(__file__)
        #load history data
        if os.path.exists(DIR+'/model.pickle'):
            with open(DIR+'/model.pickle', 'rb') as f:
                self.model = pickle.load(f)
            print('model loaded')

        self.ball_served = False
        self.record = [] #frame,ballX,ballY,dx,dy,platformX
        self.features = []
        self.targets = []
    def update(self, scene_info, keyboard=None, *args, **kwargs):
        """
        Generate the command according to the received `scene_info`.
        """
        # Make the caller to invoke `reset()` for the next round.
        if keyboard is None:keyboard = []
        if (scene_info["status"] == "GAME_OVER" or
                scene_info["status"] == "GAME_PASS"):
            return "RESET"
        if not self.ball_served:
            command = "SERVE_TO_LEFT"
            self.ball_served = True
        elif pygame.K_LEFT in keyboard:  command = "MOVE_LEFT"
        elif pygame.K_RIGHT in keyboard: command = "MOVE_RIGHT"
        else:command = "NONE"
        frame = scene_info['frame']
        x,y = scene_info['ball']
        platformX = scene_info['platform'][0]
        brickNum = len(scene_info['hard_bricks']) + len(scene_info['bricks'])
        dx,dy = 0,0
        if frame>0:
            lastFrame,lastX,lastY,last_dx,last_dy = self.record[-1][0:5]
            dx,dy = last_dx,last_dy
            if frame - lastFrame==1:
                dx,dy = x-lastX,y-lastY
                #if dx!=last_dx or dy!=last_dy:print('dx,dy=',dx,dy)
        self.record.append([frame,x,y,dx,dy])

        if self.model!=None and dy>0 and y<395+7:#platform length = 40
            #model.fit(self.features,self.targets)
            targetX = self.model.predict([[x,y,dx,dy]])[0]
            if platformX+20 > targetX:  command = "MOVE_LEFT"
            elif platformX+20 < targetX:command = "MOVE_RIGHT"
        commands = ['MOVE_LEFT','MOVE_RIGHT','NONE']
        if y>=(395-7):
            command = commands[random.randint(0,2)]
            print(frame,'hit')

        return command

    def reset(self):
        """
        Reset the status
        """
        DIR = os.path.dirname(__file__)
        #load history data
        if os.path.exists(DIR+'/targets.pickle'):
            with open(DIR+'/targets.pickle', 'rb') as f:
                self.targets = pickle.load(f)
            with open(DIR+'/features.pickle', 'rb') as f:
                self.features = pickle.load(f)
        #save record.csv
        '''
        frame   x       y       dx  dy
        150	178	395	0	0
        150	178	395	0	0
        151	171	388	-7	-7
        152	164	381	-7	-7
        '''
        with open(DIR+ '/record' +'.csv', 'w', newline='') as f:
            csv.writer(f, delimiter=',').writerows(self.record)
        #collect training data
        self.record.reverse()
        ii = None
        for i in range(len(self.record)):
            y=self.record[i][2]
            if y>=(395-7) and y<=(395+7):ii = i;break

        targetX = self.record[ii][1] #x
        for frame,x,y,dx,dy in self.record[ii:-1]:
            if dy > 0:
                self.features.append([x,y,dx,dy])
                self.targets.append([targetX])
            else:break

        #model training
        self.model = neighbors.KNeighborsRegressor(5, weights='uniform')

        self.model.fit(self.features,self.targets)
        #save features <==> targets
        with open(DIR+ '/features' + '.pickle', 'wb') as f:
            pickle.dump(self.features, f)
        with open(DIR+ '/targets' + '.pickle', 'wb') as f:
            pickle.dump(self.targets, f)
        with open(DIR+ '/model' + '.pickle', 'wb') as f:
            pickle.dump(self.model, f)
        #reset parameter
        self.ball_served = False
        self.record = []
