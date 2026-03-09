def analyze_sentiment(text):

    text = text.lower()

    negative_keywords = [
        "pressure",
        "tight deadlines",
        "fast paced",
        "high workload",
        "incident response",
        "24/7",
        "on call",
        "urgent",
        "critical",
        "stressful",
        "long hours"
    ]

    positive_keywords = [
        "flexible",
        "work life balance",
        "supportive",
        "collaborative",
        "friendly team",
        "growth",
        "learning",
        "benefits",
        "remote friendly"
    ]

    negative_score = sum(word in text for word in negative_keywords)
    positive_score = sum(word in text for word in positive_keywords)

    if negative_score > positive_score:
        return "Negative Work Environment"

    elif positive_score > negative_score:
        return "Positive Work Environment"

    else:
        return "Neutral Work Environment"