Documentação do Sistema de Cadastro FURIA

📌 Visão Geral
Sistema completo para cadastro e consulta de pessoas com integração de conteúdos específicos por interesses (LoL, Valorant, CS2) e produtos oficiais da FURIA.

🛠 Tecnologias Utilizadas
Frontend: HTML5, CSS3, JavaScript

Backend: Flask (para roteamento básico)

Armazenamento: LocalStorage do navegador

Formatos de Imagem: WEBP (otimizado) + JPG/JPEG (fallback)

🔧 Configuração
Clone o repositório:

bash
git clone [https://github.com/seu-usuario/furia-cadastro.git](https://github.com/rafaelbsdev/Furia_Dificil)
cd furia-cadastro
Instale as dependências:

bash
pip install flask python-dotenv
Execute o aplicativo:

bash
python app.py
Acesse no navegador:

✨ Funcionalidades
🧑 Cadastro de Pessoas
Validação de campos obrigatórios

Formatação automática de CPF e telefone

Upload de foto de perfil (com preview)

Seleção de múltiplos interesses

🔍 Consulta Inteligente
Busca por nome, CPF, e-mail ou telefone

Visualização em cards com foto

Exclusão individual de cadastros

🎮 Conteúdo por Interesse
League of Legends:

Instagram @furia.lol

Vídeos do YouTube

Valorant:

Canal especializado

Posts de estratégia

CS2:

Notícias de campeonatos

Vlogs exclusivos

🛍️ Produtos Relacionados
Exibição de 4 produtos aleatórios

Links diretos para loja oficial

Imagens em WEBP de alta performance

🎨 Personalização
Temas Disponíveis
css
/* themes.css */
.dark-theme {
  --bg-color: #1a1a1a;
  --text-color: #f0f0f0;
}

.light-theme {
  --bg-color: #f9f9f9;
  --text-color: #333;
}

📱 Widget WhatsApp
Botão flutuante no canto inferior direito

Modal de confirmação antes de redirecionar

Link configurável no código

🔄 JSON de Conteúdo
Estrutura do arquivo content.json:

json
{
  "geral": {
    "produtos": [...],
    "redes_sociais": [...]
  },
  "League of Legends": {
    "redes_sociais": [...],
    "conteudo": [...]
  },
  "Valorant": {...},
  "CS 2": {...}
}

📌 Dependências
Python 3.8+

Flask 2.0+

Navegador moderno (Chrome, Firefox, Edge)

📄 Licença
MIT License - Livre para uso e modificação

🌟 Recursos Adicionais
Documentação Flask

Conversor para WEBP

Ícones Unicode

👨‍💻 Autor
[Rafael Augusto Belo Silva] - [rafaelbs.dev@gmail.com]
