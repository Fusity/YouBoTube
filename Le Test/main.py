#from tkinter import *
from moviepy.editor import *

#main_clip = VideoFileClip("Dua Lipa, Angèle - Fever (Official Music Video).mp4")
#false_song = AudioFileClip("Son de test.mp3")


main_clip = VideoFileClip("Dua Lipa, Angèle - Fever (Official Music Video).mp4")
false_song = AudioFileClip("10.wav")
audio_clip = AudioFileClip("Dua Lipa, Angèle - Fever (Official Music Video).mp3")
first_image_file = ImageClip("image.jpg")

clip_duration = main_clip.duration

audio = afx.audio_loop(false_song, duration=clip_duration).volumex(2)
new_audioclip = CompositeAudioClip([main_clip.audio, audio])
myclip = ImageClip("image.jpg")
myclip = myclip.to_ImageClip(t=clip_duration)
myclip.audio = new_audioclip
myclip.fps = 24
myclip.set_duration(clip_duration).write_videofile("output.mp4")

########################################   THAT'S GOOD   ######################################
'''main_clip = VideoFileClip("Dua Lipa, Angèle - Fever (Official Music Video).mp4")
false_song = AudioFileClip("Son de test.mp3")
audio_clip = AudioFileClip("Dua Lipa, Angèle - Fever (Official Music Video).mp3")

clip_duration = main_clip.duration

audio = afx.audio_loop(false_song, duration=clip_duration).volumex(2)

new_audioclip = CompositeAudioClip([main_clip.audio, audio])
main_clip.audio = new_audioclip
main_clip.write_videofile("new_filename.mp4")'''
