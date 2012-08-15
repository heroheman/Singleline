# import sublime
import sublime_plugin
import re


def expand_to_css_rule(view, cur_point):
    '''expand cursor inside css rule to whole css rule'''
    rule = '^\w*[^{}\n]+ ?\{([^{}])*\}'
    css_rules = view.find_all(rule)
    for css_rule in css_rules:
        if css_rule.contains(cur_point):
            return css_rule
    # just return cur_point if not matching
    return cur_point


class ExpandToCssRuleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        regions = []

        for s in self.view.sel():
            regions.append(expand_to_css_rule(self.view, s))

        for r in regions:
            self.view.sel().add(r)


def toggle(text):
    # check if the css statement needs to be expanded or collapsed
    single_line = '^[ \t]*[^{}\n]+\{.*\}\s*$'
    if re.match(single_line, text):
        # expand the css statement
        m = re.search('^(?P<leading>\s*)(?P<key>.*)\{(?P<params>.*)\;\s*}$', text)

        lead = m.group('leading')
        key = m.group('key')
        lines = m.group('params').strip().split('; ')

        multi = '%s%s{\n' % (lead, key)
        for line in lines:
            multi += '%s\t%s;\n' % (m.group('leading'), line)
        multi += '%s}' % m.group('leading')

        return multi
    else:
        # collapse the css statement
        m = re.search('^(?P<leading>\s*).*$', text.split('\n')[0])  # grab leading spacing
        single = m.group('leading') + ' '.join([x.strip() for x in text.split('\n')])

        return single


class ToggleSingleLineCssCommand(sublime_plugin.TextCommand):
    '''toggle a single-line or multi-line formatted css statement'''
    def run(self, edit):
        allowed_scopes = 'source.css, source.scss, source.less'
        for region in reversed(self.view.sel()):
            # quit early if not in css area
            if self.view.score_selector(region.a, allowed_scopes) == 0:
                return

            if region.empty():
                region = expand_to_css_rule(self.view, region)
            text = self.view.substr(region)

            text = toggle(text)

            self.view.replace(edit, region, text)
