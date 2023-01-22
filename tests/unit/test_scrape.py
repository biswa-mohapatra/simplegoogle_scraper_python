import pytest
from scrape_google import scrape_google
from scrape_google.custom_exceptions import InvalidSearchqueryException

good_response = [
    ("", '<div class="yuRUbf"><a href="(.*?)" data-jsarwt=".*?" '
        'data-usg=".*?" data-ved=".*?"><br><h3 class="LC20lb MBeuO DKV0Md">(.*?)</h3>.*?'
        '<div class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf" style="-webkit-line-clamp:2">'
        "<span>(.*?)</span></div>"),
    ("", '<div class="yuRUbf"><a href="(.*?)" data-jsarwt=".*?" '
        'data-usg=".*?" data-ved=".*?"><br><h3 class="LC20lb MBeuO DKV0Md">(.*?)</h3>.*?'
        '<div class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf" style="-webkit-line-clamp:2">'
        "<span>(.*?)</span></div>"),
    ("", '<div class="yuRUbf"><a href="(.*?)" data-jsarwt=".*?" '
        'data-usg=".*?" data-ved=".*?"><br><h3 class="LC20lb MBeuO DKV0Md">(.*?)</h3>.*?'
        '<div class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf" style="-webkit-line-clamp:2">'
        "<span>(.*?)</span></div>")
]

@pytest.mark.parametrize("Query,Response",good_response)
def test_search(Query,Response):
    assert scrape_google.clean_pettern()==Response