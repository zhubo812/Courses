from moviepy.editor import VideoFileClip, ImageClip

path = 'F:\\ftp\\Friends.S03E01.720p.BluRay.x264-WiKi.mkv';

clip1 = VideoFileClip(path).subclip(300,310).resize(0.60) #读取视频，并截取10-20秒的内容

clip1.write_videofile("F:\\ftp\\clip.mp4")

clip1.audio.write_audiofile("F:\\ftp\\clip.mp3")

print('ok')
