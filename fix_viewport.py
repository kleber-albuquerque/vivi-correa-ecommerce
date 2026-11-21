import re, pathlib
META = '<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">'
alvo = []
for p in sorted(pathlib.Path('src').rglob('*.astro')):
    s = p.read_text(encoding='utf-8')
    if re.search(r'name=["\']viewport["\']', s, re.I):
        continue
    if not re.search(r'<head[\s>]', s, re.I):
        continue
    m = re.search(r'<meta\s+charset=[^>]*>', s, re.I)
    if m:
        s = s[:m.end()] + '\n    ' + META + s[m.end():]
    else:
        s = re.sub(r'(<head[^>]*>)', lambda mm: mm.group(1) + '\n    ' + META, s, count=1, flags=re.I)
    p.write_text(s, encoding='utf-8')
    alvo.append(str(p))
print('viewport injetada em:', len(alvo))
for a in alvo: print('  +', a)
