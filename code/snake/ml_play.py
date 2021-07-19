"""
The template of the script for the machine learning process in game pingpong
"""
"""
ml_play 程式只能交一份，且檔名為 ml_play.py
"""
import os
import pickle
import numpy as np

class MLPlay:
    def __init__(self):

        self.last_place=(40,40)
        with open(os.path.join(os.path.dirname(__file__), 'model.pickle'), 'rb') as f:
            self.model = pickle.load(f)



    def update(self, scene_info):

        if scene_info["status"] == "GAME_OVER":
            return "RESET"
            
        
        else:

            snake_head = scene_info["snake_head"]
            snake_speed_x = snake_head[0]-self.last_place[0]
            snake_speed_y = snake_head[1]-self.last_place[1]
            
            x = np.array([snake_head[0], snake_head[1],snake_speed_x,snake_speed_y]).reshape((1, -1))
            y = self.model.predict(x)

            if y==0:
                command = "RIGHT"
            elif y==1:
                command = "LEFT"
            elif y==2:
                command = "UP"
            elif y==3:
                command = "DOWN"
            elif y==4:
                command = "NONE"
            
            self.last_place = snake_head
            return command

        

    def reset(self):
        """
        Reset the status
        """
        self.last_place=(40,40)
