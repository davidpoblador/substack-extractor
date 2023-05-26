#!/usr/bin/env python


import sys
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


def extract_substack_article(url):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        # Wait for the article content to load, you may need to adjust the timing here
        page.wait_for_selector('article.post')
        # Extract the article content
        article_content = page.inner_html('article.post')
        browser.close()
        return article_content


def main():
    if len(sys.argv) < 2:
        print("Please provide the Substack article URL as a parameter.")
        return

    url = sys.argv[1]
    soup = BeautifulSoup(extract_substack_article(url), 'html.parser')

    header = soup.find('div', {'class': 'post-header'})
    title = header.find('h1', {'class': 'post-title'}).text
    subtitle = header.find('h3', {'class': 'subtitle'}).text

    body = soup.find('div', {'class': 'body'})

    output = "Title: " + title + "\n"
    output += "Subtitle: " + subtitle + "\n"
    output += "\n"

    for item in body.find_all(['p', 'h2']):
        if item.name == "p":
            output += item.text + "\n"
            continue

        if item.name == "h2":
            output += "\n" + item.text + "\n"
            continue

    print(output)


if __name__ == "__main__":
    main()
