
<img src="./logo.png" width="400">


## Description
Image-To-Text is an Ethereum ready dapp that applies [tesseract-OCR](https://github.com/tesseract-ocr/tesseract) to extract text from images.  

![demo](./images/demo.png)


## Usage
Bring your images together in a folder (exp: DATADIR) and add an ```input-config.yml``` file in the same folder. This file defines text's language for each image and it should respect the ```<imagename>: <lang>``` format. You can keep the language's section empty but this may affect the performance of the extraction process.

![screenshot](./images/screenshot-1.png)

In the ```app/app-config.yml``` file, change the datadir parameter to the path of your folder (DATADIR for our example) and run the script.

    $ cd image-to-text/app/src/
    $ python3 app.py

You shoud find your extracted text files in the ```DATADIR/out/``` folder.

![screenshot](./images/screenshot-2.png)


## Supported languages
English (**en**), Spanish (**es**), Frensh (**fr**), Arabic (**ar**), German (**de**), Chinese simple (**zh**), Italian (**it**), Japanese (**ja**), Portuguese (**pt**), Russian (**ru**), Turkish (**tr**), Korean (**ko**).


## Supported image types
Tested extensions: **jpeg**, **bmp**, **png**  
Those extensions are accepted but were not tested yet: **pbm**, **pgm**, **ppm**, **tiff**, **rast**, **xbm**  

## Dependencies
[python3](https://www.python.org/)  
[tesseract-ocr](https://github.com/tesseract-ocr/tesseract)  
[opencv](https://opencv.org/)


## Docker installation
After installing [docker](https://docs.docker.com/install/) and preparing your DATADIR folder, just grab the image from dockerhub and run it:

    $ docker run -v path/to/datadir:/iexec/ ziedguesmi/image-to-text

Or you can build your own image from dockerfile:

    # clone the dapp
    $ git clone https://github.com/Zied-Guesmi/image-to-text.git && cd image-to-text/ 

    # build the docker image
    $ docker build -t image-to-text .

    # run the container
    $ docker run -v path/to/datadir:/iexec/ image-to-text


## Installation
Clone the app:

    $ git clone https://github.com/Zied-Guesmi/image-to-text.git

Install system dependencies:

    # ubuntu as an example
    $ apt-get update && apt-get install -y \
        libtesseract-dev \
        libsm6 \
        python3 \
        python3-pip \
        tesseract-ocr \
        tesseract-ocr-ara \
        tesseract-ocr-eng \
        tesseract-ocr-fra \
        tesseract-ocr-spa \
        tesseract-ocr-deu \
        tesseract-ocr-chi-sim \
        tesseract-ocr-ita \
        tesseract-ocr-jpn \
        tesseract-ocr-por \
        tesseract-ocr-rus \
        tesseract-ocr-tur \
        tesseract-ocr-kor

Install python depedencies:

    $ cd image-to-text/app/
    $ pip3 install -r requirements.txt
