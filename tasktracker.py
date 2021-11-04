import stdio

# Building a task tracking application using python
# The path function makes sure that there is a text file created to store tasks

from pathlib import Path
Path("/home/diefenbw/tasktracker2/tasktracker.md").touch()

stdio.writeln("Enter tasks that you have to do. If you are unsure about the task
        end that task with a '?'")

