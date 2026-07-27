from src.pipeline import retrieve_knowledge


def test_public_mode_can_access_public_knowledge() -> None:
    results = retrieve_knowledge(
        "How can systems save time and reduce decisions?",
        mode="public",
        retrieval_mode="keyword",
    )

    assert results
    assert all(result.visibility == "public" for result in results)


def test_public_mode_cannot_access_private_knowledge() -> None:
    results = retrieve_knowledge(
        "When is the fictional appointment?",
        mode="public",
        retrieval_mode="keyword",
    )

    assert results == []


def test_private_mode_can_access_private_knowledge() -> None:
    results = retrieve_knowledge(
        "When is the fictional appointment?",
        mode="private",
        retrieval_mode="keyword",
    )

    assert results
    assert any(result.visibility == "private" for result in results)