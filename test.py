import pytest

from billboard_scraper import clean_artist

clean_artist_cases = [
    #Test empty string returns itself
    ("", ""),
    #Test that a clean lowercase name returns itself
    ("steve", "steve"),
    #Test multiple clean lowercase words return itself
    ("justin bieber", "justin bieber"),
    #Test that an uppercase name returns lowercase of itself
    ("JUSTIN", "justin"),
    #Test that a list of all clutterers gets replaced by a space for each
    (".&featuring and +? x feat", "        "),
    #Test that a cluttered uppercase phrase is correctly cleaned
    ("Benji & Vedaant", "benji   vedaant"),
    #Test that capitalized "FEAT" is removed
    ("benji FEAT vedaant", "benji   vedaant")
]



@pytest.mark.parametrize("artist,cleaned_artist", clean_artist_cases)
def test_clean_artist(artist, cleaned_artist):
    assert clean_artist(artist) == cleaned_artist