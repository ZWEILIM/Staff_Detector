import cv2
import os
from mypath import Path

def extract_frames_from_mp4_videos(base_dir, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the base directory
    for filename in os.listdir(base_dir):
        if filename.endswith(".mp4"):  # Check if the file has a .mp4 extension
            # Get the full path of the video file
            video_path = os.path.join(base_dir, filename)

            # Open the video file
            video = cv2.VideoCapture(video_path)

            # Get some video properties
            frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
            fps = video.get(cv2.CAP_PROP_FPS)

            # Loop through each frame and save them
            for frame_number in range(frame_count):
                ret, frame = video.read()
                if not ret:
                    break  # Break the loop if the video ends

                # Save the frame with a unique name directly in the output folder
                frame_name = f"frame{frame_number:04d}_ori.png"
                frame_path = os.path.join(output_folder, frame_name)
                cv2.imwrite(frame_path, frame)

            # Release the video object
            video.release()

            print(f"Extracted all frames from '{filename}' and saved in '{output_folder}' at {fps} FPS.")

# Provide the base directory and use it to construct the output folder
base_dir = Path.db_root_dir('FootfallCam')
input_folder = os.path.join(base_dir, 'video')
output_folder = os.path.join(base_dir, 'video_frame', 'TBD/images/every_frame')

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

extract_frames_from_mp4_videos(input_folder, output_folder)




# import cv2
# import os
# from mypath import Path

# def extract_frames_from_mp4_videos(base_dir, output_folder):
#     # Create the output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     # Iterate through all files in the base directory
#     for filename in os.listdir(base_dir):
#         if filename.endswith(".mp4"):  # Check if the file has a .mp4 extension
#             # Get the full path of the video file
#             video_path = os.path.join(base_dir, filename)

#             # Open the video file
#             video = cv2.VideoCapture(video_path)

#             # Get some video properties
#             fps = video.get(cv2.CAP_PROP_FPS)

#             # Calculate the frame interval based on the desired frame rate (1 frame per second)
#             frame_interval = int(fps)  # Change this if you want a different frame rate

#             # Loop through each frame and save them with the specified interval
#             frame_number = 0
#             while True:
#                 ret, frame = video.read()
#                 if not ret:
#                     break  # Break the loop if the video ends

#                 # Save the frame with a unique name directly in the output folder
#                 frame_name = f"frame{frame_number:04d}_ori.png"
#                 frame_path = os.path.join(output_folder, frame_name)
#                 cv2.imwrite(frame_path, frame)

#                 # Move to the next frame with the specified interval
#                 frame_number += 1  # Increment for every frame, not just saved frames
#                 video.set(cv2.CAP_PROP_POS_FRAMES, frame_number * frame_interval)

#             # Release the video object
#             video.release()

#             print(f"Extracted frames from '{filename}' and saved in '{output_folder}' at {fps} FPS.")

# # Provide the base directory and use it to construct the output folder
# base_dir = Path.db_root_dir('FootfallCam')
# input_folder = os.path.join(base_dir, 'video')
# output_folder = os.path.join(base_dir, 'video_frame', 'TBD/images/every_frame')

# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# extract_frames_from_mp4_videos(input_folder, output_folder)
