def preprocess_image_urls(image_urls):
        processed_urls = []
        for url in image_urls:
            if not url:
                continue
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url

            processed_urls.append(url)
        return filter_urls(processed_urls)


def remove_endline(data):
    return data.replace('\n', '')

def get_truth_meter(url):
    word = url.split("/")[-1]   # Split the URL by "/" and get the name
    word = word.split(".")[0]      # remove extension
    
    if word == "tom_ruling_pof":
        return "Pants On Fire"
    if word == "tom_ruling_falso":
        return "Falso"
    parts = word.split("-")     # Split word by -
    # Capitalize the first letter of each word and join them together
    return ' '.join([part.capitalize() for part in parts[1:]])

def filter_urls(urls):
     return urls[:4]