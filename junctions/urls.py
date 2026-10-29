
from django.urls import path
from .views import JunctionListCreateView, JunctionDetailView

urlpatterns = [
    path("", JunctionListCreateView.as_view(), name="junction-list-create"),
    path("<int:pk>/", JunctionDetailView.as_view(), name="junction-detail"),
]
