# Additional Work For Week 3

If you finish the tasks quickly and have time on your hands, here are some
other things you can try. Put your code for this additional work in this
directory, to keep it separate from the other tasks.


## Frequency Analysis
Frequency analysis is a method of breaking certain ciphers which involves counting the frequency of letters/symbols
because English has quite a clear distribution of letters, with spikes on common letters such as 'e', 'i' and 's'.

Write a program to open a file and count how many instances of each letter are in the program.


## Using csv.DictReader for csv files

The data dictionary solution is nice, but inelegant - we can actually do this much easier by using
a library called `csv` which can do this all in one go.

Rewrite the code for average grade task in `session2/task3/2_average_grade/` using `csv.DictReader` to read the data and `csv.DictWriter()` to write to file.

You need to `import csv` to use `csv.DictReader` and `csv.DictWriter()`.