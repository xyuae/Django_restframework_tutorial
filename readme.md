## Authentication & Permissions
Currentlyh our API doesn't have any restricitons on who can edit or delete code snippets. We'd like to have
some more advanced behavior in order to make sure that:
- Code snippets are always associated with a creator.
- Only authenticated users may create snippets
- Only the creator of a snippet may update or delete it.
- Unauthenticated requests should have full read-only access.

### Adding information to our model
We are going to make a couple of changes to our Snippet model class. First, let's add a couple of fileds. One of those fields will be used to represent the user who created the code snippet. The other field will be used to store the highlighted HTML representation of the code.

### Meta options
Give your model metadata by using an inner class Meta

Model metadata is anything that is not a field, such as ordering options, database table name , or human-eadable singular and plural names. None are requried, and adding class Meta to a model is completely optional. 

## Associating Snippets with Users
Right now, if we created a code snippet, there would be no way of associating the user that created the snippet, with the snippet instance. The user isn't sent as part of the serialized representation, but is instead a property of the incoming request.

The way we deal with taht is by overriding a .perform_create() method on our snippet views, that allows us to modify how the instance save is managed, and handle any information that is implicit in the incoming request or requested URL.

## Creating an ednpoint for the highlighted snippets
Unlike all our other API endpoints, we don't want to use JSON, but isntead just present an HTML representation. There are two styles of HTML renderer provides by REST framework, one for dealing with HTML rendered using templates, the other for dealing with pre-rendered HTML. The second rednerer is the one we'd like to use for this endpoint.

The other thing we need to consider when creating the code highlight view is that there is no existing concrete generic view that we can use. We are not returning an object instance, but istead a property of an object instance.

Instead of using a concrete generivc view, we will use the base class for representing instances, and create our own .get() method. 
