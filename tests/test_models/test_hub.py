def test_listing_pages_generator(default_hub):
    default_hub._max_pages = 1
    default_hub.max_page = 50
    urls = default_hub.listing_pages_generator()
    test_url = (
        "https://habr.com/kek/v2/articles/?hub=python&sort=all&fl=ru&hl=ru&page=1"
    )

    assert urls[0] == test_url
    assert len(urls) == 1
