"""
    pygments.styles.ansi
    ~~~~~~~~~~~~~~~~~~~~~~~

    pygments version of the ansi color scheme using
    terminal colors

    :copyright: Copyright 2006-2021 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import (
    Keyword,
    Name,
    Comment,
    String,
    Error,
    Number,
    Operator,
    Generic,
)


class AnsiStyle(Style):
    """
    Pygments version of the ansi colorscheme.
    """

    background_color = "ansiblack"
    highlight_color = "ansibrightblack"

    styles = {
        Comment:            "ansigreen",
        Comment.PreProc:    "ansicyan",
        Comment.Special:    "bold ansiyellow",
        Keyword:            "bold ansiblue",
        Keyword.Pseudo:     "nobold ansiblue",
        Keyword.Type:       "nobold ansiblue",
        Operator:           "ansiblue",
        Operator.Word:      "bold ansiblue",
        String:             "ansigreen",
        String.Escape:      "ansibrightyellow",
        String.Doc:         "ansigreen",
        String.Interpol:    "ansigreen",
        String.Escape:      "ansiyellow",
        String.Regex:       "ansiyellow",
        String.Symbol:      "ansigreen",
        String.Other:       "ansigreen",
        Number:             "ansimagenta",
        Name.Builtin:       "ansiblue",
        Name.Variable:      "ansiblue",
        Name.Constant:      "ansimagenta",
        Name.Class:         "ansicyan",
        Name.Function:      "ansicyan",
        Name.Namespace:     "ansicyan",
        Name.Exception:     "ansired",
        Name.Tag:           "ansicyan",
        Name.Attribute:     "ansiyellow",
        Name.Decorator:     "ansibrightyellow",
        Generic.Heading:    "bold ansigray",
        Generic.Subheading: "underline ansigray",
        Generic.Deleted:    "bg:ansired ansiblack",
        Generic.Inserted:   "bg:ansigreen ansiblack",
        Generic.Error:      "ansired",
        Generic.Emph:       "italic",
        Generic.Strong:     "bold",
        Generic.Prompt:     "ansibrightblack",
        Generic.Output:     "ansiwhite",
        Generic.Traceback:  "ansired",
        Error:              "bg:ansired ansiblack",
    }
