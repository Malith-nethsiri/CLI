# functions

import datetime
import time
import pygame
import typer
from func import format_time


app = typer.Typer()


#-------------------------------
# This is an alarm clock program
#-------------------------------
@app.command("alarm")
def set_alarm():

        while True:
            try:

                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                typer.echo(f"Current time is: {current_time}")

                alarm_time = input("⏰Set alarm time in HH:MM format (press 'x' to quit)-- ").strip() or "x"
                if alarm_time.lower() == "x":
                    break

                elif not len(alarm_time) == 5 and alarm_time[2] == ':':
                    typer.echo("❌ Invalid input. Please enter a valid time in HH:MM format. ❌\n")
                    break

                elif current_time > alarm_time:
                    typer.echo(f"⚠ Alarm time has passed. Current time is:{current_time} ⚠ \n")
                    break

                else:
                    alarm_name = input("Set an alarm name -- ") or "wake up times up"

                    if len(alarm_time) == 5 and alarm_time[2] == ':':
                        #CONVERT TO HH:MM:SS FORMAT
                        current_time = datetime.datetime.now().strftime("%H:%M:%S") #############################################
                        alarm_time = datetime.datetime.strptime(alarm_time, "%H:%M").strftime("%H:%M:%S")


                        #LOOP UNTIL THE ALARM TIME MATCHES THE CURRENT TIME
                        while True:
                            if current_time < alarm_time:
                                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                                typer.echo(f"\r{current_time}",nl=False)
                                time.sleep(1)

                            elif current_time == alarm_time:
                                typer.echo(f"\n*******{alarm_name}*******\n**********{current_time}**********\n\n")
                                pygame.mixer.init()
                                pygame.mixer.music.load("D:/MyProjects/practice/CLI/ALARM/Assassins Creed IV_ Black Flag leave her, Johnny.mp3")
                                pygame.mixer.music.play()

                                while pygame.mixer.music.get_busy():
                                    time.sleep(1)
                                break


            except ValueError :
                typer.echo("❌ ValueError occurs ❌\n")




#-----------------------------
# This is a stopwatch program
#-----------------------------

# the stopwatch---------------
@app.command("stopwatch")
def stopwatch():

    start_time = time.time()
    try:
        y_n = input("Do you want to start the stopwatch? (y/n): ").strip().lower() or "n"

        if y_n == 'y':
            typer.echo("❌ Stopwatch started. Press Ctrl+C to stop. ❌")
            while True:
                elapsed_time = time.time()- start_time
                formated =format_time(elapsed_time)
                typer.echo(f"\rElapsed time: {formated}",nl=False )
                time.sleep(0.01)


        elif y_n == 'n':
            typer.echo("Stopwatch not started.\n")


        else:
            typer.echo("❌ Invalid input. Please enter 'y' or 'n'. ❌\n")


    except KeyboardInterrupt:
        typer.echo("\nStopwatch stopped.\n")
    except ValueError :
        typer.echo("❌   ValueError   ❌")





if __name__ == "__main__":
    app()
