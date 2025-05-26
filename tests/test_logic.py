from app.logic import get_random_challenge, validate_choice


def test_random_challenge():
    challenge = get_random_challenge()
    assert "desafio" in challenge
    assert "portas" in challenge
    assert "resposta_correta" in challenge
    assert isinstance(challenge["portas"], list)
    assert isinstance(challenge["resposta_correta"], int)


def test_validate_choice():
    assert validate_choice(1, 1) == True
    assert validate_choice(0, 1) == False
