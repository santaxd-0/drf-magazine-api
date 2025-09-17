from rest_framework.routers import SimpleRouter

from .views import ItemAPI, CategoryAPI, MagazinePublicAPI

router = SimpleRouter()
router.register(r"items", ItemAPI)
router.register(r"categories", CategoryAPI)
router.register(r"accesories", MagazinePublicAPI, basename="magazine-public-api")

urlpatterns = router.urls