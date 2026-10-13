from html import escape

from django.test import TestCase, override_settings
from django.urls import reverse


class HomeViewTests(TestCase):
    @override_settings(DEBUG=False)
    def test_missing_page_uses_custom_404_template(self):
        response = self.client.get("/missing-page/")

        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")
        self.assertContains(response, "Page not found", status_code=404)

    def test_home_page_displays_latest_post(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hope Without Certainty")
        self.assertNotContains(response, "The World Keeps Turning")

    def test_posts_page_uses_distinct_image_urls(self):
        response = self.client.get("/posts")

        self.assertEqual(response.status_code, 200)
        image_urls = [post["image"] for post in response.context["posts"]]
        self.assertEqual(len(image_urls), len(set(image_urls)))
        for image_url in image_urls:
            self.assertContains(response, f'src="{escape(image_url)}"')

    def test_post_details_displays_the_selected_post(self):
        posts_response = self.client.get("/posts")

        for post in posts_response.context["posts"]:
            with self.subTest(slug=post["slug"]):
                response = self.client.get(
                    reverse("post_details", kwargs={"slug": post["slug"]})
                )

                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.context["post"], post)
                self.assertContains(response, post["title"])
                self.assertContains(response, post["author"])
                self.assertContains(response, escape(post["image"]))
                self.assertContains(response, post["content"].strip().splitlines()[0].strip())

    @override_settings(DEBUG=False)
    def test_post_details_uses_custom_404_for_unknown_slug(self):
        response = self.client.get(reverse("post_details", kwargs={"slug": "unknown-post"}))

        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "404.html")
