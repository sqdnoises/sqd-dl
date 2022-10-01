# Avatar Generator
Generate gradient avatars on demand.
<br>
This is a port of Aelpxy's avatar generator. [View repository](https://github.com/Aelpxy/avatar-generator)

## Getting Started
Clone this repository or download the zip and extract it to a folder you like.

### Requirements
You need [Python 3.6+](https://www.python.org/downloads/) for this to work.

### Install pip Requirements
Open a terminal in the folder this readme is in.

#### On Windows:
Make sure python is on path.
<br>
Run:
```
python -m pip install -r requirements.txt
```
OR
```
python -m pip install colorhash
```

#### On MacOS/Linux:
Make sure python3 is on path.
<br>
(If this command gives an error saying no module pip or something, make sure any python pip related packages are installed.)
<br>
Run:
```
python3 -m pip install -r requirements.txt
```
OR
```
python3 -m pip install colorhash
```

## To run
Open a terminal in the src folder.

### On windows:
Make sure python is on path.
<br>
Run:
```
py app.py
```

### On MacOS/Linux:
Make sure python3 is on path.
<br>
Run:
```
python3 app.py
```

## To use
Goto http://localhost:5050/ for a random image.
<br>
Goto http://localhost:5050/<some text\> where `<some text>` is the seed.
<br>
<br>
### For custom sizes,
You can use the parameter `size` to change its size in pixels.
<br>
Examples:
 - For random image: http://localhost:5050/?size=100
   <br>
   This changes the size of the image to 100 pixels.
 - With a seed: http://localhost:5050/<seed\>?size=340
   <br>
   Where `<seed>` is the seed.
   <br>
   This changes the size of the image to 100 pixels.

### For a square image,
You can use the parameter `square`  to change the shape of the svg to square.
<br>
Accepts values:
 - `true`, `t`, `yes`, `y` and `1` (any case) if you want to see square image.
 - `false`, `f`, `no`, `n` and `0` (any case) if you want to see the circular image

Examples:
 - For random image: http://localhost:5050/?square=1
 - With a seed: http://localhost:5050/<seed\>?square=yes
   <br>
   Where `<seed>` is the seed.

### Change size and make it a square
If you want to change the size of the image and also make it a square image, you can do so too by putting a `&` between the parameters.
<br>
Examples:
 - For random image: http://localhost:5050/?size=305&square=true
   <br>
   This changes the size of the image to 305 pixels and also makes it a square.
 - With a seed: http://localhost:5050/<seed\>?square=y&size=1058
   <br>
   Where `<seed>` is the seed.
   <br>
   This changes the size of the image to 1058 pixels and also makes it a square.