from django.urls import path
from . import views
urlpatterns = [
   path('insert_employee/',views.insert_employee, name='insert_employee'),
   path('view_employee/', views.view_employee,  name = 'view_employee'),
   path('insert_student/',views.insert_student, name='insert_student'),
   path('view_student/', views.view_student,  name = 'view_student'),
   path('delete_employee/<int:pk>',
        views.delete_employee,
              name='delete_employee'),
   path('delete_student/<int:pk>',
        views.delete_student,
              name='delete_student'),

   path('update_employee/<int:pk>',
        views.update_employee,
              name='update_employee'),
   path('update_student/<int:pk>',
        views.update_student,
              name='update_student'),
   path('insert_faculty/',views.insert_faculty, name='insert_faculty'),
   path('view_faculty/', views.view_faculty, name = 'view_faculty'),



]
