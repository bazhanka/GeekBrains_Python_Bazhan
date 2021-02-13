classes = {}
with open("Task6","r") as f6:
    for line in f6:
        oneclass=list(line.split())
        hours=0
        for something in oneclass:
            h2=""
            for el in something:
                try:
                    el1 = int(el)
                    h2+=el
                except ValueError:
                    pass
            try:
                h2=int(h2)
                hours+=h2
            except ValueError:
                pass
        classes[oneclass[0]]=hours
print(classes)

