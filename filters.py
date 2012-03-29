from jinja2 import Environment, evalcontextfilter, Markup, escape
import reform
from urllib import quote_plus

allowed_prefixes=['http','https','ftp','/'];

@evalcontextfilter
def htmlattribute(eval_ctx, value):
  return Markup(reform.HtmlAttributeEncode(value))

@evalcontextfilter
def cssvalue(eval_ctx, value):
  return Markup(reform.CssString(value))

@evalcontextfilter
def cssurl(eval_ctx, value):
  for prefix in allowed_prefixes:
    if value.lower().startswith(prefix):
      return Markup(cssvalue(eval_ctx,value))
  return ''

@evalcontextfilter
def jsvalue(eval_ctx, value):
  return Markup(reform.JsString(value))
  
@evalcontextfilter
def urlparam(eval_ctx, value):
  return Markup(quote_plus(value))

@evalcontextfilter
def urlattribute(eval_ctx, value):
  for prefix in allowed_prefixes:
    if value.lower().startswith(prefix):
      return Markup(reform.HtmlAttributeEncode(value,whitelist=':@/.'))
  return ''

