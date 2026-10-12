# Calculate Average Grade and Write to a File

1. Edit `average_grade.py`.

2. We want to calculate the average grade for each student and write it into a new file.

3. Add codes to open `student_data.csv` to read each student's grades.
    
    Hints: 
    - Skip the header row with data[1:]

4. Add code to read each student's grades and calculate their average grade.

    Hints:
    - CSV data comes as strings, convert grade columns to integer with `int()` for maths
    - `student_data.csv` has columns: ID, Name, Mathematics, Science, History
    - average = (maths + science + history) / 3.

5. Add codes to open a file called `report.txt` for writing. Write each student's name and their average grade to the report.

    Hints: 
    - Use `w` mode to create a fresh report each time
    - Format averages nicely, maybe to 2 decimal places with `:.2f`.