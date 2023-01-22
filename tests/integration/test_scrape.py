import pytest
from simplegoogle_scraper_python import scrapeGooGle_results
from simplegoogle_scraper_python.custom_exceptions import InvalidSearchqueryException


class Testscrapegoogle:
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
    def test_search(self,Query,Response):
        assert scrapeGooGle_results.__clean_pettern()==Response