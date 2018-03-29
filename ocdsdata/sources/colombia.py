from ocdsdata.base import Fetcher
import requests


class ColombiaFetcher(Fetcher):
    publisher_name = 'Colombia'
    url = 'https://api.colombiacompra.gov.co'

    def __init__(self, base_dir, remove_dir=False, output_directory=None):
        super().__init__(base_dir, remove_dir=remove_dir, output_directory=output_directory)

    def gather_all_download_urls(self):
        url = 'https://api.colombiacompra.gov.co/releases/?page=1'
        r = requests.get(url)
        data = r.json()
        total = data['links']['count']
        page = 1
        out = []
        # this limit is not passed to the API via the URL - but the API is currently returning 1000 results per page, so we hard code it
        limit = 1000
        while ((page-1)*limit) < total:
            out.append([
                'https://api.colombiacompra.gov.co/releases/?page=%d' % page,
                'page%d.json' % page,
                'release_package',
                []
            ])
            page += 1
        return out
