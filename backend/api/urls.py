from rest_framework.routers import DefaultRouter
from .views import usersViewSet, inventory_logViewSet, inventoryViewSet, finances_logViewSet, financesViewSet, documentsViewSet

router = DefaultRouter()
router.register(r'users', usersViewSet)
router.register(r'inventory', inventoryViewSet)
router.register(r'inventory_log', inventory_logViewSet)
router.register(r'finances', financesViewSet)
router.register(r'finances_log', finances_logViewSet)
router.register(r'documents', documentsViewSet)

urlpatterns = router.urls