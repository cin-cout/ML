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
        self.previous_blocker = (0, 0)

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

            if Direction==0:
                slope=1
            elif Direction==1:
                slope=-1
            elif Direction==2:
                slope=-1
            elif Direction==3:
                slope=1
            
            if Ball_speed_y<0:
                if Platform==80:
                    x=(Platform+20)
                elif Platform<80:
                    x=9999999
                else:
                    x=-999999
            
                #blocker下端反彈
                if Ball_y>260:
                    x2=((260-Ball_y)/slope)+Ball_x

                    if x2<=0:
                        x2=-x2
                        if x2>=200:
                            x2=x2-(x2-200)*2
		
                    elif x2>=200:
                        x2=x2-(x2-200)*2
                        if x2<=0:
                            x2=-x2
                
                    time=((260-Ball_y)/(Ball_speed_y))
                
                    #預測blocker_x
                    if Blocker_speed_x>=0:
                        preX=Blocker_x+5*time

                        if preX>195:
                            preX=preX-(preX-195)*2
                
                    elif Blocker_speed_x<0:
                        preX=Blocker_x-5*time

                        if preX<0:
                            preX=-preX
                    #如果是預測值，預測反彈
                    if preX<=x2 and x2<=preX+20:
                        if Ball_x<=preX:
                            slope2=1
                        elif Ball_x>preX:
                            slope2=-1
                        x=((420-260)/slope2)+x2

                        if x<=0:
                            x=-x
                            if x>=200:
                                x=x-(x-200)*2
		
                        elif x>=200:
                            x=x-(x-200)*2
                            if x<=0:
                                x=-x
            
            elif Ball_speed_y>0:
                x=((420-Ball_y)/slope)+Ball_x
                if x<=0:
                    x=-x
                    if x>=200:
                        x=x-(x-200)*2
		
                elif x>=200:
                    x=x-(x-200)*2
                    if x<=0:
                        x=-x                        
                if Ball_y<240:

                    x240=((240-Ball_y)/slope)+Ball_x
                    x250=((250-Ball_y)/slope)+Ball_x
                    x260=((260-Ball_y)/slope)+Ball_x
                    
                    if x240<=0:
                        x240=-x240
                        if x240>=200:
                            x240=x240-(x240-200)*2		
                    elif x240>=200:
                        x240=x240-(x240-200)*2
                        if x240<=0:
                            x240=-x240                    
                    if x260<=0:
                        x260=-x260
                        if x260>=200:
                            x260=x260-(x260-200)*2
                    elif x260>=200:
                        x260=x260-(x260-200)*2
                        if x260<=0:
                            x260=-x260
                    if x250<=0:
                        x250=-x250
                        if x250>=200:
                            x250=x250-(x250-200)*2		
                    elif x250>=200:
                        x250=x250-(x250-200)*2
                        if x250<=0:
                            x250=-x250                   
                    
                    time260=abs((260-Ball_y)/(Ball_speed_y))
                     
                    if Blocker_speed_x>=0:
                        preX260=Blocker_x+5*time260

                        if preX260>195:
                            preX260=preX260-(preX260-195)*2                
                    elif Blocker_speed_x<0:
                        preX260=Blocker_x-5*time260

                        if preX260<0:
                            preX260=-preX260
                    #print(x240,x250,x260,time260,preX260)
                    if x240<x260:#從左邊來
                        if x240<(preX260-15) and (preX260-15)<x260:
                            #print('get1')
                            x=((420-250)/(-1))+x250
                            if x<=0:
                                x=-x
                                if x>=200:
                                    x=x-(x-200)*2
                            elif x>=200:
                                x=x-(x-200)*2
                                if x<=0:
                                    x=-x
                    if x240>x260:#從右邊來
                        if x240>(preX260+35) and (preX260+35)>x260:
                            #print("get2")
                            x=((420-250)/(1))+x250                    
                            if x<=0:
                                x=-x
                                if x>=200:
                                    x=x-(x-200)*2
                            elif x>=200:
                                x=x-(x-200)*2
                                if x<=0:
                                    x=-x                    
            


            #print('LAST_____',x)
            if x==(Platform+20):
                command = "NONE"
            elif x<(Platform+20):
                command = "MOVE_LEFT"
            elif x>(Platform+20):
                command = "MOVE_RIGHT"


            self.previous_blocker = scene_info["blocker"]
            return command





    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
