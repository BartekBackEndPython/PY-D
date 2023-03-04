# 99% of this code is from Stackoverflow, I just changed variable name
import idlelib.colorizer as ic
import idlelib.percolator as ip
import re
from colors import *


def highlight(IDE_text):
    cdg = ic.ColorDelegator()
    cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat().pattern, re.S)
    cdg.idprog = re.compile(r'\s+(\w+)', re.S)

    cdg.tagdefs['MYGROUP'] = {'foreground': '#7F7F7F', 'background': '#FFFFFF'}

    # These five lines are optional. If omitted, default colours are used.
    cdg.tagdefs['COMMENT'] = {'foreground': '#FF0000', 'background': TEXT_EDITOR_COLOR}
    cdg.tagdefs['KEYWORD'] = {'foreground': '#007F00', 'background': TEXT_EDITOR_COLOR}
    cdg.tagdefs['BUILTIN'] = {'foreground': '#7F7F00', 'background': TEXT_EDITOR_COLOR}
    cdg.tagdefs['STRING'] = {'foreground': '#7F3F00', 'background': TEXT_EDITOR_COLOR}
    cdg.tagdefs['DEFINITION'] = {'foreground': '#007F7F', 'background': TEXT_EDITOR_COLOR}

    ip.Percolator(IDE_text).insertfilter(cdg)