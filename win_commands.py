
import random
import numpy as np

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

    np.array(["win", "open/close start"]),
    np.array(["win + d", "display/hide desktop"]),
    np.array(["win + tab", "switch virtual desktop"]),

    np.array(["alt + f4",  "close app"]),
    np.array(["alt + tab",  "switch app"]),

    np.array(["f2", "rename"]),
    np.array(["f5", "refresh"]),
    np.array(["f11", "enter/exit fullscreen"]),
])

# GET RANDOM INDEX FROM COMMAND ARRAY
def random_command():
    rand  = random.randrange(0,len(cmd_arr)-1)
    return cmd_arr[rand]

# GET RANDOM INDEX FROM COMMAND ARRAY FOR CHOICES
# BUTTON MODE: predef button, mode=0
# NAME MODE: predef name, mode=1
def choices(answer, mode):
    print("Answer: ", answer)
    
    ch=np.array([])
    ch = np.append(ch, answer)

    for i in range(3):
        rand_c  = random.randrange(0,len(cmd_arr)-1)
        new_choice = cmd_arr[rand_c][1]
        
        while new_choice in ch:
            rand_c = random.randrange(0,len(cmd_arr)-1)

            new_choice = None
            if mode == 0: new_choice = cmd_arr[rand_c][1]
            elif mode == 1: new_choice = cmd_arr[0][rand_c]

        ch = np.append(ch, new_choice)
        

    np.random.shuffle(ch)
    return ch

def quiz(mode):
    rand_ind = random_command()
    question = None
    answer = None
    
    # BUTTON MODE: predef button, mode=0
    if(mode == 0):
        question = rand_ind[0]
        answer = rand_ind[1]

    # NAME MODE: predef name, mode=1
    elif(mode == 1):
        question = rand_ind[1]
        answer = rand_ind[0]

    return {"question":question, "choices": choices(answer, mode), "answer": answer }
