from django.urls import path
from . import views

urlpatterns = [
    path("", views.Taskview.as_view(), name="task"),
    path('<int:pk>/update/', views.UpdateTaskview.as_view(), name='task-update'),
    path('<int:pk>/delete/', views.DeleteTaskview.as_view(), name='task-delete'),
    path('<int:id>/complete/', views.CompleteTask.as_view(), name='complete_task'),
    path('<int:id>/incomplete/', views.InCompleteTask.as_view(), name='Incomplete_task'),
    path('completed/', views.CompletedTasksView.as_view(), name='completed'),
    path("add_task/", views.AddTaskView.as_view(), name="add_task"),
        path('search_blog/', views.search_blog, name="search_blog"),
]