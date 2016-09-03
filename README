PyWikiLinks
-----------

Download a corpus of links to Wikipedia with their anchors tags
and surrounding context.

![multiple hypertext links from around the web shown in context pointing to Wikipedia articles](readme_images/wiki-link-figure.jpg)

This package lets you download and decode the wiki-links corpus. It
contains the necessary Python 3 code to decode the saved Apache Thrift
`WikiLinkItem` serialized in the dataset and read them.

### Example from wiki-links

Below are three mentions from the corpus that can be read from the
downloaded corpus. Note the presence of a link to Wikipedia (but
also freebase id) for the mentioned entity, along with "before" and
"after" context for the link to the entity along with the anchor text
found under "middle":

```bash
CONTEXT:  Context(middle=b'Graphic designers', right=b'typically don\xc3\xa2\xe2\x82\xac\xe2\x84\xa2t get involved in HTML and CSS coding. Front-end developers code designs in HTML, CSS, and JavaScript . The term \xc3\xa2\xe2\x82\xac\xc5\x93web designer\xc3\xa2\xe2\x82\xac\xef\xbf\xbd means different\xc3\x82\xc2\xa0\xc3\x82\xc2\xa0', left=b'Photoshop or Fireworks and leave the HTML and CSS to others. Or you may choose to do your own coding. Line Between Design and Implementation')
ARTICLE:  b'http://en.wikipedia.org/wiki/Graphic_designer'

CONTEXT:  Context(middle=b'JavaScript', right=b'. The term \xc3\xa2\xe2\x82\xac\xc5\x93web designer\xc3\xa2\xe2\x82\xac\xef\xbf\xbd means different\xc3\x82\xc2\xa0\xc3\x82\xc2\xa0 things to different people, but typically it implies taking on both the graphic designer role and at least', left=b'coding. Line Between Design and Implementation Graphic designers typically don\xc3\xa2\xe2\x82\xac\xe2\x84\xa2t get involved in HTML and CSS coding. Front-end developers code designs in HTML, CSS, and')
ARTICLE:  b'http://en.wikipedia.org/wiki/JavaScript'

CONTEXT:  Context(middle=b'Graphic design', right=b'and programming are very different skills, and relatively few people have a natural talent for both of them. Design is mostly a right-brain, creative activity,', left=b'approach for you depends on your interests and aptitudes, your partners, and the kinds of sites you expect to build. Advantages of the Designer/Coder Split')
ARTICLE:  b'http://en.wikipedia.org/wiki/Graphic_design'
```

As you may have noticed this data also contains many non ascii characters that show up as bytes in the text
above. Most often these are either unicode quotes or special punctuation that needs to be normalized.

### Installation

```bash
pip3 install pywikilinks
```

