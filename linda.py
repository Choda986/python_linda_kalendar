from datetime import datetime, timedelta


def get_dates_from_monday(reference_date=None):
    """
    Calculate next Thursday and following Wednesday from a Monday.

    Args:
        reference_date: datetime object (defaults to today)

    Returns:
        tuple: (thursday_date, wednesday_date) in dd-m format
    """
    if reference_date is None:
        reference_date = datetime.now()

    # Find the most recent Monday (including today if it's Monday)
    days_since_monday = reference_date.weekday()
    monday = reference_date - timedelta(days=days_since_monday)

    # Calculate next Thursday (Monday + 3 days)
    thursday = monday + timedelta(days=3)

    # Calculate following Wednesday (Thursday + 6 days)
    wednesday = thursday + timedelta(days=6)

    # Format as dd-m (remove leading zero from month)
    thursday_str = f"{thursday.day:02d}-{thursday.month}"
    wednesday_str = f"{wednesday.day:02d}-{wednesday.month}"

    return thursday_str + "-" + wednesday_str


# Example usage
if __name__ == "__main__":
    day = get_dates_from_monday()
    print(f"Output: {day}")
