# 3a + 3b
# Ett testfall räcker inte för att testa funktionen - föreslå fler testfall,
# som täcker in alla olika möjligheter för count_vowels.
# Returnerar ett heltal med antalet vokaler som finns i ordet (aeiouyåäö)


def count_vowels(word):

    vokaler = "aouåeiyäöAOUÅEIYÄÖ"
    antal_vokaler = 0

    for i in word:
        if i in vokaler:
            antal_vokaler += 1
    return antal_vokaler