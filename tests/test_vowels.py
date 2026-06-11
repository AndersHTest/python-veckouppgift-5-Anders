from my_app.vowels import count_vowels

def test_no_vowels():
    assert count_vowels("qwrt") == 0
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0
    assert count_vowels("aOåÄöiöö") == 8
    assert count_vowels("aeiouyåäö") == 9
    assert count_vowels("Du är en stjärna") == 5