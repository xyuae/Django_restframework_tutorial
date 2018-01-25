"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.userViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing
# Additionally, we include login URLs for the browsable API
urlpatterns = [
    url(r'^', include('snippets.urls')),
    path('admin/', admin.site.urls),
]

"""
REST framework introduces a Request object that extends the regular
HttpRequest, and provides more flexible request parsing. The core functionality of the
Request object is the request.data attribute, which is similar to request.POST

Response objects
REST framework also introduces a Response object, which is a type of TempalteResposne
that takes unrednered content and uses content negoitaitno to detiemrine the cforect content type
type to return to the client
return Response(data)

Wrapping API views
REST framework provides two wrappers you can use to write API views
These wrapers provide a few bits of functionality such as making sure you recieve Request isntances in your 
view, and adding context to Response objects so taht content negotaiton cvan be performed.
The wrappers also provide behaviour such as returning 405 Method not Allowed responses when appropriate, and handling any ParseError
exception that occurs when accessing request.data with malformed input.

Pulling it all together
Okay, let's go ahead and start using these new components to write a few views.
We don't need our JSONResponse class in views.py any more, so go ahead and delete that
"""


