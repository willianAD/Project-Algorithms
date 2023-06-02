import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("Hello Word!", 3) == "leH_!droW ol"
    assert encrypt_message("WillianAfonso", 7) == "nailliW_osnofA"
    assert encrypt_message("Dicas Pythonicas", 6) == "sacinohtyP_ saciD"
    assert encrypt_message("SemUnder", 10) == "rednUmeS"
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("ivalid", "key")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(13, 9)
