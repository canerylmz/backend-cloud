import base64
import io
import json
import logging

from PIL import Image

from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST


logger = logging.getLogger(__name__)


def _decode_image(data_url: str) -> Image.Image:
    encoded = data_url.split(",", 1)[-1]
    try:
        image_bytes = base64.b64decode(encoded)
        return Image.open(io.BytesIO(image_bytes)).convert("RGB")
    except Exception as exc:
        raise ValueError("Invalid image payload.") from exc


def _json_body(request: HttpRequest) -> dict:
    try:
        return json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError("Request body must be valid JSON.") from exc


@require_GET
def health(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"status": "backend-cloud is running"})


@csrf_exempt
@require_POST
def get_resolution(request: HttpRequest) -> JsonResponse:
    try:
        body = _json_body(request)
        image = _decode_image(body.get("image", ""))
    except ValueError as exc:
        return JsonResponse({"error": str(exc)}, status=400)

    width, height = image.size
    logger.info("resolution request received: width=%s height=%s", width, height)
    return JsonResponse(
        {
            "info": f"{width} x {height}",
            "resolution": {"width": width, "height": height},
        }
    )
