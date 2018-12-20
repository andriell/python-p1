import requests
import pprint

urls = ('https://www.myheadfirst.com/', 'https://www.oreilly.com/', 'https://twitter.com/')

for resp in [requests.get(url) for url in urls]:
    print(len(resp.content), resp.status_code, resp.url)

print()

for resp in (requests.get(url) for url in urls):
    print(len(resp.content), resp.status_code, resp.url)

print()


def gen_from_urls(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url
    return


for content_len, status_code, url in gen_from_urls(urls):
    print(content_len, status_code, url)

print()

resp = {url: size for size, _, url in gen_from_urls(urls)}
pprint.pprint(resp)