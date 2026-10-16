from app import greeting


def test_greeting_mentions_pipeline():
    assert "DevOps pipeline" in greeting()


def test_greeting_is_not_empty():
    assert greeting().strip() != ""
