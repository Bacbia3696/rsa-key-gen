from src import rsa_key_gen
import pytest


@pytest.mark.parametrize("test_input", [
    (100),
    (200),
    (300)
])
def test_rsa_key_gen(test_input):
    # check correctness
    n, e, d, p, q = rsa_key_gen.rsa_key_gen(123)
    ciper_text = pow(test_input, e, n)
    decrypted_text = pow(ciper_text, d, n)
    assert decrypted_text == test_input
    # check private key remain the same with the same seed
    assert (n, e, d, p, q) == rsa_key_gen.rsa_key_gen(123)
