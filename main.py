import requests

def check_urls(urls):
    not_ok_urls = []
    for url in urls:
        response = requests.get(url)
        if response.status_code != 200:
            not_ok_urls.append(url)
    return not_ok_urls

urls = ["https://google.com", "https://httpstat.us/404", "https://example.com"]
not_ok_urls = check_urls(urls)
print("Неправильні URL:", not_ok_urls)