"""
The template of the main script of the machine learning process
"""
import os
import pickle
import random

import numpy as np

# python MLGame.py -i model_DJ.py arkanoid NORMAL 2
class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.ball_served = False
        self.previous_ball = (0, 0)
        # Need scikit-learn==0.22.2 
        # with open(os.path.join(os.path.dirname(__file__), 'save', 'model.pickle'), 'rb') as f:
        #     self.model = pickle.load(f)
        #with open(os.path.join(os.path.dirname(__file__), 'my_model.pickle'), 'rb') as f:
        #   self.model = pickle.load(f)

    def update(self, scene_info):
        """
        Generate the command according to the received `scene_info`.
        """
        # Make the caller to invoke `reset()` for the next round.
        if (scene_info["status"] == "GAME_OVER" or
                scene_info["status"] == "GAME_PASS"):
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            rnd = random.randrange(2)
            
            if rnd == 1:
                command = "SERVE_TO_LEFT"
            else:
                command = "SERVE_TO_RIGHT"
        else:
            Ball_x = scene_info["ball"][0]
            Ball_y = scene_info["ball"][1]
            Ball_speed_x = scene_info["ball"][0] - self.previous_ball[0]
            Ball_speed_y = scene_info["ball"][1] - self.previous_ball[1]
            Platform = scene_info["platform"][0]
            if Ball_speed_x > 0:
                if Ball_speed_y > 0:
                    Direction = 0
                else:
                    Direction = 1
            else:
                if Ball_speed_y > 0:
                    Direction = 2
                else:
                    Direction = 3
            #x = np.array([Ball_x, Ball_y, Direction, Ball_speed_x, Ball_speed_y, Platform]).reshape((1, -1))
            #y = self.model.predict(x)	
            #print(os.getcwd())
            if Direction==0:
                slope=1
            elif Direction==1:
                slope=-1
            elif Direction==2:
                slope=-1
            elif Direction==3:
                slope=1

            x=((400-Ball_y)/slope)+Ball_x

            #print(x)
            if x<=0:
               x=-x
               if x>=200:
                   x=x-(x-200)*2
			
            elif x>=200:
               x=x-(x-200)*2
               if x<=0:
                   x=-x

            #print(Ball_x,Ball_y,Direction,x)
            if x==(Platform+25):
                command = "NONE"
            elif x<(Platform+25):
                command = "MOVE_LEFT"
            elif x>(Platform+25):
                command = "MOVE_RIGHT"

        self.previous_ball = scene_info["ball"]
        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
