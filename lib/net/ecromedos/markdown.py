# -*- coding: UTF-8 -*-
#
# Desc:    This file is part of the ecromedos Document Preparation System
# Author:  Tobias Koch <tobias@tobijk.de>
# License: MIT
# URL:     http://www.ecromedos.net
#

import re
from lxml import etree
import com.lepture.mistune as mistune
from net.ecromedos.configreader import ECMDSConfigReader
from net.ecromedos.dtdresolver  import ECMDSDTDResolver

class ECMLRendererError(Exception):
    pass

class ECMLRenderer(mistune.Renderer):

    def __init__(self):
        mistune.Renderer.__init__(self)
        self.section_level = 0
        self.footnotes_map = {}
    #end if

    # BLOCK ELEMENTS

    def block_code(self, code, language=None):
        if language == None:
            language = "text"

        return """<listing><code syntax="%(lang)s" strip="yes"
                tabspaces="4">%(code)s</code></listing>""" % {
            "lang": language,
            "code": mistune.escape(code)
        }
    #end function

    def block_quote(self, text):
        return "<blockquote>%s</blockquote>" % text
    #end function

    def block_html(self, ecml):
        return ecml
    #end function

    def header(self, text, level, raw=None):
        retval = ""

        diff = level - self.section_level

        if diff > 1:
            msg = "Heading '%s' skips a section level." % text
            raise ECMLRendererError(msg)
        else:
            sign = int(diff > 0) - int(diff < 0)
            diff = sign * diff

            # we close until we reach the new level
            if sign <= 0:
                for i in range(diff+1):
                    retval += "</section>"
            #end if
        #end if

        retval += '<section level="%d">' % level
        retval += '<title>%s</title>'    % text

        self.section_level = level
        return retval
    #end function

    def hrule(self):
        return ""
    #end function

    def list(self, body, ordered=True):
        if ordered:
            return "<ol>%s</ol>" % body
        else:
            return "<ul>%s</ul>" % body
    #end function

    def list_item(self, text):
        return "<li>%s</li>" % text
    #end function

    def paragraph(self, text):
        return "<p>%s</p>" % text
    #end function

    def table(self, header, body):
        return """\
        <table print-width="100%%" screen-width="800px" align="center" frame="top,left,right,bottom">
            <thead>
                %s
            </thead>
            <tbody>
                %s
            </tbody>
        </table>""" % (header, body)
    #end function

    def table_row(self, content):
        return '<tr valign="top">%s</tr>' % content
    #end function

    def table_cell(self, content, **flags):
        align = flags['align']
        if not align:
            return '<td>%s</td>' % content
        return '<td align="%s">%s</td>' % (align, content)
    #end function

    # INLINE ELEMENTS

    def autolink(self, link, is_email=False):
        text = link = mistune.escape(link)
        if is_email:
            link = "mailto:%s" % link
        return '<link url="%s">%s</link>' % (link, link)
    #end function

    def codespan(self, text):
        return "<tt>%s</tt>" % mistune.escape(text)
    #end function

    def double_emphasis(self, text):
        return "<b>%s</b>" % text
    #end function

    def emphasis(self, text):
        return "<i>%s</i>" % text
    #end function

    def image(self, src, title, text):
        src  = mistune.escape_link(src)
        text = mistune.escape(text, quote=True)

        if title:
            title = mistune.escape(title, quote=True)
            ecml = """\
                <figure align="center">
                    <caption>%s</caption>
                    <img src="%s" print-width="100%%" screen-width="800px"/>
                </figure>
            """ % (title, src)
        else:
            ecml = """\
                <figure align="center">
                    <img src="%s" print-width="100%%" screen-width="800px"/>
                </figure>
            """ % (src,)
        #end if

        return ecml
    #end function

    def linebreak(self):
        return "<br/>"
    #end function

    def newline(self):
        return ""
    #end function

    def footnote_ref(self, key, index):
        return '<footnote-ref idref="%s"/>' % mistune.escape(key)
    #end function

    def footnote_item(self, key, text):
        self.footnotes_map[key] = text
        return ""
    #end function

    def footnotes(self, text):
        return ""
    #end function

    def link(self, link, title, text):
        link = mistune.escape_link(link)
        return '<link url="%s">%s</a>' % (link, text)
    #end function

    def strikethrough(self, text):
        return text
    #end function

    def text(self, text):
        return mistune.escape(text)
    #end function

    def inline_html(self, ecml):
        return ecml
    #end function

#end class

class MarkdownConverterError(Exception):
    pass

class MarkdownConverter(ECMDSDTDResolver):

    DOCUMENT_TEMPLATE = """\
<!DOCTYPE report SYSTEM "http://www.ecromedos.net/dtd/3.0/ecromedos.dtd">
<%(document_type)s bcor="%(bcor)s" div="%(div)s" lang="%(lang)s" papersize="%(papersize)s" parskip="%(parskip)s" secnumdepth="%(secnumdepth)s" secsplitdepth="%(secsplitdepth)s">

    %(header)s

    <make-toc depth="%(tocdepth)s" lof="%(have_lof)s" lot="%(have_lot)s" lol="%(have_lol)s"/>

    %(contents)s

</%(document_type)s>
    """

    def __init__(self, options):
        ECMDSConfigReader.__init__(self)
        ECMDSDTDResolver. __init__(self)

        self.config = {
            "document_type": "report",
            "bcor": "0cm",
            "div": "16",
            "lang": "en_US",
            "papersize": "a4",
            "parskip": "half",
            "secnumdepth": "2",
            "secsplitdepth": "1",
            "header": "",
            "tocdepth": "5",
            "have_lof": "no",
            "have_lot": "no",
            "have_lol": "no",
            "contents": ""
        }

        self.config.update(options)
    #end function

    def convert(self, string):
        # initial conversion happening here
        renderer  = ECMLRenderer()
        markdown  = mistune.Markdown(renderer=renderer)
        contents  = markdown(self.parse_preamble(string))
        header    = self.generate_header(self.config)
        footnotes = renderer.footnotes_map

        # close all open sections
        for i in range(renderer.section_level):
            contents += "</section>"

        self.config["header"] = header
        self.config["contents"] = contents
        self.config["footnotes"] = footnotes

        contents = MarkdownConverter.DOCUMENT_TEMPLATE % self.config

        # parse XML to do post-processing
        parser = etree.XMLParser(remove_blank_text=True)
        tree   = etree.fromstring(contents, parser=parser)

        # fix footnotes, tables, section names...
        tree = self.post_process(tree)

        # return pretty-printed result
        return etree.tostring(tree, pretty_print=True, encoding="unicode")
    #end function

    def parse_preamble(self, string):
        config = {}

        m = re.match(r"\A---+\s*?$.*?^---+\s*?$", string, flags=re.MULTILINE|re.DOTALL)

        if not m:
            return string

        m = m.group(0)

        for line in m.strip("-").splitlines():
            if not line.strip():
                continue

            try:
                k, v = [x.strip() for x in line.split(":", 1)]
                k = k.replace("-", "_")
            except:
                continue

            if k != "author":
                config[k] = v
            else:
                config.setdefault(k, []).append(v)
            #end if
        #end for

        self.validate_config(config)
        self.config.update(config)

        return string[len(m):]
    #end function

    def generate_header(self, config):
        header_elements = [
            "subject",
            "title",
            "subtitle",
            "author",
            "date",
            "publisher",
            "dedication"
        ]

        header = ""

        for element_name in header_elements:
            if element_name == "title":
                header += "<title>%s</title>\n" % config.get("title", "")
            elif element_name == "author":
                for author in config.get("author", []):
                    header += "<author>%s</author>\n" % author
            else:
                element_text = config.get(element_name, "")
                if element_text:
                    header += "<%s>%s</%s>\n" % \
                            (element_name, element_text , element_name)
                #end if
            #end ifs
        #end for

        return "<head>\n%s</head>" % header
    #end function

    def validate_config(self, config):
        pass
    #end function

    def post_process(self, root_node):

        node = root_node

        while node is not None:
            if node.tag == "footnote-ref":
                node = self.__fix_footnote(node)
            elif node.tag == "section":
                node = self.__fix_section(node)
            elif node.tag == "table":
                node = self.__fix_table(node)
            elif node.tag == "thead":
                node = self.__fix_thead(node)
            elif node.tag == "tbody":
                node = self.__fix_tbody(node)
            elif node.tag == "figure":
                node = self.__fix_figure(node)
            #end if

            if len(node) != 0:
                node = node[0]
                continue

            while node is not None:
                following_sibling = node.getnext()

                if following_sibling is not None:
                    node = following_sibling
                    break

                node = node.getparent()
            #end while
        #end while

        return root_node
    #end function

    # PRIVATE

    def __fix_footnote(self, ref_node):
        footnotes    = self.config["footnotes"]
        footnote_ref = ref_node.get("idref", None)
        footnote_def = footnotes.get(footnote_ref, None)

        if footnote_def == None:
            raise MarkdownConverterError(
                "Unresolved footnote reference '%s'" % footnote_ref)
        #end if

        try:
            footnote = etree.fromstring(footnote_def)
        except etree.XMLSyntaxError as e:
            raise MarkdownConverterError(
                "Footnote '%s' is not a valid XML fragment." % footnote_ref)
        #end try

        if footnote.tag != "p":
            raise MarkdownConverterError(
                "Footnote '%s' is an invalid block element." % footnote_ref)
        #end if

        footnote.tag  = "footnote"
        footnote.tail = ref_node.tail
        ref_node.getparent().replace(ref_node, footnote)

        return footnote
    #end function

    def __fix_section(self, section_node):
        document_type = self.config["document_type"]

        if document_type == "article":
            section_names = ["section", "subsection", "subsubsection", "minisection"]
        else:
            section_names = ["chapter", "section", "subsection", "subsubsection", "minisection"]
        #end if

        level = int(section_node.attrib["level"]) - 1
        section_node.tag = section_names[level]
        del section_node.attrib["level"]

        return section_node
    #end function

    def __fix_table(self, table_node):
        if table_node.xpath("colgroup"):
            return table_node

        header_cells = table_node.xpath("thead/tr/td")

        width = 100 / len(header_cells)
        colgroup_node = etree.Element("colgroup")

        for cell in header_cells:
            col_node = etree.Element("col")
            col_node.attrib["width"] = str(width) + "%"
            colgroup_node.append(col_node)
        #end for

        table_node.insert(0, colgroup_node)

        return table_node
    #end function

    def __fix_thead(self, thead_node):
        header_row = thead_node.xpath("tr")[0]
        header_row.tag = "th"
        thead_node.getparent().replace(thead_node, header_row)
        return header_row
    #end function

    def __fix_tbody(self, tbody_node):
        table_node = tbody_node.getparent()
        body_rows  = tbody_node.xpath("tr")

        for row in body_rows:
            table_node.append(row)

        table_node.remove(tbody_node)

        return body_rows[0]
    #end function

    def __fix_figure(self, figure_node):
        section_elements = {
            "chapter": 1,
            "section": 1,
            "subsection": 1,
            "subsubsection": 1,
            "minisection": 1,
            "preface": 1,
            "abstract": 1,
            "appendix": 1
        }

        parent      = figure_node.getparent()
        grandparent = parent.getparent()

        if not section_elements.get(grandparent.tag, None):
            raise MarkdownConverterError("The parent or grandparent of image "\
                "'%s' is not a sectioning element." % figure_node.get("alt"))

        if etree.tostring(parent, method="text", encoding="unicode").strip() == "":
            grandparent.replace(parent, figure_node)
        else:
            figure_node.attrib["align"] = "left"
            img_node = figure_node.xpath("img")[0]
            img_node.attrib["print-width"] = "50%"
            img_node.attrib["screen-width"] = "400px"
        #end if

        return figure_node
    #end function

#end class
