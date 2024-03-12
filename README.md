# Video to Gif Converter
A simple Python script that converts videos into GIFs.

## Prerequirements

* Install python:
```
sudo apt install python3
sudo apt install python3-pip
```

* Install moviepy:
```
pip install moviepy
```

## How to use it?

* Clone this repo to your computer: 
```
git clone https://github.com/KarloLeksic/video-to-gif-converter.git
```
* Put all videos that you wanna convert to gifs into the `videos` folder.
* Adjust parameters according to your needs:
```
inputFolder = "videos"
outputFolder = "gifs"
videoExtension = ".webm"
gifFps = 10
```
* To execute the script, position the terminal in this folder, and just run: 
```
python3 gifConverter.py
``` 
* When the script is finished, your gifs are in `gifs` folder 😀
