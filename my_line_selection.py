import sublime
import sublime_plugin
class MyLineSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        new_cursors = []
        cursors = view.sel()
        for cursor in cursors:
            new_cursors.append(view.line(cursor))
        cursors.clear()
        for cursor in new_cursors:
            cursors.add(cursor)