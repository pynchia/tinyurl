Feature: Searching for URLs
		As an anonymous user
		I want to search for a URL
		So that I can find out what is in the archive and their stats

	Scenario: search for a URL substring
		Given the set of URLs are added to the DB
			| url |
			| http://pythonhosted.org/behave/tutorial.html#python-step-implementations |
			| http://selenium-python.readthedocs.org/en/latest/getting-started.html |
			| http://stackoverflow.com/questions/tagged/django |
		When I go to the page "http://localhost:8081/searchurl/"
		And I post "python" in the search form
		Then the page will show "2" entries containing "python"

