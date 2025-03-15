Assistente Digita - Assistente Pessoal de Voz
Este projeto é um assistente pessoal simples que utiliza reconhecimento de voz, síntese de voz e integração com vários sites e ferramentas. Ele é capaz de realizar tarefas como procurar informações na Wikipédia, abrir o YouTube, Google, sites específicos e até executar comandos locais como abrir a calculadora.

Funcionalidades
Reconhecimento de voz: O assistente pode ouvir comandos do usuário e responder a eles.
Pesquisa na Wikipédia: Você pode pedir ao assistente para procurar algo na Wikipédia e ele vai ler o resumo para você.
Abrir sites: O assistente pode abrir sites como YouTube, Google e até o site do Vasco.
Pesquisa de músicas: O assistente pode pesquisar as melhores músicas de 2025 ou as melhores músicas de rock no YouTube.
Abrir a Calculadora: O assistente pode abrir a calculadora do Windows.
Comandos personalizados: O código pode ser facilmente expandido para adicionar mais comandos.
Pré-requisitos
Antes de rodar o projeto, você precisa instalar as seguintes bibliotecas Python:

pyttsx3: para conversão de texto em fala.
speech_recognition: para reconhecimento de fala.
wikipedia: para consulta na Wikipédia.
webbrowser: para abrir sites diretamente.
Use o comando abaixo para instalar as dependências:

bash
Copiar
pip install pyttsx3 SpeechRecognition wikipedia
Como Usar
Clone o repositório:
bash
Copiar
git clone https://github.com/seu-usuario/assistente-digita.git
cd assistente-digita
Execute o script assistente.py:
bash
Copiar
python assistente.py
O assistente começará a ouvir os seus comandos. Você pode falar em português e ele responderá de acordo com o comando dado.

Exemplos de Comandos
"Pesquise na Wikipédia sobre Python": O assistente irá buscar um resumo sobre Python na Wikipédia e ler para você.
"Abrir o Youtube": O assistente abrirá o YouTube no seu navegador.
"Abrir o Google": O assistente abrirá o Google no seu navegador.
"Abrir o site do Vasco": O assistente abrirá o site oficial do Vasco da Gama.
"Melhores músicas no YouTube 2025": O assistente buscará as melhores músicas de 2025 no YouTube.
"Tchau": O assistente se despedirá e o programa será encerrado.
Contribuindo
Sinta-se à vontade para contribuir com melhorias, novas funcionalidades ou correções de bugs. Se você tiver alguma ideia ou sugestão, crie um "issue" ou envie um "pull request".
