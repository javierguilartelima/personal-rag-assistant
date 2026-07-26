from src.pipeline import retrieve_knowledge


def test_public_mode_can_access_public_knowledge() -> None:
    results = retrieve_knowledge(
        "How can systems save time and reduce decisions?",
        mode="public",
    )

    assert results
    assert all(result.visibility == "public" for result in results)


def test_public_mode_cannot_access_private_knowledge() -> None:
    results = retrieve_knowledge(
        "When is the fictional appointment?",
        mode="public",
    )

    assert results == []


def test_private_mode_can_access_private_knowledge() -> None:
    results = retrieve_knowledge(
        "When is the fictional appointment?",
        mode="private",
    )

    assert results
    assert any(result.visibility == "private" for result in results)