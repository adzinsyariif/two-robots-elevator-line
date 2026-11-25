import os

LINE = "Floor 9? Same. I ran 40,000 simulations of this chat and in 39,999 I just stared at the door — so, uh, nice shaft we're in."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
