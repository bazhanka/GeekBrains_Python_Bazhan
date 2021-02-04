#Task2
time=int(input())
if time<=86399: #если нужно реальное время
    hours=int(time/3600)
    minutes=int((time-hours*3600)/60)
    seconds=int(time-hours*3600-minutes*60)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
