from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

def combine_videos(input_folder, output_folder, output_filename):
    # Get a list of all video files in the input folder
    video_files = [file for file in os.listdir(input_folder) if file.endswith(".mp4")]

    # Sort video files based on their modification time
    video_files.sort(key=lambda x: os.path.getmtime(os.path.join(input_folder, x)))

    # Load each video clip
    clips = [VideoFileClip(os.path.join(input_folder, file)) for file in video_files]

    # Concatenate the video clips
    final_clip = concatenate_videoclips(clips)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Write the concatenated video to the output folder
    output_path = os.path.join(output_folder, output_filename)
    final_clip.write_videofile(output_path)

    # Close the clips to release memory
    final_clip.close()
    for clip in clips:
        clip.close()

# Example usage
input_folder = "/home/s186/Music/video"
output_folder = "/home/s186/Documents/data_collection_testbed"
output_filename = "combined_video.mp4"
combine_videos(input_folder, output_folder, output_filename)


