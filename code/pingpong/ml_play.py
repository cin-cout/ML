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
    def __init__(self, side):
        """
        Constructor

        @param side A string "1P" or "2P" indicates that the `MLPlay` is used by
               which side.
        """
        self.ball_served = False
        self.side = side
        self.previous_blocker = (0, 0)
        with open(os.path.join(os.path.dirname(__file__), 'model_1P.pickle'), 'rb') as f:
            self.model_1P = pickle.load(f)
        with open(os.path.join(os.path.dirname(__file__), 'model_2P.pickle'), 'rb') as f:
            self.model_2P = pickle.load(f)
        """
        load your "1P" and "2P" model here
        可以是一個檔案或是兩個檔案，但相對路徑要放好 (路徑請用相對路徑，並放在相同目錄底下)
        
        sample 1: (如果 "1P", "2P" 是分開 train)
        self.model_1 = 1P pickle
        self.model_2 = 2P pickle
        
        sample 2: (如果 "1P", "2P" train 成一個 model)
        self.model = "1P" and "2P" pickle
        """

    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """
        if scene_info["status"] != "GAME_ALIVE":
            #print("die place______",scene_info["platform_1P"])
            print(scene_info["ball_speed"])
            return "RESET"
            
        if not self.ball_served:
            self.ball_served = True
            return "SERVE_TO_LEFT"
        
        else:
            if self.side == "1P":
                Ball_x = scene_info["ball"][0]
                Ball_y = scene_info["ball"][1]
                Ball_speed_x = scene_info["ball_speed"][0]
                Ball_speed_y = scene_info["ball_speed"][1]
                Blocker_x = scene_info["blocker"][0]
                Blocker_speed_x = scene_info["blocker"][0] - self.previous_blocker[0]
                Platform = scene_info["platform_1P"][0]


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
                
                x = np.array([Ball_x, Ball_y, Ball_speed_x, Ball_speed_y,Direction,Blocker_x,Blocker_speed_x]).reshape((1, -1))
                y = self.model_1P.predict(x)

                if Platform==y:
                    command = "NONE"
                elif Platform>y:
                    command = "MOVE_LEFT"
                elif Platform<y:
                    command = "MOVE_RIGHT"
            
            if self.side == "2P":
                Ball_x = scene_info["ball"][0]
                Ball_y = scene_info["ball"][1]
                Ball_speed_x = scene_info["ball_speed"][0]
                Ball_speed_y = scene_info["ball_speed"][1]
                Blocker_x = scene_info["blocker"][0]
                Blocker_speed_x = scene_info["blocker"][0] - self.previous_blocker[0]
                Platform = scene_info["platform_2P"][0]


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
                
                x = np.array([Ball_x, Ball_y, Ball_speed_x, Ball_speed_y,Direction,Blocker_x,Blocker_speed_x]).reshape((1, -1))
                y = self.model_2P.predict(x)

                if Platform==y:
                    command = "NONE"
                elif Platform>y:
                    command = "MOVE_LEFT"
                elif Platform<y:
                    command = "MOVE_RIGHT"
            
            self.previous_blocker = scene_info["blocker"]
            return command
        """
        如果是兩個 model 可以在程式中用 side 去判斷要用哪個 model 
        
        sample 1: (如果 "1P", "2P" 是分開 train)
        if self.side == "1P":
            # 使用 model 1 預測
        else:
            # 使用 model 2 預測
            
        sample 2: (如果 "1P", "2P" train 成一個 model)
        # 直接使用 model 預測
        """
        

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
