# Background Information on PGM format

PGM (Portable Gray Map) is part of a [family of simple file formats](https://en.wikipedia.org/wiki/Netpbm#File_formats) that can be used for the storage of images.

PGM is actually two file formats, one text-based and the other binary. We consider only the text-based format here.

PGM files are suitable for storing grayscale images - i.e., images in which each pixel is a single integer, representing a shade of gray. This ranges from a minimum of 0 (black) up to a specified maximum value (white). The maximum is usually 255, allowing for 256 distinct shades of gray for each pixel.

A text-based PGM file consists of:

- The string "P2", which identifies the file as a text-based PGM image
- An optional comment line, starting with a # character
- Width and height dimensions
- Maximum gray value
- A grid of pixel values representing the image

Here's the example from Wikipedia's page on the PGM format:

    P2
    # Shows the word "FEEP"
    24 7
    15
    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0
    0  3  3  3  3  0  0  7  7  7  7  0  0 11 11 11 11  0  0 15 15 15 15  0
    0  3  0  0  0  0  0  7  0  0  0  0  0 11  0  0  0  0  0 15  0  0 15  0
    0  3  3  3  0  0  0  7  7  7  0  0  0 11 11 11  0  0  0 15 15 15 15  0
    0  3  0  0  0  0  0  7  0  0  0  0  0 11  0  0  0  0  0 15  0  0  0  0
    0  3  0  0  0  0  0  7  7  7  7  0  0 11 11 11 11  0  0 15  0  0  0  0
    0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0

There are 3 tasks in this activity:

1. Print basic information of a PGM image
2. Validate a PGM image
3. Create an inverted PGM image

Navigate to invidual directory to proceed.