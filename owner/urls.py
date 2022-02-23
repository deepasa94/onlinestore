from django.urls import path
from owner import views
urlpatterns=[
    path('book/add',views.AddBookView.as_view(),name="addbook"),
    path('employee/add',views.AddEmployeeView.as_view(),name="addemployee"),
    path('book/all',views.BookListView.as_view(),name="booklist"),
    path('book/<int:id>',views.BookDetailView.as_view(),name="bookdetail"),
    path('book/change/<int:id>',views.BookChange.as_view(),name="bookedit"),
    path('book/remove/<int:id>',views.BookDeleteView.as_view(),name="bookdelete"),
    path('employee/all',views.EmployeeListView.as_view(),name="emplist"),
    path('employee/<int:id>',views.EmployeeDetailView.as_view(),name="empdetail"),
    path('employee/change/<int:id>',views.EmployeeEditView.as_view(),name="empedit")

]