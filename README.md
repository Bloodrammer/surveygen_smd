# surveygen_smd
Provides a simple markup syntax for surveys and a renderer for it.



## Simple Markdown syntax

- **[img.png]** - paste img.png onto the survey
- **\#** - radiobox question
- **\*** - checkbox (multiple choice) question
- **\t** or **|** - answer
- **\<text>** - text with a gap after it for the respondent to fill (e.g. name, date, signature etc.)
- **\n** - newline
It also supports escape sequences. Number of answers is limited to 26 per question (well, actually, it's not, but you would go past the alphabet).

## What does it do?
There are two python files - `main.py` and `surveygen.py`. 

`surveygen.py` is a module that contains an SM parser fuction and a `Survey` class that renders it. If launched separately, `surveygen.py` asks for a filename, searches the file in the current directory and processes it, if it's found.

`main.py` is a script that searches through `./input` directory and its subfolders and processes each `.txt` file that it find. The output results are then stored in `./output` directory with the same subfolder structure as in `./input`.


## Requirements
The project requires `python3.5` and packages listed in `requirements.txt`.

## Some additional features that are coded but are not included in the pipeline
- You can choose the alignment for the `paste_image()` function from `['left','center','right']`
- If you would need separate blocks of questions (e.g. Part1 - questions 1-7, Part2 - questions 1-8 instead of questions 1-15), `question()` function has a `reset_count=False` parameter.
- For debugging purposes, you can use the `draw_grid()` function, which draws a grid over the area within the margin.
