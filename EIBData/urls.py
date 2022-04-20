from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views as cv

router = DefaultRouter()
router.register(r"countries", cv.CountrySerializerViewSet)
router.register(r"sectors", cv.SectorSerializerViewSet)
router.register(r"loans", cv.FinancedProjectSerializerViewSet,basename='loans')

urlpatterns = [
    path("", include(router.urls))
]
