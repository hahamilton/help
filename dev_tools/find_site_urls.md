# Finding Site URLs with Python
You may manage a website with more pages than you can keep track of (for example, a knowledge base or help center). The [Ultimate Website Sitemap Parser](https://github.com/berkmancenter/mediacloud-ultimate-sitemap-parser) module for Python can help with this by providing a list of every URL on your site.

In this example, the parser locates URLs by searching through a site's `sitemap.xml`. 

## Before You Begin
* Install a version of [Python](https://www.python.org/downloads/) that's compatible with the parser. According to the [documentation](https://github.com/berkmancenter/mediacloud-ultimate-sitemap-parser), you must have Python version 3.5 or later.
* If you're using Windows, add Python to your PATH.
* This solution uses a regular expression. If you're unfamiliar with regular expressions, check out https://regex101.com/.

## Create the Script
1. In a text editor, create a `.py` file (for example, `get_site_urls.py`) and save it.
2. Load the parser and regular expression modules.

		from usp.tree import sitemap_tree_for_homepage
		import re
3. Create a reference to your site.

		tree = sitemap_tree_for_homepage('https://mywebsite.com')
4. Start a for loop that looks for each page on your site.

		for page in tree.all_pages():
5. Use the following regular expression to only see the site's URLs (by default, the parser returns more data than just URLs).

		data = re.findall("(https:\/\/.+)", page)
6. Nest another for loop that lists only the URLs in the output.

		for url in data:
			print(url)
7. Run the script.
	Your site's URLs display in the output. 

> To make the output easier to share, consider adding to the script so that the output writes to a commonly used file format (such as CSV). 
