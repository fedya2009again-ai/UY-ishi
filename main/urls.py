from django.urls import path
from .views import all_phone, detail, by_category, save_comment, update_comment, delete

urlpatterns = [
    path('', all_phone, name='all_phone'),
    path('detail/<int:phone_id>/', detail, name='detail'),
    path('category/<int:category_id>/', by_category, name='by_category'),
    path('comment/save/<int:phone_id>/', save_comment, name='save_comment'),
    path('comment/update/<int:comment_id>/', update_comment, name='update_comment'),
    path('comment/delete/<int:comment_id>/', delete, name='delete')
]