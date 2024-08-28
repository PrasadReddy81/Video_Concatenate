## Set Up Your Environment
Ensure you have Python installed and the necessary libraries. If not, install the required library using the command above.

## Prepare Your Video Files
Place your MP4 video files in a folder. The script will combine these files in the order of their modification times.

Edit the Script
Update the script with the appropriate paths:

    input_folder: The path to the folder containing your MP4 video files.
    output_folder: The path to the folder where the combined video will be saved.
    output_filename: The name you want to give to the combined video file (e.g., combined_video.mp4).
    Run the Script
## Execute the script from the command line or an IDE:


    python combine_videos.py
    
Make sure the script file is named combine_videos.py or adjust the command accordingly.

**Example**
To combine video files located in /home/s186/Music/video and save the output to /home/s186/Documents/data_collection_testbed with the filename combined_video.mp4, use the following values in the script:


    input_folder = "/home/s186/Music/video"
    output_folder = "/home/s186/Documents/data_collection_testbed"
    output_filename = "combined_video.mp4"
    combine_videos(input_folder, output_folder, output_filename)
**Notes**
The script assumes all files in the input folder with an .mp4 extension are valid video files.
If there are no .mp4 files in the input folder, the script will not create any output.
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
This script uses the moviepy library, which simplifies video editing tasks in Python. Feel free to contribute by submitting issues or pull requests.



  In this version:
  - **`##`** is used for main sections like "Requirements" and "Usage".
  - **`###`** is used for sub-sections like "Set Up Your Environment", "Prepare Your Video Files", etc.

This hierarchy will make the headings appear larger and more organized in the render
