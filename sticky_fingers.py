from bs4 import BeautifulSoup as bs
import re


def sticky_fingers(html, tag, attr, pattern_set, pattern_end):
    pattern = re.compile(r'''({0})=["']?((?:.(?!["']?\s+(?:\S+)=|[>"']))+.)["']?'''.format(attr))
    with open(html, 'r') as input, open('output.html', 'w') as output:
        text = input.read()
        soup = bs(text,  'html.parser')
        html_tags = list(soup.findAll(tag))
        for html_tag in html_tags:
            match = pattern.search(str(html_tag)).group()
            skip = len(attr) + 1
            #new_attr = attr + '''="{{ url_for('static', filename=''' + match[skip::].replace('"',"'") + ''') }}"'''
            new_attr = attr + '''=''' + pattern_set + match[skip::].replace('"',"'") + pattern_end
            text = text.replace(match, new_attr)
        output.write(text)
        input.close()
        output.close()


if __name__ == '__main__':
    print('Hello, world!!!')
    #sticky_fingers('input.html','link' ,'href', '''"{{ fuck you''', ''', a leather man''')
    sticky_fingers('input.html','img' ,'src', '''"{{ url_for('static', filename=''', ''') }}"''')    