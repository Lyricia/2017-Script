from tkinter import *


def callback(event, tag):
    print(event.widget.get('%s.first'%tag, '%s.last'%tag))

root = Tk()

text = Text(root)
text.pack()

text.tag_config("tag1", foreground="blue")
text.tag_bind("tag1", "<Button-1>", lambda e:callback(e, "tag1"))
text.insert(END, "first link", "tag1")

text.insert(END, " other text ")

text.tag_config("tag2", foreground="blue")
text.tag_bind("tag2", "<Button-1>", lambda e:callback(e, "tag2"))
text.insert(END, "second link ", "tag2")

text.tag_config("tag3", foreground="blue")
text.tag_bind("tag3", "<Button-1>", lambda e:callback(e, "tag3"))
text.insert(END, "second123 link", "tag3")

root.mainloop()