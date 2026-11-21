import os
import re

# O rodapé antigo (padrão que está nos arquivos)
rodape_antigo = """    <footer class="bg-white border-t border-gray-100 py-12 text-center text-sm text-gray-400">
        <p>&copy; 2026 Vivi Correa. Todos os direitos reservados.</p>
    </footer>"""

# O rodapé novo (com os links e fundo escuro)
rodape_novo = """    <!-- Footer -->
    <footer class="bg-gray-900 text-white py-16 text-center text-sm">
        <img src="/logo.png" alt="Vivi Correa" class="h-12 mx-auto mb-6 brightness-0 invert opacity-50" />
        
        <div class="flex justify-center gap-6 mb-8 text-gray-400">
            <a href="/quem-somos" class="hover:text-white transition">Quem Somos</a>
            <a href="/ajuda" class="hover:text-white transition">Ajuda & Políticas</a>
            <a href="https://wa.me/5571991064721" target="_blank" class="hover:text-white transition">Fale Conosco</a>
        </div>
        
        <p class="text-gray-500 text-xs">&copy; 2026 Vivi Correa. Todos os direitos reservados.</p>
        <p class="mt-2 text-xs text-gray-600">Desenvolvido por KA Agência Criativa</p>
    </footer>"""

# Também tentamos pegar o rodapé que está no index.astro (que já é escuro mas não tem os links)
rodape_index_antigo = """    <footer class="bg-gray-900 text-white py-16 text-center text-sm">
        <img src="/logo.png" alt="Vivi Correa" class="h-12 mx-auto mb-6 brightness-0 invert opacity-50" />
        <p class="text-gray-400">&copy; 2026 Vivi Correa. Todos os direitos reservados.</p>
        <p class="mt-2 text-xs text-gray-500">Desenvolvido por KA Agência Criativa</p>
    </footer>"""

diretorios = ['src/pages', 'src/pages/colecoes', 'src/pages/produto']
alterados = 0

for diretorio in diretorios:
    if not os.path.exists(diretorio): continue
    
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith('.astro'):
            caminho = os.path.join(diretorio, arquivo)
            
            with open(caminho, 'r', encoding='utf-8') as f:
                conteudo = f.read()
            
            # Verifica se o rodapé antigo está no arquivo
            if rodape_antigo in conteudo:
                conteudo = conteudo.replace(rodape_antigo, rodape_novo)
                with open(caminho, 'w', encoding='utf-8') as f:
                    f.write(conteudo)
                print(f"✅ Rodapé claro substituído em: {caminho}")
                alterados += 1
            
            # Verifica se o rodapé do index está no arquivo (para atualizar os links)
            elif rodape_index_antigo in conteudo:
                conteudo = conteudo.replace(rodape_index_antigo, rodape_novo)
                with open(caminho, 'w', encoding='utf-8') as f:
                    f.write(conteudo)
                print(f"✅ Rodapé do index atualizado em: {caminho}")
                alterados += 1

print(f"\nFinalizado! {alterados} arquivos foram atualizados.")