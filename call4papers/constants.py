MINIMAL_COLUMNS = ["Acronym",  "Title",  "CORE rank", "GGS Class",  "deadline",  "when",  "where"]

DEFAULT_SETUPS = {
    "nlp": {
        "keywords": {
            "artificial intelligence",
            "machine learning",
            "pattern recognition",
            "learning representation",
            "computational linguistics",
            "learning theory",
            "neural network",
            "machine translation",
            "natural language",
            "spoken language",
            "language technology",
            "low resource",
            "neural information",
            "representation learning",
            "empirical methods",
            "language",
            "neural",
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
        "whitelist": {"NEURIPS", "ICLR", "ICML", "AAAI", "IJCAI", "COLT", "AISTATS", "IJCNN",
                      "ACL", "EMNLP", "NAACL", "TACL", "COLING", "CoNLL", "EACL", "IJCNLP", "EAMT", "LORESMT", "PACLIC",
                      "AMTA", "MT SUMMIT", "INLG", "SIGDIAL", "SLT", "LREC", "SEMEVAL", "WMT", "RepL4NLP", "BEA"},
        "blacklist": {"PLDI", "PADL", "ALT", "CICLING", "DLT", "SLE", "NLDB", "DLS", "LATA", "SNPD", "JELIA",
                      "COORDINATION", "ECML PKDD", "WOLLIC"},
    },

    "vision": {
        "keywords": {
            "artificial intelligence",
            "machine learning",
            "pattern recognition",
            "learning representation",
            "learning theory",
            "neural network",
            "neural information",
            "representation learning",
            "neural",
            "learning",
            "vision",
            "intelligent",
        },
        "nokeywords": {
        },
        "ratings": {"A*", "A", "B", "C", "1", "2", "3"},
        "whitelist": {"NEURIPS", "ICLR", "ICML", "AAAI", "IJCAI", "COLT", "AISTATS", "IJCNN",
                      "CVPR", "ICCV", "ECCV", "ICPR"},
        "blacklist": {"PLDI", "PADL", "ALT", "CICLING", "DLT", "SLE", "NLDB", "DLS", "LATA", "SNPD", "JELIA",
                      "COORDINATION", "ECML PKDD", "IDA", "IVA", "IDC", "ACIIDS", "ISC", "ITS", "EC-TEL", "LAK",
                      "IUI", "VISIGRAPP"},
    },
}

# Get all keys
DEFAULT_SETUPS["all"] = {
    "keywords": set().union(*[x["keywords"] for x in DEFAULT_SETUPS.values()]),
    "nokeywords": set().union(*[x["nokeywords"] for x in DEFAULT_SETUPS.values()]),
    "ratings": set().union(*[x["ratings"] for x in DEFAULT_SETUPS.values()]),
    "whitelist": set().union(*[x["whitelist"] for x in DEFAULT_SETUPS.values()]),
    "blacklist": set().union(*[x["blacklist"] for x in DEFAULT_SETUPS.values()]),
}

