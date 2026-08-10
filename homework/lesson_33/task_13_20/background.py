from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def send_book_email(title: str):
    with open(BASE_DIR / "emails.log", "a", encoding="utf-8") as file:
        file.write(f"Nowa książka: {title}\n")


def update_book_statistics():
    with open(BASE_DIR / "statistics.log", "a", encoding="utf-8") as file:
        file.write("Usunięto książkę - statystyki zaktualizowane\n")


def send_comment_email(post_id: int):
    with open(BASE_DIR / "emails.log", "a", encoding="utf-8") as file:
        file.write(f"Nowy komentarz do posta {post_id}\n")


def analyze_sentiment(comment: str):
    positive_words = ["super", "dobry", "świetny", "lubię"]
    text = comment.lower()

    if any(word in text for word in positive_words):
        sentiment = "positive"
    else:
        sentiment = "neutral"

    with open(BASE_DIR / "sentiment.log", "a", encoding="utf-8") as file:
        file.write(f"{comment} -> {sentiment}\n")
