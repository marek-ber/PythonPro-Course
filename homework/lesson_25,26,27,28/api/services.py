import time

from django.core.cache import cache


def get_complex_result():
    cache_key = 'complex_result'
    result = cache.get(cache_key)

    if result is None:
        time.sleep(3)
        result = {
            'result': 'Wynik skomplikowanych obliczeń',
            'source': 'Obliczone na żywo',
        }
        cache.set(cache_key, result, timeout=60)
    else:
        result['source'] = 'Pobrane z cache'

    return result
