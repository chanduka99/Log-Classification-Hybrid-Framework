import re


def classify_with_regex(log_message):
    """
    Classifies a log message into predefined categories using regular expression patterns.
    This function iterates through a dictionary of regex patterns and their corresponding labels.
    It returns the label of the first matching pattern, or None if no pattern matches.
    Args:
        log_message (str): The log message string to be classified.
    Returns:
        str or None: The classification label (e.g., "User Action", "System Notification") if a pattern matches,
                     otherwise None.
    Examples:
        >>> classify_with_regex("User User123 logged in.")
        'User Action'
        >>> classify_with_regex("Backup started at 2023-01-01.")
        'System Notification'
        >>> classify_with_regex("Unknown message.")
        None
    """

    regex_patterns = {
        r"User User\d+ logged (out|in).": "User Action",
        r"Account with ID .* created by .*.": "User Action",
        r"Backup (started|ended) at .*": "System Notification",
        r"Backup completed successfully.": "System Notification",
        r"System updated to version .*": "System Notification",
        r"File .* uploaded successfully by user .*": "System Notification",
        r"Disk cleanup completed successfully.": "System Notification",
        r"System reboot initiated by user User.*": "System Notification",
    }

    for regex_pattern, label in regex_patterns.items():
        if re.search(regex_pattern, log_message):
            return label
    return None


if __name__ == "__main__":
    message = "User User123 logged in."
    label = classify_with_regex(message)
    print(f"Message: {message}")
    print(f"Classified as: {label}")
    print("-" * 40)

    message = "Account with ID 456 created by admin."
    label = classify_with_regex(message)
    print(f"Message: {message}")
    print(f"Classified as: {label}")
    print("-" * 40)

    message = "Backup started at 2026-04-29 10:00:00"
    label = classify_with_regex(message)
    print(f"Message: {message}")
    print(f"Classified as: {label}")
    print("-" * 40)

    message = "Backup completed successfully."
    label = classify_with_regex(message)
    print(f"Message: {message}")
    print(f"Classified as: {label}")
    print("-" * 40)

    message = "System updated to version 5.2.1"
    label = classify_with_regex(message)
    print(f"Message: {message}")
    print(f"Classified as: {label}")
    print("-" * 40)

    message = "File report.pdf uploaded successfully by user alice"
    label = classify_with_regex(message)
    print(f"Message: {message}")
    print(f"Classified as: {label}")
    print("-" * 40)

    message = "Disk cleanup completed successfully."
    label = classify_with_regex(message)
    print(f"Message: {message}")
    print(f"Classified as: {label}")
    print("-" * 40)

    message = "System reboot initiated by user User789"
    label = classify_with_regex(message)
    print(f"Message: {message}")
    print(f"Classified as: {label}")
    print("-" * 40)

    message = "Unrecognized log entry for testing"
    label = classify_with_regex(message)
    print(f"Message: {message}")
    print(f"Classified as: {label}")
    print("-" * 40)
