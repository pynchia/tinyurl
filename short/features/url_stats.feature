Feature: Show URL stats
		As an anonymous user
		I want to obtain the stats of a specific short url
		So that I can monitor my resources

	Scenario: obtain the stats of an existing short URL
		Given the short URL id "5" exists
		When I ask for the stats of short URL "http://localhost:8081/r/5/"
		Then the page will show the stats of short URL id "5"

	Scenario: obtain the stats of a missing short URL
		Given the short URL id "666" is missing
		When I ask for the stats of short URL "http://localhost:8081/r/666/"
		Then the page will show an error about short URL id "666"

