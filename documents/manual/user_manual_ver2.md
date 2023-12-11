# User Manual - Version 2

## Command 1: Record

### Overview

The record feature allows you to input a task that you have completed in order to keep track of it. It uses this format:
* `python timetracker.py record date from_time to_time 'task' :TAG`

#### Some important details:
* `python timetracker.py` is always required to run a command
* You can choose to omit AM or PM, but it will be set to AM as default.
* Dates must always be in YYYY/mm/dd form or simply put `today` for the date, otherwise the application will tell you your date format is wrong, and your command will not be processed.
* Your task needs to be enclosed in quotations (as a string) such that you can put multiple words in your task description example: `'studied java'`
* All tags must start with ":", otherwise your command will not be processed correctly. 

#### Example commands:
* `python timetracker.py record today 1:00 2:00 'studied software design' :STUDY`
* `python timetracker.py record 2023/12/3 12:00pm 3:00pm 'studied cross-platform development' :STUDY`
* `python timetracker.py record 2023/1/4 1:00PM 2:00PM 'went for a run' :FITNESS`

## Command 2: Query

### Overview

The query feature allows you to search for all entries by a specific date, task, or tag. It uses this format:
* `python timetracker.py query argument` (replace argument with a date, task, or tag)

#### Some important details
* Your query argument must be in the exact form that you want to search for. For example, having an entry with 2023/12/12 and searching with 12/12/2023 as an a argument will not return the desired result.
* The same overall formatting rules apply to this command, dates must be in YYYY/mm/dd, tasks must be enclosed in quotations, and tags must start with ':'.

#### Example Commands:
* `python timetracker.py query 2023/12/1`
* `python timetracker.py query today`
* `python timetracker.py query 'studied java'`
* `python timetracker.py query :STUDY`

## Command 3: Report

### Overview

The report feature allows you to generate a report of your activity between two dates. It uses this format:
* `python timetracker.py report start_date end_date` (replace start_date and end_date with desired date range)

#### Some important details
* You must give a valid date range, i.e. your start date must be before the end date for the command to function properly.

#### Example Commands:
* `python timetracker.py report 2023/1/1 2023/12/1`
* `python timetracker.py report 2023/1/1 today`

## Command 4: Priority

### Overview

The priority command allows you to generate a list of the amount of hours you have spent on each task in descending order of number of hours. It uses this format:
* `python timetracker.py priority`

#### Some important details
* This command's output is grouped by specific task, so similarly named tasks will not be counted. For example 'studied java' and 'study java' would not be combined together.

