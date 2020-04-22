from usp.tree import sitemap_tree_for_homepage
import re

tree = sitemap_tree_for_homepage('https://documents.polycom.com/')

# pdl_links = []

# with open('urls.csv', 'w', newline='') as f:
#	thewriter = csv.writer(f)

for page in tree.all_pages():
	data = re.findall("(https:\/\/.+)", page)
	for url in data:
		print(url)
