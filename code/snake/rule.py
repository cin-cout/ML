"""
The template of the script for playing the game in the ml mode
"""

class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.Direction="NONE"

    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """
        if scene_info["status"] == "GAME_OVER":
            return "RESET"

        snake_head = scene_info["snake_head"]
        food = scene_info["food"]

        if snake_head == (40,40):
            self.Direction = "RIGHT"
            return "RIGHT"
        
        elif snake_head[0] == 290:

            if self.Direction =="DOWN" :
                self.Direction = "LEFT"
                return "LEFT"
            
            self.Direction = "DOWN"
            return "DOWN"
        
        elif snake_head[0] == 0:

            if self.Direction =="LEFT" :

                if snake_head[1] == 290:
                    self.Direction = "UP"
                    return "UP"
                
                else :
                    self.Direction = "DOWN"
                    return "DOWN"

            elif self.Direction =="DOWN" :
                self.Direction = "RIGHT"
                return "RIGHT"
            
            elif self.Direction =="UP" :

                if snake_head[1] == 0:
                    self.Direction = "RIGHT"
                    return "RIGHT"
        
    def reset(self):
        """
        Reset the status if needed
        """
        self.Direction="NONE"
