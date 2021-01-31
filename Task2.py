#Task2
time=int(input())
if time<=86399: #если нужно реальное время
    hours=int(time/3600)
    minutes=int((time-hours*3600)/60)
    seconds=int(time-hours*3600-minutes*60)
    if hours<10:
        hours='0'+str(hours)
    if minutes<10:
        minutes='0'+str(minutes)
    if seconds<10:
        seconds='0'+str(seconds)
    print(f"{hours}:{minutes}:{seconds}")
