import requests
import bs4
import logging

# Perform Google Image Search using a query and get image URLs
def fetch_image_urls(keyword):
    try:
        url = 'https://www.google.com/search?hl=en&tbm=isch&q=' + keyword
        request_result = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = bs4.BeautifulSoup(request_result.text, "html.parser")

        image_tags = soup.find_all('img')
        image_urls = []
        for img in image_tags:
            img_url = img.get('src')
            if img_url and img_url.startswith('http'):
                larger_img_url = img.get('data-src')
                if larger_img_url:
                    image_urls.append(larger_img_url)
                else:
                    image_urls.append(img_url)
                if len(image_urls) == 8:
                    break
        return image_urls
    except Exception as e:
        logging.error(f"Error during image extraction: {e}")
        return []
