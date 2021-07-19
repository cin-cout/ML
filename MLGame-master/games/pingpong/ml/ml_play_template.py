"""
The template of the script for the machine learning process in game pingpong
"""

class MLPlay:
    def __init__(self, side):
        """
        Constructor

        @param side A string "1P" or "2P" indicates that the `MLPlay` is used by
               which side.
        """
        self.ball_served = False
        self.side = side
        self.previous_ball = (0, 0)

    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """
        if scene_info["status"] != "GAME_ALIVE":
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            return "SERVE_TO_LEFT"
        else:

            Ball_x = scene_info["ball"][0]
            Ball_y = scene_info["ball"][1]
            Ball_speed_x = scene_info["ball"][0] - self.previous_ball[0]
            Ball_speed_y = scene_info["ball"][1] - self.previous_ball[1]
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

            if y == 0:
                command = "NONE"
            elif y == -1:
                command = "MOVE_LEFT"
            elif y == 1:
                command = "MOVE_RIGHT"

            self.previous_ball = scene_info["ball"]
            return command



    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
