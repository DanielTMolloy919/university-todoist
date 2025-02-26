# University Todoist Task Generator

This program generates a CSV file with tasks for each week of a university class, following the Todoist CSV import format.

## Features

- Creates one task per week for each class
- Automatically skips midsemester break weeks
- Supports specifying the day of the week when classes occur
- Outputs a CSV file that can be imported directly into Todoist

## Requirements

- Python 3.6 or higher

## Usage

1. Edit the configuration variables at the top of `main.py`:

2. Run the program:

```bash
uv run main.py
```

### Configuration Options

- `CLASS_NAME`: Name of the class (e.g., "COMP3100")
- `START_DATE`: Start date of the semester in YYYY-MM-DD format
- `CLASS_DAY`: Day of the week when the class happens (0=Monday, 1=Tuesday, etc.)
- `NUM_WEEKS`: Total number of weeks in the semester
- `BREAK_WEEKS`: List of week numbers when there's a midsemester break (e.g., [7, 8])
- `OUTPUT_FILE`: Output CSV file name (default: university_tasks.csv)

### Example

With the default configuration, the program will generate tasks for COMP3100 starting from February 27, 2023, for 12 weeks, with breaks in weeks 7 and 8. The class is scheduled for Mondays, and no tasks will be created for the break weeks.

## Importing to Todoist

1. Run the program to generate the CSV file
2. In Todoist, go to Settings > Import/Export
3. Select "Import from CSV file"
4. Choose the generated CSV file
5. Follow the prompts to complete the import
