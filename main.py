import random
import numpy as np

# mode = input("wala lang")
# print(mode)

cmd_arr = np.array([
    np.array(["ctrl + a", "select all"]),
    np.array(["ctrl + b", "bold"]),
    np.array(["ctrl + c", "copy"]),
    np.array(["ctrl + e", "center"]),
    np.array(["ctrl + f", "find"]),
    np.array(["ctrl + h", "history"]),
    np.array(["ctrl + i", "italic"]),
    np.array(["ctrl + j", "downloads/justify"]),
    np.array(["ctrl + m", "mute tab"]),
    np.array(["ctrl + n", "new window"]),
    np.array(["ctrl + o", "open"]),
    np.array(["ctrl + p", "print"]),
    np.array(["ctrl + s", "save"]),
    np.array(["ctrl + t", "new tab"]),
    np.array(["ctrl + u", "underline"]),
    np.array(["ctrl + v", "paste"]),
    np.array(["ctrl + w", "close window"]),
    np.array(["ctrl + x", "cut"]),
    np.array(["ctrl + y", "undo"]),
    np.array(["ctrl + z", "redo"]),

    np.array(["ctrl + plus", "zoom in"]),
    np.array(["ctrl + minus", "zoom out"]),
    np.array(["ctrl + mouse scroll", "zoom in/out"]),
    np.array(["ctrl + home",  "put cursor to start"]),
    np.array(["ctrl + end",  "put cursor to end"]),
    np.array(["ctrl + up arrow", "scroll up"]),
    np.array(["ctrl + down arrow", "scroll down"]),

    np.array(["windows", "open/close start"]),
    np.array(["windows + d", "display/hide desktop"]),
    np.array(["windows + tab", "switch virtual desktop"]),

    np.array(["alt + f4",  "close app"]),
    np.array(["alt + tab",  "switch app"]),

    np.array(["f2", "rename"]),
    np.array(["f5", "refresh"]),
    np.array(["f11", "enter/exit fullscreen"]),
])

rand  = random.randrange(1,len(cmd_arr))-1
print("Question: ", cmd_arr[rand])

ch = np.array([])
ch = np.append(ch, cmd_arr[rand][1])

for i in range(3):
    rand_c  = random.randrange(1,len(cmd_arr))-1
    ch = np.append(ch, cmd_arr[rand_c][1])

np.random.shuffle(ch)
print("Choices: ",ch)

user_in = int(input("Your answer(1-4): "))
if(cmd_arr[rand][1] == ch[user_in-1]):
    print("TAMA KA")
else:
    print("MALI KA!!!")