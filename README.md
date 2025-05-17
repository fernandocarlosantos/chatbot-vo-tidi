# Chatbot Vó Tidi - Seu Assistente de Receitas Amoroso

## Olá, meu querido(a)! 👋

Este é o repositório do Chatbot Vó Tidi, um assistente pessoal muito especial com um toque de carinho de avó! Ele foi criado para te ajudar com todas as suas dúvidas sobre receitas deliciosas, sempre com uma linguagem acolhedora e cheia de amor.

## Como Funciona? 🤔

O código Python presente neste projeto utiliza a biblioteca `google-genai` para interagir com um modelo de linguagem da Google (atualmente configurado para ser o `gemini-2.0-flash`). A mágica acontece da seguinte forma:

1.  **Configuração Inicial:**
    * Importa as bibliotecas necessárias (`os`, `google.genai`, `google.colab.userdata`, `types`).
    * Tenta obter sua chave da API do Google Cloud a partir do `userdata` do Google Colab (isso é importante para autenticar o acesso ao modelo).
    * Cria um cliente para interagir com a API do Gemini.
    * Define o modelo de linguagem a ser usado (`gemini-2.0-flash`).
    * Cria uma configuração para o chat, definindo uma instrução de sistema muito importante: o chatbot deve se comportar como uma "vovó amorosa" focada em receitas.

2.  **Criação da Sessão de Chat:**
    * Inicializa uma sessão de chat com o modelo e a configuração definida.

3.  **Mensagem de Apresentação:**
    * Exibe uma mensagem calorosa de boas-vindas, como se a Vó Tidi estivesse falando com você!

4.  **Loop de Conversa:**
    * Entra em um loop onde o programa espera que você digite sua pergunta sobre receitas.
    * Enquanto você não digitar "fim", o chatbot (Vó Tidi) processa sua pergunta e envia uma resposta gerada pelo modelo de linguagem.
    * A resposta é exibida na tela.
    * O programa pergunta novamente o que mais você gostaria de aprender.

## Como Usar? 🚀

Para experimentar o Chatbot Vó Tidi, você precisará:

1.  **Ter uma chave da API do Google Cloud Gen AI.** Você pode obter uma seguindo os passos na documentação oficial do Google Cloud AI.
2.  **Estar em um ambiente onde você possa configurar variáveis de ambiente ou usar o `google.colab.userdata`.** O código fornecido assume que você está usando o Google Colab e configurou sua chave API nos "User Secrets".
3.  **Executar o código Python.** Ao rodar o script, você verá a mensagem de apresentação da Vó Tidi e poderá começar a fazer suas perguntas sobre receitas!

## Exemplo de Conversa 💬
