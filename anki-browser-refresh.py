# -*- coding: utf-8 -*-

"""
Anki Add-on: Refresh browser list

Refreshes browser view and sets card sorting to "creation time"
(e.g. to show newly added cards since last search)

Copyright: (c) Glutanimate 2016
License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
"""
 
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QKeySequence
from anki.hooks import addHook

def refreshBrowserView(self):
    self.onSearch(reset=True)
    if u'noteCrt' in self.model.activeCols:
        col_index = self.model.activeCols.index(u'noteCrt')
        self.onSortChanged(col_index, True)
    self.form.tableView.selectRow(0)

def setupMenu(self):
    menu = self.form.menuEdit
    menu.addSeparator()
    a = menu.addAction('Refresh View')
    a.setShortcut(QKeySequence("F5"))
    self.connect(a, SIGNAL("triggered()"), lambda b=self: refreshBrowserView(b))


addHook("browser.setupMenus", setupMenu)