# from tkinter import *
# from PIL import Image, ImageTk, ImageSequence
# import time
# import pygame
# from pygame import mixer
# import threading  # Import the threading module
#
# mixer.init()
#
# root = Tk()
# root.geometry("1000x500")
#
# def play_gif_thread():
#     # Function to play GIF in a separate thread
#     t = threading.Thread(target=play_gif)
#     t.start()
#
# def play_gif():
#     root.lift()
#     root.attributes("-topmost", True)
#     img = Image.open("snap.gif")
#     lbl = Label(root)
#     lbl.place(x=0, y=0)
#
#     mixer.music.load("Startup2.mp3")
#     mixer.music.play()
#
#     start_time = time.time()
#
#     for frame in ImageSequence.Iterator(img):
#         frame = frame.resize((1000, 500))
#         img = ImageTk.PhotoImage(frame)
#         lbl.config(image=img)
#         root.update()
#         time.sleep(0.05)
#
#         if time.time() - start_time >= 1 and not mixer.music.get_busy():
#             break
#
#     root.after(2000, root.destroy)
#
# # Call the function to play GIF in a separate thread
# play_gif_thread()
#
# # Start the Tkinter event loop
# root.mainloop()
# from tkinter import *
# from PIL import Image, ImageTk, ImageSequence
# import time
# import pygame
# from pygame import mixer
# import threading  # Import the threading module
#
# mixer.init()
#
# root = Tk()
# root.geometry("1000x500")
#
# def play_gif_thread():
#     # Function to play GIF in a separate thread
#     t = threading.Thread(target=play_gif)
#     t.start()
#
# def play_gif():
#     img = Image.open("snap.gif")
#     start_time = time.time()
#     frames = []
#
#     # Load frames
#     for frame in ImageSequence.Iterator(img):
#         frame = frame.resize((1000, 500))
#         frames.append(ImageTk.PhotoImage(frame))
#
#     # Play music
#     mixer.music.load("Startup2.mp3")
#     mixer.music.play()
#
#     # Display frames
#     for img in frames:
#         lbl.config(image=img)
#         root.lift()
#         root.attributes("-topmost", True)
#         root.update()
#         time.sleep(0.05)
#
#         if time.time() - start_time >= 1 and not mixer.music.get_busy():
#             break
#
#     # Destroy root after 2 seconds
#     root.after(2000, root.destroy)
#
# lbl = Label(root)
# lbl.place(x=0, y=0)
#
# # Call the function to play GIF in a separate thread
# play_gif_thread()
#
# # Start the Tkinter event loop
# root.mainloop()



# from tkinter import *
# from PIL import Image, ImageTk, ImageSequence
# import time
# import pygame
# from pygame import mixer
# import threading
#
# mixer.init()
#
# root = Tk()
# root.geometry("1000x500")
#
# def play_gif_thread():
#     # Function to play GIF in a separate thread
#     t = threading.Thread(target=play_gif)
#     t.start()
#
# def play_gif():
#     img = Image.open("snap.gif")
#     start_time = time.time()
#     frames = []
#
#     # Load frames
#     for frame in ImageSequence.Iterator(img):
#         frame = frame.resize((1000, 500))
#         frames.append(ImageTk.PhotoImage(frame))
#
#     # Play music
#     mixer.music.load("Startup2.mp3")
#     mixer.music.play()
#
#     # Display frames
#     for img in frames:
#         lbl.config(image=img)
#         root.lift()
#         root.attributes("-topmost", True)
#         root.update()
#         time.sleep(0.05)
#
#         if time.time() - start_time >= 1 and not mixer.music.get_busy():
#             break
#
#     # Destroy root after 2 seconds
#     root.after(2000, root.destroy)
#
# lbl = Label(root)
# lbl.place(x=0, y=0)
#
# # Call the function to play GIF in a separate thread
# play_gif_thread()
#
# # Start the Tkinter event loop
# root.mainloop()
