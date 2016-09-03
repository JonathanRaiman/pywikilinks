"""
Utilities for using bash wget and gunzip
to download and collect files along with
the file-list and url-list of wiki-links.
"""
import subprocess

from os.path import join, exists
from os import makedirs, stat

def execute_bash(command, verbose=True):
    """
    Executes bash command, prints output and throws an exception on failure.
    (Warning: this runs shell commands)
    """
    process = subprocess.Popen(command,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               universal_newlines=True)
    for line in process.stdout:
        if verbose:
            print(line, end='', flush=True)
    process.wait()
    assert process.returncode == 0


def get_urls():
    """
    Generate urls to all wiki-links
    files (totaling ~1.8GB of gzipped data.
    ~5.93GB decompressed) listed at this address:

    http://www.iesl.cs.umass.edu/data/wiki-links

    Returns:
        list<tuple<str,str>> : urls and filenames
    """
    base_url = (
        "http://iesl.cs.umass.edu/downloads/wiki-link/context-only/"
    )
    urls = []
    for i in range(1, 110):
        name = "%03d.gz" % (i,)
        url = base_url + name
        urls.append((url, name))
    return urls


def download_and_extract(urls, path, verbose=True):
    """
    Download the files specified under `urls` into a folder `path` and run
    `gunzip` on the files. Checks if the files exists before downloading
    and creates the folder `path` if it is missing.

    Arguments:
        urls : list<str>, location of the files to download
        path : str, path to directory where files should be kept
        verbose : bool, defaults to True. print message when a file
                  was already downloaded and isn't re-downloaded.
                  also shows wget and gunzip output.

    Returns:
        list<str> : absolute filenames of downloaded files.
    """
    makedirs(path, exist_ok=True)
    extracted_files = []
    downloads = []
    unzip_commands = []

    for url, name in urls:
        dest = join(path, name)
        unzipped = join(path, name.rstrip(".gz"))
        extracted_files.append(unzipped)

        if exists(unzipped) and stat(unzipped).st_size > 1000:
            if verbose:
                print("Already downloaded and extracted %r." % (unzipped,))
            continue

        if not (exists(dest) and stat(dest).st_size > 1000):
            execute_bash("wget -O %s %s" % (dest, url), verbose=verbose)

        execute_bash("gunzip %s" % (dest,), verbose=verbose)

    return extracted_files
