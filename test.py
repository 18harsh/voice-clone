from moviepy.editor import *


clip = VideoFileClip("static/saket.mp4")
audioclip = AudioFileClip("static/demo_output.wav")
videoclip = clip.set_audio(audioclip)

videoclip.write_videofile("static/saket_stud.mp4")