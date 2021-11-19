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
            "object-oriented",
            "automata languages",
            "compilers",
            "programming languages",
            "design languages",
            "engineering languages",
            "constraint programming"
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
            "vision"
        },
        "nokeywords": {
        },
        "ratings": {"A*", "A", "B", "C", "1", "2", "3"},
        "blacklist": {},
    },

    "all": {
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
                "vision",
                "data mining",
                "intelligent",
                "knowledge",
            },
            "nokeywords": {
            },
            "ratings": {"A*", "A", "B", "C", "1", "2", "3"},
            "blacklist": {},
        },
}
