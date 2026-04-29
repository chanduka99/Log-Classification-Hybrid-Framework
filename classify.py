from processor_regex import classify_with_regex
from processor_ml_clf import classify_with_ml_clf
from processor_llm import classify_with_llm
import pandas as pd


def classify(logs):
    """Classify a sequence of log entries.

    Args:
        logs: An iterable of tuples in the form (source, log_message).

    Returns:
        A list of classification labels, one per log entry.
    """
    labels = []
    for source, log_msg in logs:
        label = classify_log(source, log_msg)
        labels.append(label)
    return labels


def classify_log(source, log_msg):
    """Classify a single log entry based on its source.

    Args:
        source: The source system for the log entry.
        log_msg: The log message text.

    Returns:
        The label assigned to the log entry.

    Notes:
        - For LegacyCRM logs, classification is performed with the LLM.
        - For all other sources, regex classification is attempted first.
        - If regex does not return a label, the ML classifier is used as a fallback.
    """
    if source == "LegacyCRM":
        label = classify_with_llm(log_msg)
    else:
        label = classify_with_regex(log_msg)
        if label is None:
            label = classify_with_ml_clf(log_msg)
    return label


def classify_csv(file_path_or_buffer):
    """Classify logs in a CSV file or buffer and return the classified DataFrame.

    Args:
        file_path_or_buffer: Path to the input CSV file or a file-like buffer.

    Returns:
        A pandas DataFrame with an additional "target_label" column.
    """
    df = pd.read_csv(file_path_or_buffer)
    df["target_label"] = classify(list(zip(df["source"], df["log_message"])))
    return df


def save_classified_csv(df, output_file="resources/output.csv"):
    """Save the classified DataFrame to a CSV file.

    Args:
        df: The classified DataFrame.
        output_file: Path to the output CSV file.
    """
    df.to_csv(output_file, index=False)


def main():
    """Run a simple test of classify_csv using resources/test.csv."""
    input_file = "resources/test.csv"
    df = classify_csv(input_file)
    output_file = "resources/output.csv"
    save_classified_csv(df, output_file)
    print(f"Classified logs written to: {output_file}")


if __name__ == "__main__":
    main()
