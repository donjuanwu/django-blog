"""

Test usage:
python manage.py test blogging

"""

from blogging.models import Post
from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class PostTestCase(TestCase):
    fixtures = ['blogging_test_fixture.json', ]

    def setup(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)