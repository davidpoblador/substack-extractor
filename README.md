# substrack-extractor
Crawls and extracts the text of a URL containing a Substack post

# Why
It's useful to be able to pipe those articles into your favorite LLM.

# Utilization
- Clone the repo
- Create Virtual Environment
```
python3 -m venv .venv
```
- Activate Virtual Environment
```
source .venv/bin/activate
```
- Install required packages
```
pip install -r requirements.txt
```
- Install browser drivers (required because we need to support JS)
```
playwright install
```
- Crawl
```
./substack_extractor.py "https://newsletter.keepitboring.com/p/the-evolution-of-digital-interactions"
```
