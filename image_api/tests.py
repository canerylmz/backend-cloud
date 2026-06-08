import base64
import io

from PIL import Image


def _sample_data_url() -> str:
    image = Image.new("RGB", (3, 2), color=(20, 120, 240))
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{encoded}"


def test_get_resolution(client):
    response = client.post(
        "/get/resolution",
        data={"image": _sample_data_url()},
        content_type="application/json",
    )

    assert response.status_code == 200
    assert response.json()["resolution"] == {"width": 3, "height": 2}
