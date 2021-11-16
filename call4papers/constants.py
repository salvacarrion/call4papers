MINIMAL_COLUMNS = ["Acronym",  "Title",  "CORE rank", "GGS Class",  "deadline",  "when",  "where"]

DEFAULT_SETUPS = {
    "nlp": {
        "keywords": {
            "computational linguistics",
            "machine translation",
            "natural language",
            "artificial intelligence",
            "pattern recognition",
            "machine learning",
            "neural networks",
            "neural",
            "language",
            "learning",
        },
        "nokeywords": {
            "object oriented",
            "automata languages",
            "compilers",
            "programming languages",
            "design languages",
            "engineering languages",
        },
        "ratings": {"A*", "A", "B", "C", "1", "2", "3"},
        "blacklist": {"cicling"},
    },

    "vision": {
        "keywords": {
            "artificial intelligence",
            "pattern recognition",
            "machine learning",
            "neural networks",
            "neural",
            "learning",
        },
        "nokeywords": {
        },
        "ratings": {"A*", "A", "B", "C", "1", "2", "3"},
        "blacklist": {},
    }
}
