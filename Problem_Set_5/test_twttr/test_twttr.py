from twttr import shorten

def test_twttr():
    assert shorten("Hello This is CS50") =="Hll Ths s CS50"
    assert shorten("My name is Alie") =="My nm s l"
    assert shorten("lol") == "ll"
    assert shorten("MY NAME IS KHAN") =="MY NM S KHN"
    assert shorten("/bc/deed!?") =="/bc/dd!?"