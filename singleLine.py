import sublime
import sublime_plugin
import re


def expand_to_css_rule(view, cur_point):
    print "in expander"
    '''expand cursor inside css rule to whole css rule'''
    css_rules = view.find_all('(^ *\.?\w+) ?\{([^{])*\}')
    for css_rule in css_rules:
        print css_rule.a, css_rule.b, view.substr(css_rule)
        if css_rule.contains(cur_point):
            return css_rule
    # just return cur_point region if nothing found
    return cur_point


class ToggleSingleLineCssCommand(sublime_plugin.TextCommand):
    '''toggle a single-line or multi-line formatted css statement'''
    def run(self, edit):
        print "======= entered toggle function ========"
        for region in reversed(self.view.sel()):
            # quit early if not in css area
            if self.view.score_selector(region.a, 'source.css') == 0:
                return

            if region.empty():
                region = expand_to_css_rule(self.view, region)
            text = self.view.substr(region)
            print '>>> css region ==>', text

            # check if the css statement needs to be expanded or collapsed
            if re.match('^.*\{.*}\s*$', text):
                # expand the css statement
                m = re.search('^(?P<key>.*)\{(?P<params>.*)\;\s*}$', text)
                multiline = '%s{\n\t%s;\n}' % (m.group('key'), m.group('params').strip().replace('; ', ';\n\t'))
                self.view.replace(edit, region, multiline)
            else:
                # collapse the css statement
                singleline = ' '.join([x.strip() for x in text.split('\n')])
                self.view.replace(edit, region, singleline)
