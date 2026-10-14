# Create Inverted Image

We want to create an inverted image of a pgm image file.

1. Edit `invert_image.py`.

2. Write codes to open a pgm image file and read the content. 
    
    - You could handle file errors with try/except.

3. Write code for the inverted image.
    
    The formula to invert each pixel:

        invert_pixel_value = max_gray - original_pixel_value

4. Write the inverted pgm image to a new file.

    - Remember to include the string `P2`, the width and height dimensions, and the maximum gray value
    - You could convert numbers in a list to strings and join them with spaces. For example:
        
        ```
        line = [255, 255, 0, 255, 255]
        string_line = " ".join(str(item) for item in line) 
        # output: string_line = "255 255 0 255 255"
        ```

5. Open the inverted pgm image to verify.