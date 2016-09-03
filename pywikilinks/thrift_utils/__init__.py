from io import BytesIO

import thrift

from .ttransport import TBufferedTransport
from thrift.protocol import TBinaryProtocol
from .edu.umass.cs.iesl.wikilink.expanded.data import ttypes


def read_thrift_files(filepath):
    """
    Consume a thrift encoded file of type 'WikiLinkItem' and return the
    parsed datastructure as a Python object.

    Arguments:
        filepath : str, location of the file

    Returns:
        generator<ttypes.WikiLinkItem> : iterate over found structs.

    """
    transport = BytesIO(open(filepath, 'rb').read())
    transport.seek(0)
    transport = TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    while True:
        doc = ttypes.WikiLinkItem()
        try:
            doc.read(protocol)
            yield doc
        except EOFError:
                break


__all__ = ["read_thrift_files"]
