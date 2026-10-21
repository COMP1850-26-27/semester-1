
# PGM files - functional decomposition

Last week you started work on code to handle PGM files
- simple grey-scale image data
- reading a PGM image from a text-file
- simple processing of the PGM image data

Now we can consider how to write functions to handle PGM files
- reading a file from disk
- writing a file to disk
- operations on PGM image data

This is a more modular way to program
- we design a "toolkit" of functions that we can use

The `readPGM()` function is implemented
- this basic implementation does no validation or error checking
- you may want to check that the file exists
- you may want to include a check for a comment line

Implement `writePGM()` to write a PGM image to disk
- you can test this by writing out the same image to a new file name
- if you write to an existing filename you will overwrite what is there

Implement `invertPGM()` to invert the gray-scale
- you only have to modify the pixel array
    -  pixel_value -> 255 - pixel_value
- you can test by writing out the inverted image to disk

Further functions could be creeated to:
- rotate the image by 90 degrees
- threshold the image
    - set a minimum or maximum pixel value for the image
    