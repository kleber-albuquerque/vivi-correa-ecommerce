import re, pathlib

def repl_static(m):
    attr, path = m.group(1), m.group(2)
    if path.startswith('//'):
        return m.group(0)
    return attr + '={`${import.meta.env.BASE_URL}' + path[1:] + '`}'

for p in pathlib.Path('src').rglob('*.astro'):
    s = p.read_text(encoding='utf-8')
    orig = s
    s = re.sub(r'(href|src)="(/[^"]*)"', repl_static, s)
    s = re.sub(r"(href|src)='(/[^']*)'", repl_static, s)
    s = re.sub(r'(href|src)=\{`/', r'\1={`${import.meta.env.BASE_URL}', s)
    s = re.sub(r"location\.href\s*=\s*'/", "location.href = import.meta.env.BASE_URL + '", s)
    s = re.sub(r'location\.href\s*=\s*"/', 'location.href = import.meta.env.BASE_URL + "', s)
    s = re.sub(r'location\.href\s*=\s*`/', 'location.href = `${import.meta.env.BASE_URL}', s)
    s = re.sub(r"location\.(assign|replace)\('/", r"location.\1(import.meta.env.BASE_URL + '", s)
    s = s.replace("bundlePath: '/pagefind/'", "bundlePath: import.meta.env.BASE_URL + 'pagefind/'")
    s = s.replace('bundlePath: "/pagefind/"', 'bundlePath: import.meta.env.BASE_URL + "pagefind/"')
    if s != orig:
        p.write_text(s, encoding='utf-8')
        print('corrigido:', p)
print('concluido')
