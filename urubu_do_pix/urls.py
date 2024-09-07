from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from pix.application.rest.api import router as pix_router


api = NinjaAPI(
    title="DDD Django",
    description="Isso é apenas um teste aplicando DDD com Django"
)

@api.get("hc")
def health_check(request):
    return {"status": "ok"}

api.add_router("pix/", pix_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
