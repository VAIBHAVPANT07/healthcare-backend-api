from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include


def home(request):
    return JsonResponse(
        {
            'message': 'Healthcare Backend API is running',
            'endpoints': {
                'admin': '/admin/',
                'auth': '/api/auth/',
                'patients': '/api/patients/',
                'doctors': '/api/doctors/',
                'mappings': '/api/mappings/',
            },
        }
    )

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/patients/', include('patients.urls')),
    path('api/doctors/', include('doctors.urls')),
    path('api/mappings/', include('mappings.urls')),
]
