from moviepy.editor import VideoFileClip

# Load the video
video_path = 'images/sortinghat.mov'
video = VideoFileClip(video_path)

# Calculate new dimensions to shrink height to 75% while maintaining aspect ratio
target_height = video.size[1] * 0.75
aspect_ratio = video.size[0] / video.size[1]
new_width = target_height * aspect_ratio

# Resize video
resized_video = video.resize(height=target_height)

# Save the resized video
resized_video_path = 'images/sortinghat_resized.mov'
resized_video.write_videofile(resized_video_path, codec="libx264", audio_codec="aac")

resized_video_path
print("yes")
