from src.models.groq_model import get_model

def test_get_model():
    model = get_model()

    assert model is not None