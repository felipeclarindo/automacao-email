from hashlib import sha256
import smtplib
import ssl
import time
import schedule
import requests
import json
import os
import random

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

cont = 0
send_job = 0
receivers = []
email_status = {}
alter = {}
message = ""
sends = []
sender_name = ""
subject = ""
body = ""
imagem = ""

print("-" * 45)
print("--------------- Send E-mails  ---------------")
print("-" * 45)

input("APERTE ENTER PARA INICIALIZAR A APLICAÇÂO!")

try:
    # cria o servidor SMTP

    print("Conectando-se ao servidor...")
    time.sleep(1)

    context = ssl.create_default_context()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()

    print("Conectado!")

    # dados do remetente  ik

    email_cliente = str(input("Qual seu e-mail? ")).replace(" ", "").lower()
    user_password = str(input("Digite a senha do e-mail: ")).replace(" ", "").lower()
    name_email = str(input("Qual o nome do remetente? ")).title()

    sender_email = email_cliente  # e-mail do remetente
    password = user_password  # senha do e-mail
    hash_password = sha256(password.encode())
    sender_name = name_email  # nome do remetente

    print('-' * 40)

    # dados do email

    title = str(input("Qual o assunto do e-mail? "))
    corpo = str(input("Qual o texto que deseja no e-mail? "))

    subject = title
    body = corpo
    message = f'From:{sender_name}\nSubject:{subject}\n\n{body}'

    # Instancia de MIMEmultipart

    msg = MIMEMultipart()
    msg['From: '] = sender_name
    msg['Subject: '] = subject

    # Adicione o corpo do e-mail como texto

    msg.attach(MIMEText(body, 'plain'))


    # Calcular Metricas

    def calculate_metrics():
        total_emails = len(email_status)
        total_respostas = sum(status['resposta'] for status in email_status.values())
        total_conversoes = sum(status.get('conversao', False) for status in email_status.values())

        taxa_resposta = (total_respostas / total_emails) * 100
        taxa_conversao = (total_conversoes / total_emails) * 100

        return taxa_resposta, taxa_conversao

        # Código para enviar e-mails aqui, incluindo todas as partes que você já implementou


    def send_emails():

        global cont

        # Loop para enviar e-mails para cada destinatário
        for receiver in receivers:
            try:

                server.login(sender_email, password)

                # Simulando envio do e-mail
                email_status[receiver] = {
                    "entregue": True,
                    "aberto": False,
                    "clicado": False,
                    "resposta": False
                }

                server.sendmail(sender_email, receiver, msg.as_string())
                sends.append(print(f"E-Mail para {receiver} Enviado!!!"))
                cont += 1

            except Exception as e:
                print(f"Erros: {e}")

        taxa_resposta, taxa_conversao = calculate_metrics()
        track_conversions()
        calculate_metrics()
        show_report()
        generate_pdf_report(taxa_resposta, taxa_conversao)

        print("\nMétricas:")
        print(f"Taxa de Resposta: {taxa_resposta:.2f}%")
        print(f"Taxa de Conversão: {taxa_conversao:.2f}%")


    def schedule_and_send():
        send_emails()
        calculate_metrics()
        schedule.cancel_job(send_job)  # Cancela o job para que não seja reagendado
        show_report()


    # rastrear conversões

    def track_conversions():
        for receiver in email_status:
            # Simule que uma conversão ocorreu com uma probabilidade de 20%
            email_status[receiver]["conversao"] = random.random() < 0.2

        calculate_metrics()


    # Gerar um relatorio em pdf

    def generate_pdf_report(taxa_resposta, taxa_conversao):

        c = canvas.Canvas("email_relatorio.pdf", pagesize=letter)

        c.drawString(100, 750, "Relatório de E-mails Enviados")
        c.drawString(100, 730, "-" * 40)

        y = 700
        for receiver, status in email_status.items():
            status_str = f"Entregue: {status['entregue']}, Aberto: {status['aberto']}, Clicado: {status['clicado']}, Resposta: {status['resposta']}, Conversão: {status.get('conversao', False)}"
            c.drawString(100, y, f"{receiver}: {status_str}")
            y -= 20

        total_emails = len(email_status)
        total_entregues = sum(status['entregue'] for status in email_status.values())
        total_abertos = sum(status['aberto'] for status in email_status.values())
        total_clicados = sum(status['clicado'] for status in email_status.values())

        taxa_entrega = (total_entregues / total_emails) * 100
        taxa_abertura = (total_abertos / total_emails) * 100
        taxa_cliques = (total_clicados / total_emails) * 100

        c.drawString(100, y - 20, "\nResumo do Relatório:")
        c.drawString(100, y - 40, f"Total de E-mails: {total_emails}")
        c.drawString(100, y - 60, f"Taxa de Entrega: {taxa_entrega:.2f}%")
        c.drawString(100, y - 80, f"Taxa de Abertura: {taxa_abertura:.2f}%")
        c.drawString(100, y - 100, f"Taxa de Cliques: {taxa_cliques:.2f}%")
        c.drawString(100, y - 120, f"Taxa de Resposta: {taxa_resposta:.2f}%")
        c.drawString(100, y - 140, f"Taxa de Conversão: {taxa_conversao:.2f}%")

        c.save()



    # Agendamento do envio de e-mai
    def show_report():
        print("\nRelatório de E-mails Enviados:")

        for receiver, status in email_status.items():
            status_str = f"Entregue: {status['entregue']}, Aberto: {status['aberto']}, Clicado: {status['clicado']}, Resposta: {status['resposta']}, Conversão: {status.get('conversao', False)}"
            print(f"{receiver}: {status_str}")

        total_emails = len(email_status)
        total_entregues = sum(status['entregue'] for status in email_status.values())
        total_abertos = sum(status['aberto'] for status in email_status.values())
        total_clicados = sum(status['clicado'] for status in email_status.values())

        taxa_entrega = (total_entregues / total_emails) * 100
        taxa_abertura = (total_abertos / total_emails) * 100
        taxa_cliques = (total_clicados / total_emails) * 100

        print("\nResumo do Relatório:")
        print(f"Total de E-mails: {total_emails}")
        print(f"Taxa de Entrega: {taxa_entrega:.2f}%")
        print(f"Taxa de Abertura: {taxa_abertura:.2f}%")
        print(f"Taxa de Cliques: {taxa_cliques:.2f}%")



    # Gerenciamento (menu)

    def menu():
        while True:
            print("\n-----------------------------")
            print("----------- Menu ------------")
            print("-----------------------------")
            print("[ 1 ] Gerenciar e-mails.")
            print("[ 2 ] Agendamento de e-mail.")
            print("[ 3 ] Visualizar conteudo do e-mail.")
            print("[ 4 ] Sair do gerenciamento.")
            choice = input("Escolha uma opção: ").replace(" ", "")[0]

            if choice == "1":
                menu_emails()
                break
            elif choice == "2":

                # Configuração do agendamento de e-mails!

                while True:
                    print("\n-------------------------------")
                    print("------- AGENDAMENTOS ----------")
                    print("-------------------------------")
                    print("Escolha uma opção de agendamento:")
                    print("[ 1 ] Agendamento para hoje!")
                    print("[ 2 ] Agendamento para um dia na semana")
                    print("[ 3 ] Agendamento para um dia no mês")
                    print("[ 4 ] Voltar para o MENU")
                    print("OBS: Agendamentos tem base no mês atual")
                    opcao = str(input("Opção: "))

                    if opcao == "1":
                        hora = str(input("Qual horário? (HH:MM): "))
                        schedule.every().day.at(hora).do(schedule_and_send)
                        print("Agendamento feito!")
                        break

                    elif opcao == "2":
                        while True:
                            dia_semana = str(input("Qual dia da semana? (seg, ter, qua, qui, sex, sab, dom): "))

                            # Mapeia o nome do dia para o método correspondente do schedule
                            dias_da_semana = {
                                'seg': schedule.every().monday,
                                'ter': schedule.every().tuesday,
                                'qua': schedule.every().wednesday,
                                'qui': schedule.every().thursday,
                                'sex': schedule.every().friday,
                                'sab': schedule.every().saturday,
                                'dom': schedule.every().sunday
                            }

                            hora = str(input("Qual horário? (HH:MM): "))

                            if dia_semana.lower() in dias_da_semana:
                                dias_da_semana[dia_semana.lower()].at(hora).do(schedule_and_send)
                                break
                            else:
                                print("Dia da semana inválido.")


                    elif opcao == "3":
                        dia_mes = int(input("Qual dia do mês? (1-31): "))
                        hora = str(input("Qual horário? (HH:MM): "))
                        schedule.every().month.at(f"{dia_mes:02d} {hora}").do(schedule_and_send)
                        print("Agendamento feito!")
                        break
                    elif opcao == "4":
                        
                        menu()
                        break
                    else:
                        print("Opção invalida!")
                        continue
                        

                    while True:
                        schedule.run_pending()
                        time.sleep(60)  # Espera por 1 minuto antes de verificar novamente
                break

            elif choice == "3":

                # Pergunta pro usuario se ele quer ver o e-mail
                while True:
                    global message
                    print(message)

                    alter = str(input("Deseja alguma alteração? [Sim/Nao] ")).replace(" ", "").title()[0]
                    if alter == "S":
                        new_subject = str(input("Qual o assunto do e-mail? "))
                        new_body = str(input("Qual o texto que deseja no e-mail? "))

                        print('---------------------------------')
                        print('---------- NOVO E-MAIL ----------')
                        print('---------------------------------')

                        subject = new_subject
                        body = new_body
                        message = f'From:{sender_name}\nSubject:{subject}\n\n{body}'

                        print(message)
                        print("Mensagem alterada com sucesso!")
         
                        break
                        

                    elif alter == "N":
                        print("Ok!")
        
                        break
                    else:
                        print("Tente novamente, Digite 'Sim' ou 'Nao'.")
                break

            elif choice == "4":
                
                # Confirmação para envio de e-mails!

                while True:

                    confirm_send = str(input("Os destinatarios e o e-mail ja está pronto para envio? [Sim/Não]")).replace(" ", "").title()[0]
                    if confirm_send == "S":
                        send_emails()
                        break
                break
            
            else:
                print("Opção inválida.")
    
    def menu_emails():
        while True:
            
            print("\n---------------------------------------")
            print("--------- Gerenciador E-mails ---------")
            print("---------------------------------------")
            print("[ 1 ] Adicionar endereço de e-mail.")
            print("[ 2 ] Remover endereço de e-mail.")
            print("[ 3 ] Mostrar lista de e-mails.")
            print("[ 4 ] Anexar Imagem Ao e-mail. ")
            print("[ 5 ] Voltar para o MENU.")
            options = input("Escolha uma opção: ").replace(" ", "")[0]

            if options == "1":
                while True:
                    add_email_options = str(input("Deseja adicionar os destinatarios manualmente, a partir de um arquivo ou voltar pro Menu?? [Manualmente/Arquivo/Menu] ")).replace(" ", "").title()

                    if add_email_options == "Manualmente":
                        while True:
                            new_email = input("Digite o novo endereço de e-mail: ").replace(" ", "").lower()
                            
                            if '@gmail.com' in new_email:
                                receivers.append(new_email)
                                print(f"Endereço de e-mail {new_email} adicionado à lista.")

                                while True:
                                    add_emails = str(input("Deseja adicionar mais destinatários? [Sim/Não]: ")).replace(" ", "").title()[0]
                                    if add_emails == "S":
                                        break
                                    elif add_emails == "N":
                                        menu_emails()
                                        break
                                    else:
                                        print("Responda com 'Sim' ou 'Nao', Tente novamente.")

                                break
                    
                            else:
                                print("Endereço invalido, Tente novamente!")
                        break

                    elif add_email_options == "Arquivo":
                        while True:
                            email_list_file = str(input("Digite o nome do arquivo que contém os endereços de e-mail: ")).replace(" ", "").lower()

                            if os.path.isfile(email_list_file):  # Verifica se o arquivo existe.
                                with open(email_list_file, "r") as file:
                                    email_lines = file.readlines()
                                    for line in email_lines:
                                        email = line.strip()  # Remove espaços em branco e quebras de linha
                                        receivers.append(email)
                                        print(f"e-mail: {email}, foi adicionado com sucesso!")
                                break
                            else:
                                print("Arquivo não encontrado, Tente novamente")
                        break
                    elif add_email_options == "Menu":
                        menu()
                        break
                    else:
                        print("Opção Invalida!")
                break
            elif options == "2":

                print("Lista de Destinatários:")
                for i, email in enumerate(receivers):
                    print(f"[{i}] {email}")

                if len(receivers) == 0:
                    print("Sem e-mails adicionados, Volte ao MENU para adicionar!")
                    break

                else:
                    while True:
                        index_to_remove = int(input("Digite o número do endereço de e-mail a ser removido: "))

                        if 0 <= index_to_remove < len(receivers):
                            removed_email = receivers.pop(index_to_remove)
                            print(f"Endereço de e-mail {removed_email} removido da lista.")
                            break
                        else:
                            print("Índice inválido.")
                break
                

            elif options == "3":
                print("Lista de Destinatários:")
                if len(receivers) == 0:
                    print("Sem e-mails adicionados!")
                else:
                    for i, email in enumerate(receivers):
                        print(f"[{i}] {email}")
                break

            elif options == "4":
                
                while True:
                    anex_imagem = str(input("Deseja anexar imagem? [Sim/Nao] ")).replace(" ", "").title()[0]

                    if anex_imagem == "S":
                        while True:
                            imagem = str(input(
                                "Qual o nome do arquivo da imagem com o formato? (Digite 'Voltar' caso queira voltar) ")).replace(
                                " ", "").lower()
                            if os.path.isfile(imagem):

                                # Carregue a imagem a ser anexada

                                with open(imagem, 'rb') as img_file:
                                    img = MIMEImage(img_file.read())

                                # Adicione a imagem ao e-mail

                                img.add_header('Content-Disposition', 'attachment', filename='image.png')
                                msg.attach(img)

                                print("Imagem carregada!")
                                menu_emails()
                                break
                            elif imagem == 'voltar':
                                menu_emails()
                                break
                            else:
                                print("Imagem não encontrada, Tente novamente!")
                        break

                    elif anex_imagem == "N":
                        menu_emails()
                        break

                    else:
                        print("Tente novamente, Digite 'Sim' ou 'Não'.")
                break
            elif options == "5":
                menu()
                break

            else:
                print("Opção invalida.")
    menu()


except smtplib.SMTPAuthenticationError:
    print("Erro de autenticação. Verifique suas credenciais.")
except smtplib.SMTPException as e:
    print(f"Erro SMTP: {e}")
except Exception as e:
    print(f"Outro erro: {e}")
finally:
    server.quit()

print(sends)

if cont == 1:
    print(f"\nFoi enviado apenas {cont} e-mail!")
if cont > 1:
    print(f"\nForam enviados um total de: {cont} e-mails!")