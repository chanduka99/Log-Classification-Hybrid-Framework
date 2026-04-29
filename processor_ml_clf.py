import joblib
from sentence_transformers import SentenceTransformer

# Load the model
model = joblib.load("./models/log_clf.joblib")

# Load sentence transformer
sentence_model = SentenceTransformer("all-MiniLM-L6-v2")


def classify_with_ml_clf(log_message: str) -> str:
    """
    Classify a log message using a saved model and sentence embeddings.

    Args:
        log_message: The log message to classify

    Returns:
        The predicted label
    """
    # Generate embedding
    embedding = sentence_model.encode(log_message)

    # Reshape for single sample prediction
    embedding = embedding.reshape(1, -1)

    probabilities = model.predict_proba(embedding)[0]

    if probabilities.max() < 0.5:
        return "Unclassified"

    # Predict
    prediction = model.predict(embedding)

    return prediction[0]


if __name__ == "__main__":
    # Example usage
    log_msg = "Hey bro chill yah, I am just testing the BERT-SVM classifier."
    label = classify_log_message(log_msg)
    print(f"Predicted label: {label}")
