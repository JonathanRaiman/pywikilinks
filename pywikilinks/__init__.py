"""
Utilities to parse and download thrift files
from the wiki-links corpus.

Usage
-----

To download and view mentions from the corpus:

```
import pywikilinks as wl
extracted_files = wl.download_and_extract(wl.get_urls(), "wiki-links")
for fname in extracted_files:
    for doc in wl.read_thrift_files(fname):
    	for mention in doc.mentions:
            print("CONTEXT: ", mention.context)
            print("ARTICLE: ", mention.wiki_url)
            print("")
```

"""
from .thrift_utils import read_thrift_files
from .download_utils import get_urls, download_and_extract

__all__ = ["read_thrift_files", "get_urls", "download_and_extract"]
