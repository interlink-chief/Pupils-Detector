Architecture: [figma](https://www.figma.com/file/2C53L0KhQTwOMrpxIsmVCR/Centroids-detector?type=whiteboard&node-id=0%3A1&t=KwWL17chcdEzb7nR-1)
## Table of contents

- [Description](#description)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
- [Installation](#installation)

## Description
An eye centroids detector program is a computer program designed to detect and locate the positions of the centroids of the eyes in a video stream. The centroids are the points that represent the center of each eye. 

The program typically uses computer vision techniques such as image processing, feature detection, and machine learning algorithms to identify the eyes in the input video stream. Once the eyes are detected, the program calculates the centroid coordinates by analyzing the shape, size, and position of the eye regions.

In addition to detecting the centroids of the eyes, some eye centroids detector programs may also provide additional feature such as eye tracking on 3D graphic. This feature can be used for various applications such as driver monitoring systems, virtual reality, and human-computer interaction.

## Technologies
- Python:
> [opencv](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)

> [NumPy](https://numpy.org/)

> [matplotlib.pyplot](https://matplotlib.org/stable/gallery/mplot3d/wire3d.html)

> [time](https://docs.python.org/3/library/time.html)

> [concurrent](https://docs.python.org/3/library/concurrency.html)

> [tornado](https://www.tornadoweb.org/en/stable/)

> [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

## Getting Started
- with Python Virtual Environment:
```bash
python -m venv myenv
```
> activation Windows:
```bash
myenv\Scripts\activate
```
> activation Unix/Linux (Bash/Zsh):
```bash
source myenv/bin/activate
```
> activation Unix/Linux (Fish):
```bash
source myenv/bin/activate.fish
```
> activation Unix/Linux (Csh/Tcsh):
```bash
source myenv/bin/activate.csh
```

- with Conda environment:
```bash
conda create --name myenv
```
> activation:
```bash
conda activate myenv
```

## Installation 
> Local Machine(root directory)
```bash
python server.py
```
> Local Machine (Docker)
```bash
docker login
```
```bash
docker-compose up
```
