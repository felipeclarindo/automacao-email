# Automação de Envio de E-mails

Este é um programa Python que automatiza o envio de e-mails utilizando a biblioteca `smtplib` e agendamento com a biblioteca `schedule`.

## Funcionalidades

- Envio de e-mails para uma lista de destinatários.
- Agendamento do envio de e-mails em horários específicos.
- Rastreamento de aberturas, cliques e conversões.
- Geração de relatório em PDF com as métricas de entrega, abertura, cliques e conversões.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

- `smtplib`
- `ssl`
- `schedule`
- `reportlab`

## Configuração do Remetente

Antes de usar o programa, é necessário configurar o remetente, que é a conta de e-mail da qual os e-mails serão enviados. Para garantir a segurança da sua conta, siga estas etapas:

1. Acesse a sua conta de e-mail.
2. Vá para as configurações de segurança.
3. Ative a autenticação de dois fatores (2FA) se ainda não estiver ativada.
4. Na seção de autenticação de 2FA, escolha a opção "Senha de App" para gerar uma senha específica para o aplicativo.
5. Escolha "E-mail" como o aplicativo e selecione o dispositivo para o qual você deseja gerar a senha de app.
6. Anote a senha de app gerada, pois você usará essa senha no lugar da sua senha normal ao executar o programa.

## Como Usar

1. Execute o código `main.py` em um ambiente Python.
2. Siga as instruções do terminal para configurar o remetente, destinatários, assunto e corpo do e-mail.
3. Se desejar, anexe uma imagem ao e-mail.
4. Escolha se deseja agendar o envio do e-mail.
5. Confirme o envio dos e-mails.

## Gerenciamento de Destinatários

O programa permite que você gerencie a lista de destinatários. Você pode adicionar ou remover destinatários manualmente, ou carregar uma lista a partir de um arquivo.

## Agendamento

Você pode escolher agendar o envio do e-mail. Há três opções de agendamento disponíveis:

1. Agendamento para hoje em um horário específico.
2. Agendamento para um dia específico da semana e horário.
3. Agendamento para um dia específico do mês e horário.

## Relatório

Após o envio dos e-mails, o programa gera um relatório em PDF com as métricas de entrega, abertura, cliques e conversões. O relatório é salvo como `email_relatorio.pdf`.

## Notas

- Certifique-se de que sua conta de e-mail permita acesso de aplicativos menos seguros.
- Em sua senha, é precisa que você pegue o token dela in
- Este código é um exemplo simplificado e pode ser adaptado para suas necessidades específicas.

## Autor

Felipe Clarindo!




<!-- # Programa de Envio de E-mails

Este é um programa simples em Python que permite enviar e-mails, agendar o envio de e-mails, gerar relatórios detalhados sobre os e-mails enviados e salvar esses relatórios em formato PDF.

## Funcionalidades

- Envio de e-mails para destinatários individuais.
- Agendamento de envio de e-mails para um horário específico.
- Geração de relatórios detalhados sobre os e-mails enviados, incluindo a taxa de entrega, taxa de abertura e taxa de cliques.
- Salvamento dos relatórios em formato PDF.

## Requisitos

- Python 3.x
- Bibliotecas: `smtplib`, `ssl`, `time`, `schedule`, `requests`, `json`, `reportlab`,`os`
- Uma conta de e-mail Gmail para enviar os e-mails.

## Como Executar

1. Certifique-se de ter as bibliotecas necessárias instaladas. Você pode instalar as bibliotecas usando o seguinte comando:
Certifique-se de ter as seguintes bibliotecas instaladas:

Será necessario instalar as seguintes bibliotecas: 

- `secure-smtplib` (envio de emails)
- `schedule` (agendamento de tarefas)
- `requests` (requisições HTTP)
- `reportlab` (geração de PDFs)


As seguintes bibliotecas fazem parte da biblioteca padrão do Python e não requerem instalação adicional:

- `ssl` (segurança para conexões de rede)
- `time` (gerenciamento de tempo)
- `json` (manipulação de dados JSON)
- `os` (operações do sistema operacional)
 -->
