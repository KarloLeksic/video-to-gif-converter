import os
from moviepy.editor import VideoFileClip

# Function that converts videos into GIFs
def convertVideosToGifs(inputFolder, outputFolder, videoExtension, fps):
    # Check if there is an output folder and create one if it doesn't exist
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)

    # Counter for converted videos
    n = 0

    # Go across each file
    for filename in os.listdir(inputFolder):
        # Filter videos by extension
        if filename.endswith(videoExtension):
            inputPath = os.path.join(inputFolder, filename)
            
            # Get the input file name to make the same name for the GIF
            outputFileName = os.path.splitext(filename)[0] + ".gif"
            outputPath = os.path.join(outputFolder, outputFileName)
            
            # Load the video
            clip = VideoFileClip(inputPath)

            # Convert the video to gif and print a message
            clip.write_gif(outputPath, fps=fps)
            print(f"{inputPath} --> {outputPath}")

            # Increase gif counter
            n += 1

    # Print success message
    print(f"Successfully converted {n} {'video' if n == 1 else 'videos'}!")

# Settings - adjust it for your needs
inputFolder = "videos"
outputFolder = "gifs"
videoExtension = ".mp4"
gifFps = 10

# Call the function for converting
convertVideosToGifs(inputFolder, outputFolder, videoExtension=videoExtension, fps=gifFps)
