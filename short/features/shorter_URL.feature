Feature: Shorter URL
		As an anonymous user
		I want to obtain a url shorter than the one I give
		So that I can save typing/space/use it on twitter

	Scenario: obtain a short URL for a new URL(web)
		Given "https://docs.djangoproject.com/en/dev/topics/testing/tools/" has no short url
		When I post "https://docs.djangoproject.com/en/dev/topics/testing/tools/" in the homepage form
		Then the page will show the short URL for "https://docs.djangoproject.com/en/dev/topics/testing/tools/"

