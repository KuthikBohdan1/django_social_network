from django.test import TestCase, RequestFactory
from main.models import Post, Profile, CustomUser

class ProfileListTest(TestCase):
    def test_ping(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    # def test_polls_list_ajax(self):
    #     factory = RequestFactory()
    #     request = factory.get()

class PostModelTest(TestCase):
    # def setUp(self) -> None:#
    #     return super().setUp()
    def create_profile(self):
        user = CustomUser.objects.create(
            email  = "owepofwefoewpfo@gmail.com",
            username = "nigerttdfdsfJJP876"
        )

        profile = Profile.objects.create(
            user = user
        )
        return profile

    def test_create_post(self):
        profile = self.create_profile()
        post = Post.objects.create(
            profile = profile,
            description = "sdsdsd",
        )
        self.assertEqual(post.description, "sdsdsd")
        self.assertEqual(post.profile.user.username, "nigerttdfdsfJJP876")
        self.assertEqual(post.profile.user.email, "owepofwefoewpfo@gmail.com")
        # self.assertTrue(post.)
    def test_str(self):
        profile =  self.create_profile()
        post = Post.objects.create(
            profile = profile,
            description = "new"
        )
        self.assertEqual(str(post), "new")