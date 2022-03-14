from functions import are_there_duplicates, determine_outfit, smart_styler

def test_are_there_duplicates():

    assert are_there_duplicates(['a', 'b', 'c', 'b']) == True
    assert are_there_duplicates(['a', 'b', 'c']) == False

def test_determine_outfit():

    assert determine_outfit("cas", "cool", "fem") == "cas_cool_fem.jpg"

def test_smart_styler():

    assert callable(smart_styler)
