from ocdsdata import util
from ocdsdata.base import Source


class ColombiaSource(Source):
    publisher_name = 'Colombia'
    url = 'https://api.colombiacompra.gov.co'
    source_id = 'colombia'

    def gather_all_download_urls(self):
        if self.sample:
            return [{
                'url': 'https://api.colombiacompra.gov.co/releases/?page=1',
                'filename': 'sample.json',
                'data_type': 'release_package',
            }]

        r = util.get_url_request('https://api.colombiacompra.gov.co/releases/?page=1')
        if r[1]:
            raise Exception(r[1])
        r = r[0]
        data = r.json()
        total = data['links']['count']
        page = 1
        out = []
        # this limit is not passed to the API via the URL - but the API is currently returning 1000
        # results per page, so we hard code it
        limit = 1000
        while ((page-1)*limit) < total:
            out.append({
                'url': 'https://api.colombiacompra.gov.co/releases/?page=%d' % page,
                'filename': 'page%d.json' % page,
                'data_type': 'release_package',
            })
            page += 1
        return out
