from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def health(request):
    db_ok = True
    try:
        connection.cursor().execute("SELECT 1")
    except Exception:
        db_ok = False
    return Response({"status": "ok", "service": "hello", "db": db_ok})