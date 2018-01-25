'''
The first thing we need to get started on our Web API is to provide a way
of serializing and deserializing the snippet isntances into representations such
as json. We can do this by declaring serializers that work very similar to Django
forms. Create a file in the snippets directory named serializers.py and add the following.
'''
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')



'''
Adding required permission to views
Now that code snippets are associated with users, we want to make sure
that only authenticated users are able to create, update and delete code snippets.

REST framework includes a number of permission classes that we can use to restrict who can access a given view.
In this case the one we are looking for is IsAuthenticatedOrReadOnly, which can



The field we have added is the untyped ReadOnlyField class, in contrast to the other typed fields,
such as CharField, BooleanField etc... The untyped ReadOnlyField is always read-only, and will be used for serialized representations,
but will not be used for updating model instance when they are deserialized. We could have also used CharField(read_only=Ture) here.

Adding required permission to views
Now that code snippets are associated with users, we want to 
make sure that only authentidcated users are able to craete, update and delete code snippets.

REST framework includes a number of permission clases that we can use to restrict who can access a given
view. In this case the one we are looking 


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new 'Snippet' instance, given the validated data
        """
        return Snippet.objects.create(**validated_data)

    def update(self, isntance, validated_data):
        """
        UPdate and return an existing 'Snippet' instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

'''

"""
The first part of the serializer class defines the fields that
get serialized/deserialized. The create() and update() methods define 
how fully fledged instances are created or modified when calling
serializer.save()

A serializer class is very similiar to a Django form class, and includes similar validatoin flags on the various fields, such as
required, max_length and default

The field flasg can also control how the serializer should be displayed in certain
circumstances, such as when rendering to HTML. The `{'base_template: 'textarea.html'}` flag above is equivalent to 
using `widget=widgets.Textarea` on a Django Form class. This is particularly useful for controling how the borwsable API should 
be displayed, as we will see later in the turorial. 
We can actually also save ourselve some time by using the ModelSerializer class, as we will see later, but for now we will 
keep our serializer definition explicit.

Our SnippetSerializer class is replicating a lot of information that's 
also contained inteh Snippet model. It would be nice if we could keep our code a bit more concise.

In the same way that Django provides both Form classes and ModelForm classes, REST 
framework includes both Serializer clases, and ModelSerilizer classes.

Let's look at refactoring our serializer using the ModelSerializer class. Open the 
file snippets/serializers.py again, and replace the SnippetSerializer claws with the follwoing. 

One nice property that serializers have is that you can inspect all the fields in a serializer instance,
by printing its represnetration. Open the Django shell.

Writing regular Django views using our Serializer
Let's see how we can write some API vies using our new Serializer class. For the moment we 
won't use any of REST framework's other features, we jsut write the views as regular Django views.


"""

