from sys import argv
skript_name, work_hours, perhour, bonus = argv
print(int(work_hours)*int(perhour)+int(bonus))