from datetime import datetime

def date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def Log(level, message, file="logs.txt"):
    with open(file, "a") as f:
        f.write(f"[{level}] {{{date()}}} - <{message}>\n")

