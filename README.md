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

 **Felipe Clarindo**
  - [LinkedIn](https://www.linkedin.com/in/felipe-clarindo-934578289/)
  - [Instagram](https://www.instagram.com/lipethegoat)
  - [GitHub](https://github.com/felipeclarindo)


## Licença

Este projeto está licenciado sob a [GNU Affero License](https://www.gnu.org/licenses/agpl-3.0.html).

