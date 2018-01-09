"""
Get the selected text, build contextual menu and search the text using google.
"""
import sublime
import sublime_plugin
import webbrowser


class SublimeSearchForCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        url = 'https://www.google.com.np/search?q={}'.format(self.get_text())
        webbrowser.open_new_tab(url=url)

    # get the selected text
    def get_text(self):
        return self.view.substr(self.view.sel()[0])

    def is_visible(self):
        if self.get_text():
            return True
        else:
            return False

    # adds captions to context menu
    def description(self):
        text = self.get_text()
        if text:
            return 'Search Google for "{}"'.format(text)
