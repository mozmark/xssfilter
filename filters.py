from jinja2 import Environment, evalcontextfilter, Markup, escape
import reform
from urllib import quote_plus

allowed_prefixes=['http','https','ftp','/'];

@evalcontextfilter
def htmlattributefilter(eval_ctx, value):
  return Markup(reform.HtmlAttributeEncode(value))

@evalcontextfilter
def cssfilter(eval_ctx, value):
  return Markup(reform.CssString(value))

@evalcontextfilter
def cssurlfilter(eval_ctx, value):
  for prefix in allowed_prefixes:
    if value.lower().startswith(prefix):
      return Markup(cssfilter(eval_ctx,value))
  return ''

@evalcontextfilter
def jsfilter(eval_ctx, value):
  return Markup(reform.JsString(value))
  
@evalcontextfilter
def urlparamfilter(eval_ctx, value):
  return Markup(quote_plus(value))

@evalcontextfilter
def urlattributefilter(eval_ctx, value):
  for prefix in allowed_prefixes:
    if value.lower().startswith(prefix):
      return Markup(reform.HtmlAttributeEncode(value,whitelist=':@/.'))
  return ''

