from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)
"""


We will take a moment to examine exactly waht's happening here.
We are bulidling our view using GenericAPIView, and adding
in ListModeMixin and CreateModelMixin.

The base class provides the core functionality, and the mixin classs
provide the .list() and .create() actions. We're then explicitly binding the 
get and post methods to the appropriate actions. Simple enough stuff so far.

Again we are using the GenericAPIView class to provide the core 
functionality and adding in mixins to provide the .retrieve, update, and destroy actions

Using the mixin classes we've rewritten the views to use slightly less code than before, 
but we can go one step further. Rest framework provides a set of already mixed-in generic views that we can 
use to trim down our views.py module even more.


"""

"""
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from rest_framework import status
from snippets.serializers import SnippetSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView

class SnippetList(APIView):
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SnippetDetail(APIView):
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, foramt=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
    
"""
Note that because we want to be able to POST to this veiw from clients that won't have a 
CSRF token we need to mark the view as csrf_exempt. This isn't something that 
you'd normally want to do, and REST framework vies actually use more sensible behavior than this.
This should all feel very familiar - it is not a lot different from working with regular Django views.

Notice that we are no longer explicitly trying our requests or responses to a given content type.
request.data can handle incoming json requests, but it can also handle other formats. Similarly we are returning   

Adding optional format suffixes to our URLs
To take advantage of the fact that our respones are no longer hardwired to a single content type let's add support for format suffixes to 
our API endpoints. Using format suffixes gives us URLs

Browsability
Because the API chooses the content type of the response based on the client request, it will,
by default, return an HTML-formatted representation of the resource when that resource is requested by a web
browser. 
Having a web-browable API is a huge usability win, and makes develpiong and using your API much easier. It 
also dramatically lowers the barrier-to-entry for other developers wanting to inspect and work with your API.

## Class-based Views
We can also write our API views using class-based views, rather than function based views.
As we will see this is a powerful pattern taht allows us to reuse common funcitonality
"""
