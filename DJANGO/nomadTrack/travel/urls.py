from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="home"),
    path("about/", views.about, name="about"),
    path("travel/", views.travels_index, name="index"),
    path("travel/<int:travel_id>/", views.travels_detail, name="detail"),
    path("travel/create/", views.TravelCreate.as_view(), name="travels_create"),
    path(
        "travel/<int:pk>/update/", views.TravelUpdate.as_view(), name="travels_update"
    ),
    path(
        "travel/<int:pk>/delete/", views.TravelDelete.as_view(), name="travels_delete"
    ),
    path(
        "travel/<int:travel_id>/add_checking/", views.add_checking, name="add_checking"
    ),
    # M:M
    path(
        "traels/<int:travel_id>/assoc_checklist/<int:checklist_id>/",
        views.assoc_checklist,
        name="assoc_checklist",
    ),
    path(
        "travel/<int:travel_id>/unassoc_checklist/<int:checklist_id>/",
        views.unassoc_checklist,
        name="unassoc_checklist",
    ),
     path(
        "list/", views.TravelList.as_view(), name="checklists_list"
    ),  
]
