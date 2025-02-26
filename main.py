import csv
import datetime
from typing import List, Dict

# ===== CONFIGURATION (EDIT THESE VALUES) =====
# Name of the class (e.g., "COMP3100 Lecture")
CLASS_NAME = "COMP3100 Lecture"

# Start date of the semester (YYYY-MM-DD)
START_DATE = "2023-02-27"

# Day of the week when the class happens (0=Monday, 1=Tuesday, 2=Wednesday, 3=Thursday, 4=Friday, 5=Saturday, 6=Sunday)
CLASS_DAY = 0  # Monday by default

# Total number of weeks in the semester
NUM_WEEKS = 12

# List of week numbers when there's a midsemester break (e.g., [7, 8])
BREAK_WEEKS = [7, 8]

# Output CSV file name
OUTPUT_FILE = "university_tasks.csv"
# =============================================


def generate_university_tasks(
    class_name: str,
    start_date: datetime.date,
    class_day: int,
    num_weeks: int,
    break_weeks: List[int],
    output_file: str = "university_tasks.csv"
) -> None:
    """
    Generate a CSV file with tasks for each week of a university class.
    
    Args:
        class_name: Name of the class (e.g., "COMP3100")
        start_date: The start date of the semester
        class_day: Day of the week when the class happens (0=Monday, 1=Tuesday, etc.)
        num_weeks: Total number of weeks in the semester
        break_weeks: List of week numbers when there's a midsemester break
        output_file: Output CSV file name
    """
    # Define the headers based on Todoist CSV format
    headers = [
        "TYPE", "CONTENT", "DESCRIPTION", "PRIORITY", "INDENT", 
        "AUTHOR", "RESPONSIBLE", "DATE", "DATE_LANG", "TIMEZONE",
        "DURATION", "DURATION_UNIT", "DEADLINE", "DEADLINE_LANG"
    ]
    
    # Create tasks for each week
    tasks: List[Dict[str, str]] = []
    
    # Add the meta row
    tasks.append({
        "TYPE": "meta",
        "CONTENT": "view_style=list",
        "DESCRIPTION": "",
        "PRIORITY": "",
        "INDENT": "",
        "AUTHOR": "",
        "RESPONSIBLE": "",
        "DATE": "",
        "DATE_LANG": "",
        "TIMEZONE": "",
        "DURATION": "",
        "DURATION_UNIT": "",
        "DEADLINE": "",
        "DEADLINE_LANG": ""
    })
    
    # Add an empty row
    tasks.append({header: "" for header in headers})
    
    # Map day number to day name
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_name = day_names[class_day]
    
    # Calculate the first class date (adjust start_date to match class_day)
    days_to_add = (class_day - start_date.weekday()) % 7
    first_class_date = start_date + datetime.timedelta(days=days_to_add)
    
    # Generate tasks for each week
    current_date = first_class_date
    for week in range(1, num_weeks + 1):
        # Skip tasks for break weeks
        if week in break_weeks:
            # Skip break weeks entirely
            pass
        else:
            # Add class task
            tasks.append({
                "TYPE": "task",
                "CONTENT": f"{class_name} Week {week} ({day_name})",
                "DESCRIPTION": "",
                "PRIORITY": "4",
                "INDENT": "1",
                "AUTHOR": "",
                "RESPONSIBLE": "",
                "DATE": current_date.strftime("%Y-%m-%d"),
                "DATE_LANG": "en",
                "TIMEZONE": "",
                "DURATION": "",
                "DURATION_UNIT": "",
                "DEADLINE": "",
                "DEADLINE_LANG": ""
            })
        
        # Move to next week
        current_date += datetime.timedelta(days=7)
    
    # Add an empty row at the end
    tasks.append({header: "" for header in headers})
    
    # Write tasks to CSV file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for task in tasks:
            writer.writerow(task)
    
    print(f"Generated {len(tasks)} tasks for {class_name} in {output_file}")
    print(f"Class day: {day_name}")


def parse_date(date_str: str) -> datetime.date:
    """Parse a date string in YYYY-MM-DD format."""
    return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()


def main():
    # Parse the start date
    start_date = parse_date(START_DATE)
    
    # Generate the tasks
    generate_university_tasks(
        class_name=CLASS_NAME,
        start_date=start_date,
        class_day=CLASS_DAY,
        num_weeks=NUM_WEEKS,
        break_weeks=BREAK_WEEKS,
        output_file=OUTPUT_FILE
    )


if __name__ == "__main__":
    main()
