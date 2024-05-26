from moviepy.editor import VideoFileClip

# 视频文件路径
video_path = r"D:\桌面文件\李佩忆\李佩忆视频模版.mp4"

# 输出音频文件路径
output_audio_path = r"D:\桌面文件\李佩忆\背景音乐.mp3"

# 读取视频文件
video_clip = VideoFileClip(video_path)

# 提取背景音乐（音频）
audio_clip = video_clip.audio

# 导出音频到指定路径
audio_clip.write_audiofile(output_audio_path)

print(f"背景音乐已导出到: {output_audio_path}")