
import os
import re

# O novo header que vai substituir o antigo
novo_header = """
import Header from '{path}components/Header.astro';
---
<Header />
"""

# O padrão do header antigo (procura desde <header> até </header>)
padrao_header = re.compile(r'<header.*?</header>', re.DOTALL)

# Pastas onde estão os arquivos
pastas = [
    ('src/pages', '../'), # Arquivos na raiz de pages precisam subir um nível
    ('src/pages/colecoes', '../../'),
    ('src/pages/produto', '../../')
]

for pasta, caminho_relativo in pastas:
    if not os.path.exists(pasta): continue
    
    for arquivo in os.listdir(pasta):
        if arquivo.endswith('.astro'):
            caminho_completo = os.path.join(pasta, arquivo)
            
            with open(caminho_completo, 'r', encoding='utf-8') as f:
                conteudo = f.read()
            
            # Só altera se encontrar o header antigo
            if '<header' in conteudo:
                # Remove o header antigo e coloca o import + componente
                conteudo_novo = padrao_header.sub(novo_header.format(path=caminho_relativo), conteudo)
                
                with open(caminho_completo, 'w', encoding='utf-8') as f:
                    f.write(conteudo_novo)
                print(f"✅ Atualizado: {caminho_completo}")

print("Finalizado!")
