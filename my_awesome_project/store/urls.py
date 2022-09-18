from django.urls import path
from .views import all_categories

app_name = "store"
urlpatterns = [
    path("", all_categories, name="all_categories"),
]