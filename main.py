"""
Get the selected text, build contextual menu and search the text using google.
"""
import sublime
import sublime_plugin
import webbrowser


class SearchGoogleForCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        url = 'https://www.google.com.np/search?q={}'.format(self.textSelected)
        webbrowser.open_new_tab(url=url)

    # set the selected text
    def set_text(self):
        self.textSelected = self.view.substr(self.view.sel()[0])

    def is_visible(self):
        self.set_text()

        if self.textSelected:
            return True
        else:
            return False

    # adds captions to context menu usi
    def description(self):
        self.set_text()

        if self.textSelected:
            return 'Search Google for "{}"'.format(self.textSelected)
