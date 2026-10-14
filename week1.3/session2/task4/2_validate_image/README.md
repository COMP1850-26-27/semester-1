# Validate PGM image

We want to write a program to check whether the image width, height and the pixel values corresponds to the dimensions and maximum gray value specified in the pgm image.

1. Edit `validate_image.py`.

2. Write codes to open a pgm image.

    - You could handle file errors with try/except.

3. Write codes to read file content.

    - Assign each of the width, the height, and the maximum gray value to a variable.
    - For each pixel, check if the pixel value is between 0 and the maximum gray value inclusive.
    - Check if the widths and heights are the same as specified.

4. Print the final verdit.

    - Print `Valid image` if the widths, the heights are the same, and all pixel values between 0 and the maximum gray value inclusive.
    - Print `Invalid width` if the widths are different.
    - Print `Invalid height` if the heights are different.
    - Print `Invalid pixel values` if any pixel values is less than 0 and greater than the maximum gray value.