import datetime
import time
import sched
import os
import subprocess

scheduler = sched.scheduler(time.time, time.sleep)
def kill_rlcd_tasks(sc): 
    print("haha task kill go brrrrrr")

    now = datetime.datetime.now()
    print (f"The Time is Now: {now.hour}:{now.minute}:{now.second}")

    if now.hour == 4: 
        tasks_to_kill = ["Rocketleague.exe", "cmd.exe", "obs64.exe", "Brave.exe"]
        for task in tasks_to_kill:
         os.system(f"taskkill /IM {task}"),
        time.sleep(3600),
        #another way to do this if the .exe fails
        #subprocess.call([r"C:\Program Files\AutoHotkey\autohotkey.exe", r"C:\Users\Publicspace\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Setup_Bot.ahk"])
        subprocess.call(r"C:\Users\Publicspace\Documents\Setup_Bot.exe")
    else:
        print("nah not feeling it")

    sc.enter(60, 1, kill_rlcd_tasks, (sc,))

scheduler.enter(60, 1, kill_rlcd_tasks, (scheduler,))
scheduler.run()