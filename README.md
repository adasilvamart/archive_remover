# ArchiveRemover

## Description
This simple script removes archives in the given directory. For example it's useful for Windows temp files from <strong>"%temp%", "temp" and "prefetch"</strong> directories. 
You can leave a scheduled task in the Task Manager that runs this script under the conditions you want. For example, once a week at 1:00 p.m.

## Usage
Replace the comment in the line 45 with your directories separated by commas as a
<strong>raw string</strong>. When you define a text string with `r`, Python interprets the string as written, without any special escape sequences.

Example of use:
```python
directories = [ r'C:\Path\to\Directory' ]
```