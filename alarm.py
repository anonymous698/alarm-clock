import time
import datetime
import pygame

def set_alarm(alarm_time):
    print("alarm set for",alarm_time)
    is_running=True
    try:
        while is_running:
            current_time=datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time)
            if current_time==alarm_time:
                print("Wake Up!!!")
                pygame.mixer.init()
                pygame.mixer.music.load("gg.mp3")
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
                is_running=False
            time.sleep(1)
    except RuntimeWarning:
        print("No Worries")        
        


        
        




if __name__=="__main__":
    alarm_time=input("set alarm time(HH:MM:SS): ")
    set_alarm(alarm_time)
