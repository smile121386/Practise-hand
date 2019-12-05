from lxml import etree
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
# text = '''
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# '''
html = etree.HTML(text)
result = html.xpath('//li/attribute::*')
# print(type(result))
print(result)
# result1 = html.xpath('//li[last()]/a/text()')
# print(result1)
# result2 = html.xpath('//li[position()<3]/a/text()')
# print(result2)
# result3 = html.xpath('//li[last()-2]/a/text()')
# print(result3)
