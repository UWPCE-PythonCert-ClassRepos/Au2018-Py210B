#!/usr/bin/env python3

"""
Class: Python 210 B, Au2018
Exercise: Session 06, Mailroom Part 04
Student: Jason Jakubiak

A class-based system for rendering html.
"""

# This is the framework for the base class
class Element(object):
    """
    Abstract base class for rendering an Html element
    """
    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        self.attributes = kwargs
        self.contents = []
        if content is not None:
            self.contents = [content]


    def append(self, new_content):
        self.contents.append(new_content)


    def attrubutes(self):
        attrb = "".join([' {}="{}"'.format(key, val) 
                        for key, val in self.attributes.items()]
                        )
        return attrb


    def make_open_tag(self, cur_ind=""):
        open_tag = "<{}{}>".format(self.tag, self.attrubutes())
        return cur_ind + open_tag


    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write(self.make_open_tag())
        out_file.write("\n")
        for content in self.contents:
            try:
                content.render(out_file, cur_ind + self.indent)
            except AttributeError:
                out_file.write(cur_ind + self.indent)
                out_file.write(str(content) + "\n")
        out_file.write(cur_ind)
        out_file.write("</{}>\n".format(self.tag))

class OneLineTag(Element):
    tag = "Title"

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind)
        out_file.write(self.make_open_tag())
        for content in self.contents:
            out_file.write(str(content))
        out_file.write("</{}>\n".format(self.tag))

class Html(Element):
    tag = "html"

    def render(self, out_file, cur_ind=""):
        out_file.write("<!DOCTYPE html>\n")
        super().render(out_file, cur_ind)


class Body(Element):
    tag = "body"


class P(Element):
    tag = "p"


class Head(Element):
    tag = "head"


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):
    """
    Base class for tags without content
    To render horizontal rule and line breaks
    """

    def append(self, *args, **kwargs):
        raise TypeError("Adding content to a self closing tag not allowed")


    def render(self, out_file, cur_ind=""):
        open_tag = self.make_open_tag()
        out_file.write(cur_ind)
        out_file.write(open_tag.replace(">", " />"))
        out_file.write("\n")


class Hr(SelfClosingTag):
    tag = "hr"


class Br(SelfClosingTag):
    tag = "br"


class A(OneLineTag):
    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        super().__init__(content, **kwargs)


class Li(Element):
    tag = 'li'


class Ul(Element):
    tag = 'Ul'


class H(OneLineTag):
    tag = 'H'

    def __init__(self, level, content=None, **kwargs):
        self.tag = "h" + str(int(level))
        super().__init__(content, **kwargs)


class Meta(SelfClosingTag):
    tag = "meta"
