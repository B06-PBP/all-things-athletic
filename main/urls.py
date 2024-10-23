from django.urls import path
<<<<<<< HEAD
from main import views
from main.views import show_main, create_review, show_xml, show_json, show_xml_by_id, show_json_by_id
=======
from main.views import show_main
>>>>>>> origin/shafa

app_name = 'main'

urlpatterns = [
<<<<<<< HEAD
    path('admin/', admin.site.urls),
    path('', show_main, name='show_review'),
    path('create/', create_review, name='create_review'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
=======
    path('', show_main, name='show_main'),
>>>>>>> origin/shafa
]