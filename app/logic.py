import random

DESAFIOS = [
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
        "desafio": "Resolva: 2, 4, 8, 16, ?",
        "portas": ["20", "32", "24"],
        "resposta_correta": 1
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
        "desafio": "Resolva: Qual número completa a sequência? 3, 6, 9, ?",
        "portas": ["10", "12", "15"],
        "resposta_correta": 1
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
    }
]


def get_random_challenge():
    return random.choice(DESAFIOS)


def validate_choice(escolha: int, resposta: int) -> bool:
    return escolha == resposta
