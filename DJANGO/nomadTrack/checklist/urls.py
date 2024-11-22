from django.urls import path
from . import views

urlpatterns = [
    path("checklists/", views.checklists_index, name="checklists_index"),
    path(
        "checklists/<int:pk>/",
        views.ChecklistDetail.as_view(),
        name="checklists_detail",
    ),
    path("checklists/create/", views.ChecklistCreate.as_view(), name="checklists_create"),
    path(
        "checklists/<int:pk>/update/",
        views.ChecklistUpdate.as_view(),
        name="checklists_update",
    ),
    path(
        "checklists/<int:pk>/delete/",
        views.ChecklistDelete.as_view(),
        name="checklists_delete",
    ),
]
