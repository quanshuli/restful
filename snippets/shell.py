# python manage.py shell

from rest_framework import serializers
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# create snippet and save
snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print("hello, world")\n')
snippet.save()

# serilize the snippet
serializer = SnippetSerializer(snippet)
serializers.data
# {'id': 2, 'title': '', 'code': 'print("hello, world")\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}

# render the data into json
content = JSONRenderer().render(serializer.data)
# content:
# b'{"id": 2, "title": "", "code": "print(\\"hello, world\\")\\n", "linenos": false, "language": "python", "style": "friendly"}'

# deserialize
import io
stream = io.BytesIO(content)
data = JSONParser.parse(stream)

