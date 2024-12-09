from ghost_admin import GhostAdmin

ga = GhostAdmin()


def test_get_tiers():
    r = ga.get_tiers()
    assert isinstance(r, dict)
    assert isinstance(r["tiers"], list)


def test_post_posts_lexical():
    posts = [
        {
            "title": "My lexical test post",
            "lexical": '{"root":{"children":[{"children":[{"detail":0,"format":0,"mode":"normal","style":"","text":"Hello, beautiful world! 👋","type":"extended-text","version":1}],"direction":"ltr","format":"","indent":0,"type":"paragraph","version":1}],"direction":"ltr","format":"","indent":0,"type":"root","version":1}}',
            "status": "published",
        }
    ]
    r = ga.post_posts(posts=posts)
    assert r == "Success!"


def test_post_posts_html():
    posts = [
        {
            "title": "My html test posts",
            "html": "<p>My post content. Work in progress...</p>",
            "status": "published",
        }
    ]
    r = ga.post_posts(source="html", posts=posts)
    assert r == "Success!"


def test_post_post_html():
    post = {
        "title": "My html test post",
        "html": "<p>My post content. Work in progress...</p>",
        "status": "published",
    }
    r = ga.post_post(source="html", post=post)
    assert r == "Success!"
