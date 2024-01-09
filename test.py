# import cv2
# from ultralytics import YOLO
# import os

# # Load the YOLOv8 model
# model = YOLO(r'C:\Program Files (x86)\Work\FootfallCam\weights\focus_on_tag\best.pt') # FOT
# # model = YOLO(r'C:\Program Files (x86)\Work\FootfallCam\weights\focus_on_people\best.pt') #FOP

# # Open the video file
# # video_path = r"C:\Program Files (x86)\Work\FootfallCam\Sample_Own.mp4"
# video_path = r"C:\Program Files (x86)\Work\FootfallCam\data\video\sample.mp4"
# cap = cv2.VideoCapture(video_path)
 
# # Get video properties
# fps = cap.get(cv2.CAP_PROP_FPS)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Define the codec and create a VideoWriter object
# result_video_folder = r"C:\Program Files (x86)\Work\FootfallCam\data\result_4_FOT"
# if not os.path.exists(result_video_folder):
#     os.makedirs(result_video_folder)
# result_video_path = os.path.join(result_video_folder, 'result_video.mp4')
# fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # or use 'XVID'
# out = cv2.VideoWriter(result_video_path, fourcc, fps, (width, height))

# # Loop through the video frames
# while cap.isOpened():
#     # Read a frame from the video
#     success, frame = cap.read()

#     if success:
#         # Run YOLOv8 inference on the frame
#         results = model(frame)

#         # Visualize the results on the frame
#         annotated_frame = results[0].plot()

#         # Write the annotated frame to the output video
#         out.write(annotated_frame)

#         # Display the annotated frame (optional)
#         cv2.imshow("YOLOv8 Inference", annotated_frame)

#         # Break the loop if 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break
#     else:
#         # Break the loop if the end of the video is reached
#         break

# # Release the video capture object, VideoWriter, and close the display window
# cap.release()
# out.release()
# cv2.destroyAllWindows()



# import cv2
# from ultralytics import YOLO
# import os

# # Load the YOLOv8 model
# model = YOLO(r'C:\Program Files (x86)\Work\FootfallCam\weights\focus_on_PnT\best.pt') # FOPT
# # model = YOLO(r'C:\Program Files (x86)\Work\FootfallCam\weights\focus_on_tag\best.pt') # FOT
# # model = YOLO(r'C:\Program Files (x86)\Work\FootfallCam\weights\focus_on_people\best.pt') #FOP

# # Open the video file
# video_path = r"C:\Program Files (x86)\Work\FootfallCam\Sample_Own.mp4"
# # video_path = r"C:\Program Files (x86)\Work\FootfallCam\data\video\sample.mp4"
# cap = cv2.VideoCapture(video_path)

# # Get video properties
# fps = cap.get(cv2.CAP_PROP_FPS)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Define the codec and create a VideoWriter object
# result_video_folder = r"C:\Program Files (x86)\Work\FootfallCam\data\result_5_FOPT"
# if not os.path.exists(result_video_folder):
#     os.makedirs(result_video_folder)
# result_video_path = os.path.join(result_video_folder, 'result_video.mp4')
# fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # or use 'XVID'
# out = cv2.VideoWriter(result_video_path, fourcc, fps, (width, height))

# # Loop through the video frames
# while cap.isOpened():
#     # Read a frame from the video
#     success, frame = cap.read()

#     if success:
#         # Run YOLOv8 inference on the frame
#         results = model(frame)

#         # Visualize the results on the frame
#         annotated_frame = results[0].plot()

#         # Write the annotated frame to the output video
#         out.write(annotated_frame)

#         # Display the annotated frame (optional)
#         cv2.imshow("YOLOv8 Inference", annotated_frame)

#         # Introduce a delay to match the original frame rate
#         delay = int(1000 / fps)  # Delay in milliseconds
#         cv2.waitKey(delay)

#         # Break the loop if 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break
#     else:
#         # Break the loop if the end of the video is reached
#         break

# # Release the video capture object, VideoWriter, and close the display window
# cap.release()
# out.release()
# cv2.destroyAllWindows()


# import cv2
# from ultralytics import YOLO
# import os
# import json 

# # Load the YOLOv8 model
# model = YOLO(r'C:\Program Files (x86)\Work\FootfallCam\weights\focus_on_PnT\best.pt') # FOPT
# # model = YOLO(r'C:\Program Files (x86)\Work\FootfallCam\weights\focus_on_tag\best.pt') # FOT
# # model = YOLO(r'C:\Program Files (x86)\Work\FootfallCam\weights\focus_on_people\best.pt') #FOP

# # Open the video file
# # video_path = r"C:\Program Files (x86)\Work\FootfallCam\Sample_Own.mp4"
# video_path = r"C:\Program Files (x86)\Work\FootfallCam\Sample_short.mp4"
# # video_path = r"C:\Program Files (x86)\Work\FootfallCam\data\video\sample.mp4"
# cap = cv2.VideoCapture(video_path)

# # Get video properties
# fps = cap.get(cv2.CAP_PROP_FPS)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Define the codec and create a VideoWriter object
# result_video_folder = r"C:\Program Files (x86)\Work\FootfallCam\data\result_11_FOPT"
# if not os.path.exists(result_video_folder):
#     os.makedirs(result_video_folder)
# result_video_path = os.path.join(result_video_folder, 'result_video.mp4')
# fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # or use 'XVID'
# out = cv2.VideoWriter(result_video_path, fourcc, fps, (width, height))


# json_file_path = os.path.join(result_video_folder, 'result.json')

# # cv2.namedWindow("YOLOv8 Inference", cv2.WINDOW_NORMAL)
# # cv2.resizeWindow("YOLOv8 Inference", 800, 600)  # Adjust the size as needed

# # Loop through the video frames
# while cap.isOpened():
#     success, frame = cap.read()

#     if success:
#         # Run YOLOv8 inference on the frame
#         results = model(frame)

#         # Convert YOLOv8 results to JSON
#         json_results = results[0].tojson()

#         # Save JSON results to a file
#         with open(json_file_path, 'w') as json_file:
#             json.dump(json_results, json_file, indent=2)

#         # Visualize the results on the frame
#         annotated_frame = results[0].plot()

#         # Filter results to display only when class is 1
#         if 'class' in json_results[0] and json_results[0]['class'] == 1:
#             # Convert JSON results to string
#             json_str = json.dumps(json_results, indent=2)

#             # Display JSON content on the frame
#             cv2.putText(annotated_frame, json_str, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#         # Write the annotated frame to the output video
#         out.write(annotated_frame)

#         # Display the annotated frame (optional)
#         cv2.imshow("YOLOv8 Inference", annotated_frame)

#         # Introduce a delay to match the original frame rate
#         delay = int(1000 / fps)
#         cv2.waitKey(delay)

#         # Break the loop if 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break
#     else:
#         break

# # Release the video capture object, VideoWriter, and close the display window
# cap.release()
# out.release()
# cv2.destroyAllWindows()





import cv2
from ultralytics import YOLO
import os
import json 
import numpy as np


# Load the YOLOv8 model
model = YOLO(r'C:\Program Files (x86)\Work\FootfallCam\weights\without any checkpoint\best.pt') # FOPT
# model = YOLO(r'C:\Program Files (x86)\Work\FootfallCam\weights\focus_on_tag\best.pt') # FOT
# model = YOLO(r'C:\Program Files (x86)\Work\FootfallCam\weights\focus_on_people\best.pt') #FOP

# Open the video file
# video_path = r"C:\Program Files (x86)\Work\FootfallCam\Sample_Own.mp4"
# video_path = r"C:\Program Files (x86)\Work\FootfallCam\Sample_short.mp4"
video_path = r"C:\Program Files (x86)\Work\FootfallCam\data\video\sample.mp4"
cap = cv2.VideoCapture(video_path)

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create a VideoWriter object
result_video_folder = r"C:\Program Files (x86)\Work\FootfallCam\data\result_23"
if not os.path.exists(result_video_folder):
    os.makedirs(result_video_folder)
result_video_path = os.path.join(result_video_folder, 'result_video.mp4')
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # or use 'XVID'
out = cv2.VideoWriter(result_video_path, fourcc, fps, (width, height))


json_file_path = os.path.join(result_video_folder, 'result.json')

# cv2.namedWindow("YOLOv8 Inference", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("YOLOv8 Inference", 800, 600)  # Adjust the size as needed

# Loop through the video frames
while cap.isOpened():
    success, frame = cap.read()

    if success:
       # Run YOLOv8 inference on the frame
        results = model(frame)

        # Convert YOLOv8 results to JSON
        json_results = json.loads(results[0].tojson())

        # Save JSON results to a file
        with open(json_file_path, 'w') as json_file:
            json.dump(json_results, json_file, indent=2)

        # Filter entries with the name "staff"
        staff_entries = [entry for entry in json_results if entry.get('name') == 'Staff']

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # if staff_entries:
        #     for staff_entry in staff_entries:
        #         # Extract relevant information
        #         name = staff_entry.get('name', '')
        #         class_label = staff_entry.get('class', '')
        #         confidence = staff_entry.get('confidence', '')
        #         box = staff_entry.get('box', {})

        #         # # Extract box coordinates
        #         # x1, y1, x2, y2 = map(int, [box['x1'], box['y1'], box['x2'], box['y2']])

        #         # # Change the bounding box color based on class label
        #         # color = (0, 0, 255)  # Default to red
        #         # if class_label == 1:  # Change to yellow for class 1
        #         #     color = (0, 255, 255)

        #         # # Draw the bounding box on the frame
        #         # cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, 2)

        #     # Display information on the frame (in the top-left corner)
        #     info_str = f"name: {name}, confidence: {confidence:.4f}, box: {box}"
        #     cv2.putText(annotated_frame, info_str, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        if staff_entries:
            for staff_entry in staff_entries:
                # Extract relevant information
                name = staff_entry.get('name', '')
                class_label = staff_entry.get('class', '')
                confidence = staff_entry.get('confidence', '')
                box = staff_entry.get('box', {})

                # Display information on the frame (in the top-left corner)
                info_str = f"name: {name},\nconfidence: {confidence:.4f},\nbox: {box}"
                lines = info_str.split('\n')
                y_position = 30
                for line in lines:
                    cv2.putText(annotated_frame, line, (10, y_position), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                    y_position += 20  # Adjust the vertical spacing

        # Write the annotated frame to the output video
        out.write(annotated_frame)

        # Display the annotated frame (optional)
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Introduce a delay to match the original frame rate
        delay = int(1000 / fps)
        cv2.waitKey(delay)

        # Break the loop if 'q' is pressedq
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


    #    # Run YOLOv8 inference on the frame
    #     results = model(frame)

    #     # Convert YOLOv8 results to JSON
    #     json_results = json.loads(results[0].tojson())

    #     # Save JSON results to a file
    #     with open(json_file_path, 'w') as json_file:
    #         json.dump(json_results, json_file, indent=2)

    #     # Filter entries with the name "staff"
    #     staff_entries = [entry for entry in json_results if entry.get('name') == 'staff']

    #     # Visualize the results on the frame
    #     annotated_frame = results[0].plot()
        
    #     if staff_entries:
    #         # # Convert JSON results to string
    #         # json_str = json.dumps(staff_entries, indent=2)

    #         # # Display JSON content on the frame
    #         # cv2.putText(annotated_frame, json_str, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    #         for staff_entry in staff_entries:
    #             # Extract relevant information
    #             name = staff_entry.get('name', '')
    #             class_label = staff_entry.get('class', '')
    #             confidence = staff_entry.get('confidence', '')
    #             box = staff_entry.get('box', {})

    #             # Display information on the frame
    #             info_str = f"name: {name}, class: {class_label}, confidence: {confidence:.4f}, box: {box}"
    #             cv2.putText(annotated_frame, info_str, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    #     # Write the annotated frame to the output video
    #     out.write(annotated_frame)

    #     # Display the annotated frame (optional)
    #     cv2.imshow("YOLOv8 Inference", annotated_frame)

    #     # Introduce a delay to match the original frame rate
    #     delay = int(1000 / fps)
    #     cv2.waitKey(delay)

    #     # Break the loop if 'q' is pressed
    #     if cv2.waitKey(1) & 0xFF == ord("q"):
    #         break
    else:
        break

# Release the video capture object, VideoWriter, and close the display window
cap.release()
out.release()
cv2.destroyAllWindows()