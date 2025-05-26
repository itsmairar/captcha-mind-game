import random

DESAFIOS_EASY = [
    {
        "desafio": "Resolva: 2, 4, 8, 16, ?",
        "portas": ["20", "32", "24"],
        "resposta_correta": 1
    },
    {
        "desafio": "Resolva: Qual número completa a sequência? 3, 6, 9, ?",
        "portas": ["10", "12", "15"],
        "resposta_correta": 1
    },
    {
        "desafio": "Resolva: 1, 1, 2, 3, 5, 8, ?",
        "portas": ["11", "13", "12"],
        "resposta_correta": 1
    },
    {
        "desafio": "Quantos 'A's há na frase: 'A Ana ama as árvores altas'?",
        "portas": ["5", "6", "7"],
        "resposta_correta": 2
    }
]

DESAFIOS_HARD = [
    {
        "desafio": "Apenas uma das frases abaixo é verdadeira. Qual porta leva à saída?",
        "portas": [
            "A porta 2 leva à saída.",
            "A porta 3 leva à morte.",
            "Esta porta leva à saída."
        ],
        "resposta_correta": 0
    },
    {
        "desafio": "Uma das afirmações é falsa. Qual porta você escolhe para sair?",
        "portas": [
            "A porta 3 leva à saída.",
            "Todas as portas levam à saída.",
            "A porta 1 mente."
        ],
        "resposta_correta": 2
    },
    {
        "desafio": "Apenas uma frase é verdadeira. Qual porta leva à saída?",
        "portas": [
            "Porta 2 leva à morte.",
            "Porta 3 mente.",
            "Esta porta é segura."
        ],
        "resposta_correta": 2
    },
    {
        "desafio": "Um coelho vê 6 elefantes indo para o rio. Cada elefante vê 2 macacos indo na direção oposta. Cada macaco segura 1 papagaio. Quantos animais vão para o rio?",
        "portas": ["1", "7", "3"],
        "resposta_correta": 0
    },
    {
        "desafio": "Escolha a única afirmação VERDADEIRA:",
        "portas": [
            "Todas as portas mentem.",
            "Exatamente uma porta está dizendo a verdade.",
            "Essa frase é falsa."
        ],
        "resposta_correta": 1
    },
    {
        "desafio": "Qual afirmação é verdadeira?",
        "portas": [
            "Essa frase é falsa.",
            "A próxima frase é verdadeira.",
            "A frase anterior é falsa."
        ],
        "resposta_correta": 0
    },
    {
        "desafio": "Duas portas mentem. Qual é a correta?",
        "portas": [
            "Eu sou a porta correta.",
            "A porta 1 está mentindo.",
            "A porta 2 está dizendo a verdade."
        ],
        "resposta_correta": 0
    },
    {
        "desafio": "Apenas uma frase é falsa. Qual porta é a certa?",
        "portas": [
            "Porta 3 é segura.",
            "Porta 1 mente.",
            "Porta 2 está errada."
        ],
        "resposta_correta": 0
    }
]


def get_random_challenge(dificuldade="easy"):
    if dificuldade == "hard":
        return random.choice(DESAFIOS_HARD)
    return random.choice(DESAFIOS_EASY)


def validate_choice(escolha: int, resposta: int) -> bool:
    return escolha == resposta
