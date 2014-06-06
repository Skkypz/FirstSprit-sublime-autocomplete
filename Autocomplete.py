'''
FirstSpirit snippets and syntax autocomplete

Created on 07.05.2014
@author: Gheorgheoiu Nicolae - S.H.E Frontend Team
'''

import sublime, sublime_plugin

class Autocomplete(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        return [
                # HTML
                ('CMS_FOR', "\$CMS_FOR($0,)\$\n\$CMS_END_FOR\$"), 
                ("$COMMENT", "\$--$0--\$"),
                ("$CMS_IF", "\$CMS_IF($0)\$\n\$CMS_END_IF\$"),
                ("$CMS_ELSEIF", "\$CMS_IF($1)\$\n    \$CMS_ELSIF($0)\$\n    \$CMS_ELSE\$\n\$CMS_END_IF\$"),
                ("$CMS_INCLUDE", "\$CMS_INCLUDE($0)\$"),
                ("$CMS_REF", "\$CMS_REF($0)\$"),
                ("$CMS_RENDER", "\$CMS_RENDER($0)\$"),
                ("$CMS_SET", "\$CMS_SET($0,)\$"),
                ("$CMS_SET+END_SET", "\$CMS_SET($0)\$\n\$CMS_END_SET\$"),
                ("$CMS_SWITCH", "\$CMS_SWITCH($1)\$\n    \$CMS_CASE($0)\$\n\$CMS_END_SWITCH\$"),
                ("$CMS_TRIM", "\$CMS_TRIM(level:$0)\$\n\$CMS_END_TRIM\$"),
                ("$CMS_VALUE", "\$CMS_VALUE($0)\$"),
                ("$CMS_VALUE DEFAULT", "\$CMS_VALUE($1,default:\"$0\")\$")
                ]


                