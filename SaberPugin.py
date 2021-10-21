import sublime
import sublime_plugin
import random

class SaberRunCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		saber_str = self.view.settings().get('saber_str', '')
		prefix = self.view.settings().get('saber_prefix', '')
		name_lenth = self.view.settings().get('saber_length', 6)
		sel = self.view.sel()[0]
		if len(saber_str)==0:
			saber_str = 'abcdefghijklmnopqrstuvwxyz1234567890'

		names = random.sample(saber_str, name_lenth)
		class_name = ''.join(names)
		if len(prefix) > 0 :
			class_name = prefix+'-'+class_name

		#copy the class name to clipboard
		sublime.set_clipboard('.'+class_name)
		self.view.replace(edit, sublime.Region(sel.begin(), sel.begin()), 'class="'+class_name+'"')
