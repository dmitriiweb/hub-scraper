def test_listing_pages_generator(default_scraper):
    default_scraper.hub._max_pages = 1
    default_scraper.hub.max_page = 50
    print(default_scraper.hub.max_page)
    urls = default_scraper.listing_pages_generator()
    test_url = (
        "https://habr.com/kek/v2/articles/?hub=python&sort=all&fl=ru&hl=ru&page=1"
    )

    assert urls[0] == test_url
    assert len(urls) == 1
