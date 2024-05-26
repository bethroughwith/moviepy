from moviepy.editor import VideoFileClip
import os
import imageio

# 视频文件路径
video_path = r"D:\桌面文件\李佩忆\李佩忆视频模版.mp4"

# 输出图片目录
output_dir = r"D:\output_images"

# 创建输出目录
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 读取视频文件
clip = VideoFileClip(video_path)

# 将视频的每一帧保存为图片
for i, frame in enumerate(clip.iter_frames(fps=1, dtype='uint8')):
    frame_path = os.path.join(output_dir, f"frame_{i}.png")
    imageio.imwrite(frame_path, frame)

print("所有帧图片已导出到目录:", output_dir)