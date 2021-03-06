# Add-on descriptions

<!-- MarkdownTOC -->

- [Published on Ankiweb](#published-on-ankiweb)
    - [anki-browser-search-hotkeys.py](#anki-browser-search-hotkeyspy)
    - [anki-browser-search-modifiers.py](#anki-browser-search-modifierspy)
    - [anki-browser-create-duplicate.py](#anki-browser-create-duplicatepy)
    - [anki-browser-lookup.py](#anki-browser-lookuppy)
    - [anki-editor-field-navigation.py](#anki-editor-field-navigationpy)
    - [anki-editor-tag-hotkeys.py](#anki-editor-tag-hotkeyspy)
    - [anki-editor-autocomplete-whitelist.py](#anki-editor-autocomplete-whitelistpy)
    - [anki-editor-restore-fields.py](#anki-editor-restore-fieldspy)
    - [anki-browser-refresh.py](#anki-browser-refreshpy)
    - [anki-browser-replace-tag.py](#anki-browser-replace-tagpy)
    - [anki-browser-create-filtered-deck.py](#anki-browser-create-filtered-deckpy)
    - [anki-overview-deck-switcher.py](#anki-overview-deck-switcherpy)
    - [anki-reviewer-puppy-reinforcement.py](#anki-reviewer-puppy-reinforcementpy)
    - [anki-browser-advanced-preview.py](#anki-browser-advanced-previewpy)
    - [anki-browser-batch-edit.py](#anki-browser-batch-editpy)
    - [anki-reviewer-card-stats.py](#anki-reviewer-card-statspy)
    - [anki-editor-custom-tagedit.py](#anki-editor-custom-tageditpy)
    - [anki-overview-heatmap.py](#anki-overview-heatmappy)
- [Yet to be published](#yet-to-be-published)
- [The rest](#the-rest)

<!-- /MarkdownTOC -->


## Published on Ankiweb

### anki-browser-search-hotkeys.py

**Browser search hotkeys**

**Allows you to set up hotkeys for searches in the browser**

Hotkeys follow this scheme: Ctrl+S –> (Modifier) + Key. I.e.: hit Ctrl+S to start the key sequence, let go of Ctrl+S, then hit the key assigned to  your search, plus an optional modifier.

You can use keyboard modifiers to control whether to add a term to the  search, negate it, remove it, or do something else. This follows the same  logic as the default behaviour in Anki when clicking on a search term in the sidebar.

New hotkeys can be defined in the source file by editing the `search_shortcuts` dictionary. Make sure to follow the existing syntax.

For instance, line 2 in the default `search_shortcuts` dict assigns the search
'added 1' (cards added today) to 'T'. This defines the following key sequences
in the browser:

    Ctrl+S -> T             replace search field with 'added:1'
    Ctrl+S -> Ctrl+T        add 'added:1' to existing search
    Ctrl+S -> Alt+T:        replace search field with '-added:1'
    Ctrl+S -> Ctrl+Alt+T:   add '-added:1' to existing search
    Ctrl+S -> Shift+T:      add 'or added:1' to existing search

The following keys are assigned by default:

    'A': {'search': ''},            # All together now
    'T': {'search': 'added:1'},     # Today
    'V': {'search': 'rated:1'},     # Viewed
    'G': {'search': 'rated:1:1'},   # aGain today
    'F': {'search': 'card:1'},      # First
    'C': {'search': 'deck:current'},# Current
    'N': {'search': 'is:new'},      # New
    'L': {'search': 'is:learn'},    # Learn
    'R': {'search': 'is:review'},   # Review
    'D': {'search': 'is:due'},      # Due
    'S': {'search': 'is:suspended'},# Suspended
    'B': {'search': 'is:buried'},   # Buried
    'M': {'search': 'tag:marked'},  # Marked
    'E': {'search': 'tag:leech'},   # lEech

**Changes**

2016-04-27 - Implemented hotkeys for more searches. Thanks to ankitest!

**License**

*Copyright (c) 2016 [Glutanimate](https://github.com/Glutanimate)*

The code for this add-on is hosted in my [misc Anki add-ons repository](https://github.com/Glutanimate/anki-addons-misc).

Licensed under the [GNU GPL v3](http://www.gnu.de/documents/gpl-3.0.en.html).

### anki-browser-search-modifiers.py

**Browser search modifiers**

**Checkbox toggles that modify how the browser search behaves**

Adds two checkboxes to the browser search form that, when toggled, modify searches in the following way:

**Deck** (Hotkey: Alt+D): Limit results to current deck
**Card** (Hotkey: Alt+C): Limit results to first card of each note

![screenshot](screenshots/anki-browser-search-modifiers.png)

Based on the following add-ons:

- "Limit searches to current deck" by Damien Elmes
   (https://github.com/dae/ankiplugins/blob/master/searchdeck.py)
- "Ignore accents in browser search" by Houssam Salem
   (https://github.com/hssm/anki-addons)

Original idea by Keven on the [Anki support forums](https://anki.tenderapp.com/discussions/ankidesktop/17918-add-on-or-anki-feature-suggestion-show-only-front-card-in-browser-checkbox).

Special thanks to ankitest for testing and improving this add-on.

**License**

*Copyright (c) 2016 [Glutanimate](https://github.com/Glutanimate)*

The code for this add-on is hosted in my [misc Anki add-ons repository](https://github.com/Glutanimate/anki-addons-misc).

Licensed under the [GNU GPL v3](http://www.gnu.de/documents/gpl-3.0.en.html).

### anki-browser-create-duplicate.py

**Duplicate selected Notes**

**Overview**

This add-on supplements the card browser by adding a keyboard shortcut and menu entry for creating duplicates of notes.

Pressing the shortcut (Ctrl+Alt+C by default) or clicking on the 'Create Duplicate' entry in the Edit menu will find all notes belonging to the selected cards and duplicate them in place.

**A few pointers**

- **Important**: All cards generated by each note will be duplicated alongside the note
- All duplicated cards will end up in the deck of the first selected card
- The duplicated cards should look exactly like the originals
- Tags are preserved in the duplicated notes
- Review history is NOT duplicated to the new cards (they appear as new cards)
- The notes will be marked as duplicates (because they are!)

**Changes**

2016-04-30 - duplications can now be undone via CTRL+Z (using Anki's default restoration points)

**Credits, license, and source code**

*Copyright (c) 2016 [Glutanimate](https://github.com/Glutanimate)*

This add-on is based on "[Create Copy of Selected Cards](https://ankiweb.net/shared/info/787914845)" by Kealan Hobelmann

The code for this add-on is hosted in my [misc Anki add-ons repository](https://github.com/Glutanimate/anki-addons-misc).

Licensed under the [GNU GPL v3](http://www.gnu.de/documents/gpl-3.0.en.html).

### anki-browser-lookup.py

**Search browser for selected words**

A simple Anki add-on that adds a context-menu entry to search the card browser for selected words.

**Changes**

2016-04-19 - double-quote phrases when searching

**License**

*Copyright (c) 2016 [Glutanimate](https://github.com/Glutanimate)*

Based on ['OSX Dictionary Lookup'](https://gist.github.com/eddie/ff3d820fb267ae26ca0e) by Eddie Blundell.

The code for this add-on is hosted in my [misc Anki add-ons repository](https://github.com/Glutanimate/anki-addons-misc).

Licensed under the [GNU GPL v3](http://www.gnu.de/documents/gpl-3.0.en.html).

### anki-editor-field-navigation.py

**Quick Field Navigation Add-on for Anki**

**Quickly navigate through your entry fields in the card editor**

This add-on provides the following shortcuts:

**Ctrl** + **1-9**: Switch focus to field 1-9
**Ctrl** + **0**: Switch focus to last field
**Alt** + **Shift** + **F**: Switch focus back to note fields from tag field (to complement Anki's inbuilt Ctrl + Shift + T) hotkey to switch to the tags field)

Note: In their current implementation the hotkeys will not work when the tag suggestions drop-down box is active. I am [still looking for a fix for this](https://anki.tenderapp.com/discussions/add-ons/4725-dd-on-development-unable-to-switch-editor-focus-back-to-web-view-when-tags-completer-is-active).

**Changelog**

2016-04-19 – Reworked the add-on from scratch to have a much leaner footprint
2015-09-04 – Initial release

**License**

*Copyright (c) 2016 [Glutanimate](https://github.com/Glutanimate)*

The code for this add-on is hosted in my [misc Anki add-ons repository](https://github.com/Glutanimate/anki-addons-misc).

Licensed under the [GNU GPL v3](http://www.gnu.de/documents/gpl-3.0.en.html).

### anki-editor-tag-hotkeys.py

**Editor Tag Hotkeys Add-on for Anki**

This is a very simple add-on for [Anki](http://ankisrs.net/) that adds a few hotkey toggles for user-defined tags. It also includes a hotkey that clears the tags field (<kbd>Alt</kbd> + <kbd>Shift</kbd> + <kbd>R</kbd> by default)

**Usage**

*Adding a tag hotkey*

Edit `anki-editor-tag.hotkeys.py` and modify the `onSetupButtons` function with your custom hotkeys and tags. For instance, to add a toggle for the tag *important* and assign it to <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>I</kbd> you would replace the following block:

```python
s = QShortcut(QKeySequence(Qt.CTRL + Qt.SHIFT + Qt.Key_1), editor.parentWindow)
s.connect(s, SIGNAL("activated()"),
          lambda : toggleTag(editor, "toggled-tag1"))
```

with:

```python
s = QShortcut(QKeySequence(Qt.CTRL + Qt.SHIFT + Qt.Key_I), editor.parentWindow)
s.connect(s, SIGNAL("activated()"),
          lambda : toggleTag(editor, "important"))
```

You can add as many toggles as you want by placing additional blocks of this type under the `def onSetupButtons(editor):` line. Make sure to preserve the indenting!

For a list of all possible key assignments check here:

- [keys](http://ftp.ics.uci.edu/pub/centos0/ics-custom-build/BUILD/PyQt-x11-gpl-4.7.2/doc/html/qt.html#Key-enum)
- [modifiers](http://ftp.ics.uci.edu/pub/centos0/ics-custom-build/BUILD/PyQt-x11-gpl-4.7.2/doc/html/qt.html#Modifier-enum)

*Defining a unique tag*

Sometimes you might want to quickly toggle between several different tags. For this purpose I've implemented a configuration option called uniqueTags. Any items added to this list will cause their respective hotkeys to delete all other instances of unique tags aside from the one currently being triggered. 

For instance, if you set up hotkeys for "subject-a" and "subject-b" and add these tags to `uniqueTags`, hitting the hotkey for "subject-a" will delete "subject-b" from the tags list and vice-versa.

To add a unique tag, simply update the following excerpt in the script:

```python
uniqueTags = [
    "subject-a", "subject-b"
]
```

Please make sure to preserve the formatting and quoting while doing so!

**License**

*Copyright 2015 [Glutanimate](https://github.com/Glutanimate)*

Anki Editor Tag Hotkeys add-on for Anki is licensed under the [GNU GPLv3](http://www.gnu.de/documents/gpl-3.0.en.html).


### anki-editor-autocomplete-whitelist.py

**Overview**

This is a modified version of the [Editor Autocomplete add-on for Anki](https://github.com/sartak/anki-editor-autocomplete). Instead of checking against a blacklist of non-autocompleted fields this implementation of the add-on will only enable autocomplete on fields you specify.

Fields to enable autocomplete on can be specified by modifying the `AutocompleteFields` array at the beginning of the script, e.g.:

```python
AutocompleteFields = [ "sources", "additional-info" ]
```

This version of the add-on also includes a hotkey that saves you the trouble of clicking on the autocomplete suggestion. It's set to <kbd>Alt</kbd> + <kbd>Return</kbd> by default.

All credit for the original add-on goes to Shawn M Moore ([@sartak](https://github.com/sartak/)).


### anki-editor-restore-fields.py

**Editor Field History**

**Overview**

This add-on enhances Anki's note editor with the following:

- hotkeys that copy over tags and field values of the last note in the same deck
- a history window that provides a list of last used values for the current field

Overview of all available hotkeys:

*Ctrl + Alt + H* – Invoke history window
*Alt+Z* – Copy over current field from last note
*Alt+Shift+Z* – Copy over a a number of user-defined fields (see below)
*Ctrl+Alt+Shift+Z* – Copy over all fields

**Configuration**

You can edit the add-on's source code to modify the following:

`history_window_shortcut`: controls the hotkey for invoking the history window
`field_restore_shortcut`: controls "Restore current field hotkey"
`partial_restore_shortcut`: controls "Restore a number of user-defined fields" hotkey
`full_restore_shortcut`: controls "Restore all fields" hotkey
`partial_restore_fields`: list of fields that are restored by the `partial_restore_shortcut`. Needs to be formatted as a python list (e.g. `["field1", "field2", "field3"]`).

**Changelog**

2016-12-13 – Fixed a rare bug that caused empty notes to appear
2016-06-04 – Added history window to the add-on (invoked via Ctrl+Alt+H)
2016-05-27 – Initial release

**License**

*Copyright (c) 2016 [Glutanimate](https://github.com/Glutanimate)*

The code for this add-on is hosted in my [misc Anki add-ons repository](https://github.com/Glutanimate/anki-addons-misc).

Licensed under the [GNU GPL v3](http://www.gnu.de/documents/gpl-3.0.en.html).


### anki-browser-refresh.py

**F5 to Refresh the Browser**

Adds a hotkey to the browser that refreshes the current view. Useful when you've added new cards and want to repeat an existing search. Note: cards are sorted by creation time when refreshing the view.

Hotkey: *F5*

**Changelog**

2016-05-27 – Initial release

**License**

*Copyright (c) 2016 [Glutanimate](https://github.com/Glutanimate)*

The code for this add-on is hosted in my [misc Anki add-ons repository](https://github.com/Glutanimate/anki-addons-misc).

Licensed under the [GNU GPL v3](http://www.gnu.de/documents/gpl-3.0.en.html).


### anki-browser-replace-tag.py

**Search and Replace Tags**

**Overview**

Adds a "Replace Tag" dialog to the card browser that prompts for a tag and its replacement and then replaces the tag in all selected notes.

Hotkey: *Ctrl+Alt+Shift+T*

**Changelog**

2016-06-04 – Switch to title case for menu entries
2016-05-27 – Initial release

**License**

*Copyright (c) 2016 [Glutanimate](https://github.com/Glutanimate)*

The code for this add-on is hosted in my [misc Anki add-ons repository](https://github.com/Glutanimate/anki-addons-misc).

Licensed under the [GNU GPL v3](http://www.gnu.de/documents/gpl-3.0.en.html).


### anki-browser-create-filtered-deck.py

**Create Filtered Deck from the Browser**

Adds a hotkey and menu item to the browser that launches a filtered deck creation dialog based on the current search.

Hotkey: *Ctrl+Shift+D*

The dialog will be placed above Anki's main window (this is a limitation of the deck creation dialog).

**Changelog**

2016-05-28 – Initial release

**License**

*Copyright (c) 2016 [Glutanimate](https://github.com/Glutanimate)*

The code for this add-on is hosted in my [misc Anki add-ons repository](https://github.com/Glutanimate/anki-addons-misc).

Licensed under the [GNU GPL v3](http://www.gnu.de/documents/gpl-3.0.en.html).

### anki-overview-deck-switcher.py

**Switch Between Decks on the Main Screen**

Adds the following hotkeys to Anki's main deck browser screen:

Ctrl + Tab: Switch to next deck
Ctrl + Shift + Tab: Switch to previous deck

These also work in the detailed view of each deck and in the reviewer.

**Configuration**

By default the hotkeys will skip decks that don't have any cards that are due or new. Filtered decks and custom study sessions are also ignored. You can change this by editing the add-on and setting the variables defined in the USER CONFIGURATION section at the top.

**Changelog**

2016-07-30 – Initial release

**Compatibility**

Only works with Anki releases 2.0.x for now, i.e. the Anki 2.1.x alpha/beta is not yet supported.

**License**

*Copyright (c) 2016 [Glutanimate](https://github.com/Glutanimate)*

The code for this add-on is hosted in my [misc Anki add-ons repository](https://github.com/Glutanimate/anki-addons-misc).

Licensed under the [GNU GPL v3](http://www.gnu.de/documents/gpl-3.0.en.html).

### anki-reviewer-puppy-reinforcement.py

**Puppy Reinforcement**

**Overview**

Uses intermittent reinforcement with cute puppies to encourage card review streaks.

Based on "Show Cute Dogs" (https://ankiweb.net/shared/info/1125592690).

![](https://raw.githubusercontent.com/Glutanimate/anki-addons-misc/master/screenshots/anki-reviewer-puppy-reinforcement.png)

**What's new in this version**

- Uses tooltips instead of a separate window
- The puppies are spread intermittently through your reviews. By default they will appear around every 10 cards (some take longer than others). You can customize this by editing the add-on)
- Customizable encouragement messages that change based on the card tally
- Removed cats and other non-puppies

**Other notes**

- The add-on comes with around 50 puppies by default, but you can add more by placing additional images in the puppy_reinforcement folder next to the add-on
- the tooltip will appear slightly higher than tooltips in Anki usually do. This is to prevent overlapping with other tooltips (e.g. the ones produced by the answer confirmation add-on)

**Credits**

(c) 2015 mbertolacci (https://github.com/mbertolacci)
(c) 2016 Glutanimate (https://github.com/Glutanimate)

Source code: https://github.com/Glutanimate/anki-addons-misc/blob/master/anki-reviewer-puppy-reinforcement.py

### anki-browser-advanced-preview.py

**Advanced Previewer**

**Overview**

Extends the card previewer with the following features:

- Preview multiple cards at the same time
- Option to show both the front and back of your cards (toggled via a button or the hotkey 'B')
- Customizable preview content styling (by editing the source code)

**Demo**

Here's a quick demo video that showcases these features:

[![YouTube: Anki add-on demo: Advanced  Previewer](https://i.ytimg.com/vi/yQ1fpGsPRMU/mqdefault.jpg)](https://youtu.be/yQ1fpGsPRMU)

**Other Remarks**

Rendering multiple notes at once can be taxing on the system, so please don't try invoking the preview window on too many notes. Otherwise Anki might stop responding and need to be restarted.

**Changelog**

2016-12-24 – Add tooltips and shortcuts that were introduced in Anki 2.0.37
2016-12-09 – Add support for "Replay Buttons on Card" and "JS Booster" add-ons
2016-12-04 – Initial release

**License**

*Copyright (c) 2016 [Glutanimate](https://github.com/Glutanimate)*

The code for this add-on is hosted in my [misc Anki add-ons repository](https://github.com/Glutanimate/anki-addons-misc).

Licensed under the [GNU GPL v3](http://www.gnu.de/documents/gpl-3.0.en.html).

This add-on was written [on commission](https://anki.tenderapp.com/discussions/add-ons/8504-100-for-add-on-developer).

### anki-browser-batch-edit.py

**Batch Note Editing**

**Overview**

Adds a new menu item to the card browser that allows you to:

- batch-add information/media to a specific field
- batch-replace the contents of a specific field

The changes will be applied to all selected notes that feature the selected field.

**Demo**

Here's a quick demo video that showcases these features:

[![YouTube: Anki add-on demo: Batch Note Editing](https://i.ytimg.com/vi/iCZzcSnAeH4/mqdefault.jpg)](https://youtu.be/iCZzcSnAeH4)

**Other Remarks**

The add-on uses the first selected note to generate the field list you're presented with. So please make sure to select a note with the right fields.

**Changelog**

2016-12-11 – Support for adding text before existing content (thanks to @luminousspice for the idea)
2016-12-08 – Initial release

**License**

*Copyright (c) 2016 [Glutanimate](https://github.com/Glutanimate)*

All credit for the original idea for this add-on goes to [/u/TryhardasaurusRex on Reddit](https://www.reddit.com/user/TryhardasaurusRex) who commissioned its development.

The code is also hosted in my [misc Anki add-ons repository](https://github.com/Glutanimate/anki-addons-misc).

Licensed under the [GNU GPL v3](http://www.gnu.de/documents/gpl-3.0.en.html).

### anki-reviewer-card-stats.py

**Extended Card Stats During Review**

Based on [Card Info During Review](https://ankiweb.net/shared/info/2179254157) by Damien Elmes and [Reviewer Show Cardinfo](https://github.com/steveaw/anki_addons/blob/master/reviewer_show_cardinfo.py) by Steve AW. Extends Damien's add-on with a review log table similar to the one found in the Browser.

**Screenshot**

![](https://raw.githubusercontent.com/Glutanimate/anki-addons-misc/master/screenshots/anki-reviewer-card-stats.png)

**License**

*Copyright (c) 2012 Damien Elmes*
*Copyright (c) 2013 Steve AW*
*Copyright (c) 2016 [Glutanimate](https://github.com/Glutanimate)*

The code for this add-on is hosted in my [misc Anki add-ons repository](https://github.com/Glutanimate/anki-addons-misc).

Licensed under the [GNU GPL v3](http://www.gnu.de/documents/gpl-3.0.en.html).

### anki-editor-custom-tagedit.py

**Tag Entry Enhancements**

A number of enhancements meant to improve keyboard navigation in Anki's tag entry field:

- adds *Return/Enter* as a hotkey to apply the first suggested tag
- adds *Ctrl+Tab* as a hotkey to move through the list of suggestions
- disables initial suggestion box popup when entering the field

**Changelog**

2016-12-28 – Initial release

**License**

*Copyright (c) 2016 [Glutanimate](https://github.com/Glutanimate)*

The code for this add-on is hosted in my [misc Anki add-ons repository](https://github.com/Glutanimate/anki-addons-misc).

Licensed under the [GNU GPL v3](http://www.gnu.de/documents/gpl-3.0.en.html).

### anki-overview-heatmap.py

**Review Heatmap**

Adds a **heatmap graph** to Anki's main window which visualizes past and future card review activity, similar to the contribution view on GitHub. Information on the **current streak** is displayed alongside the heatmap. Clicking on an item shows the cards reviewed on that day.

![heatmap of past reviews](https://github.com/Glutanimate/anki-addons-misc/blob/master/screenshots/_anki-overview-heatmap-1.png)

![heatmap of pending reviews](https://github.com/Glutanimate/anki-addons-misc/blob/master/screenshots/_anki-overview-heatmap-2.png)

**Video demonstration**

[![YouTube: Anki add-on demo: Batch Note Editing](https://i.ytimg.com/vi/3Hk5TYdvKnM/mqdefault.jpg)](https://youtu.be/3Hk5TYdvKnM)

(Make sure to enable closed-captions for comments on the demonstrated features)

**Features**

- Color-coded overview of past and future review activity: Hues of green for past reviews, shades of grey for pending reviews
- Tooltips provide additional information on each day
- Ability to navigate between different years
- Clicking on a day will draw up the cards seen on that day in the browser. In case of a future date all cards that are due on that day will be shown instead
- Going to the overview page of a specific deck will show deck-specific information
- The heatmap is updated in real-time as you review more cards

**Configuration**

The add-on will map your entire review history and calculate all available review forecasts by default. With larger collections and slower machines this can have a performance toll.

If you are experiencing slow-downs you can limit the number of days calculated by the add-on. These are controlled by the *HEATMAP_HISTORY_LIMIT* and *HEATMAP_FORECAST_LIMIT* variables in the source code. More information on how to modify these variables is provided in the header section of the add-on.

**Other notes**

Pending review counts will appear as negative numbers. Rather than a deliberate design decision this is a workaround I had to employ in order to utilize two distinct color schemes for past and future reviews.

The browser might not draw up any results when clicking on a day sometimes. This is because the review log also contains entries on cards that might have been deleted in the meantime.

In order to show the cards reviewed on a specific day the add-on adds a new search filter to Anki. This filter can also be used outside of the add-on, e.g. in regular browser searches, and is called in the following way: "seen:days_ago" (e.g. "seen:365").

**Bug Reports and Suggestions**

Bug reports and suggestions are always welcome, but it might take me a while to get to them. Please don't post them here, as I won't be able to help you or reply. Instead, please either use the [issues page](https://github.com/Glutanimate/anki-addons-misc/issues) on GitHub or create a new thread on the [add-on forums](https://anki.tenderapp.com/discussions/add-ons/) (no registration required).

**Changelog**

- 2017-01-02 – The add-on should now be compatible with "More Overview Stats"
- 2017-01-01 – Switched from an absolute color scale to one that's relative to the average daily review count (inspired by the comment below). Fixed a bug with the calendar controls. Improved streak calculation.
- 2016-12-31 – Initial release

**Credits and License**

*Copyright (c) 2016-2017 [Glutanimate](https://github.com/Glutanimate)*

Inspired by GitHub's contribution calendar and *Forecast graph on Overview page* by Steve AW.

Ships with the following javascript libraries:

- d3.js (v3.5.17), (c) Mike Bostock, BSD license
- cal-heatmap (v3.6.2), (c) Wan Qi Chen, MIT license

The code for this add-on is hosted in my [misc Anki add-ons repository](https://github.com/Glutanimate/anki-addons-misc).

Licensed under the [GNU GPL v3](http://www.gnu.de/documents/gpl-3.0.en.html).

-------------------------------

## Yet to be published

- **anki-add-reverse-toggle**: adds a user-defined key-binding that toggles the 'reverse' field in optionally reversible note types (default: Alt+Shift+B)
 
    This one is locale-dependent, so make sure to edit the source file with the name of the 'reverse' field in your note models

- **anki-browser-more-hotkeys**: adds two additional hotkeys to the card browser, CTRL+R for rescheduling cards and CTRL+ALT+I for inverting the selection.

- **anki-reviewer-hint-hotkeys**: based on [Hint-peeking Keyboard Bindings](https://ankiweb.net/shared/info/2616209911) by Ben Lickly. Adds two hotkeys to the reviewer: 'H' to reveal hints one by one, 'G' to reveal all hints at once.

- **anki-sibling-spacing-whitelist**: based on [Sibling Spacing](https://ankiweb.net/shared/info/2951410923) by Andreas Klauer. Modified to follow a whitelist approach when choosing which note types to enable on. Check the comments in the source file for more information.

------------------------

## The rest

If an add-on doesn't appear in this document there's a very good chance it's not ready for general use, yet.
