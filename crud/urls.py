from django.urls import path

from crud import views

urlpatterns = [
    path('excel/', views.ExcelAPIView.as_view()),
    path("data/", views.DataAPIView.as_view()),
    path("data/<int:pk>/", views.DataDetailAPIView.as_view()),
    path("data/restore/<int:pk>/", views.DataRestoreDetailAPIView),
]
