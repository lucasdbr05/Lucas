import pygame
from pygame.locals import *
import random
import time
import playsound

def escolher_cor_aleatoria():
    pisca_vermelho = {'cor':cor_vermelho,'posição':(251,282),'raio':130}
    pisca_verde = {'cor': cor_verde, 'posição': (251, 282), 'raio': 130}
    pisca_laranja = {'cor': cor_laranja, 'posição': (251, 282), 'raio': 130}
    pisca_azul = {'cor': cor_azul, 'posição': (251, 282), 'raio': 130}
    cores = [pisca_vermelho,pisca_azul,pisca_laranja,pisca_verde]
    return random.choice(cores)


def piscar_cores(lista_cores):
    for cor in lista_cores:
        if cor['cor'] == cor_verde:
            pygame.draw.circle(interface,cor['cor'],cor['posição'],cor['raio'],draw_top_right=True)
        elif cor['cor'] == cor_laranja:
            pygame.draw.circle(interface,cor['cor'],cor['posição'],cor['raio'],draw_bottom_left=True)
        elif cor['cor'] == cor_vermelho:
            pygame.draw.circle(interface,cor['cor'],cor['posição'],cor['raio'],draw_bottom_right=True)
        elif cor['cor'] == cor_azul:
            pygame.draw.circle(interface,cor['cor'],cor['posição'],cor['raio'],draw_top_left=True)
        pygame.display.update()
        time.sleep(0.4)
        interface.blit(Fundo, (0,30)) #retorna à imagem anterior
        pygame.display.update()
        time.sleep(0.4)


def obter_resposta(quantidade_cores):
    resposta_usuario = [] #armazena resposta
    while quantidade_cores > 0:
        for evento in pygame.event.get():
            if evento.type== QUIT:
                quit()
            if evento.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if botao_verde.collidepoint(mouse):
                    resposta_usuario.append(cor_verde)
                    quantidade_cores-=1
                elif botao_laranja.collidepoint(mouse):
                    resposta_usuario.append(cor_laranja)
                    quantidade_cores -= 1
                elif botao_vermelho.collidepoint(mouse):
                    resposta_usuario.append(cor_vermelho)
                    quantidade_cores -= 1
                elif botao_azul.collidepoint(mouse):
                    resposta_usuario.append(cor_azul)
                    quantidade_cores -= 1
    return resposta_usuario


def restart():
    texto_jogar_novamente = fonte_botoes.render('RESTART',True,cor_preto)
    interface.blit(Fundo, (0,30))
    botao_jogar_novamente = pygame.draw.rect(interface, cor_branco, (175,70,155,60))
    interface.blit(texto_jogar_novamente,(176,73))
    pygame.display.update()
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                quit()
            if evento.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if botao_jogar_novamente.collidepoint(mouse):
                    interface.blit(Fundo,(0,30))
                    pygame.display.update()
                    return True



pygame.init() #Inicializa pygame
interface = pygame.display.set_mode((500,530)) # Largura e altura da interface
fonte_botoes = pygame.font.SysFont('Arial',40)
fonte_contagem = pygame.font.SysFont('Arial',30)
barra_status = pygame.Surface((interface.get_width(),30)) #área de contagem de pontos


Fundo =  pygame.image.load('Imagem.png')

#cores
cor_preto = (0,0,0)
cor_branco = (255,255,255)
cor_vermelho = (255,0,0)
cor_verde = (0,255,0)
cor_azul = (0,0,255)
cor_laranja = (255,127,0)


#botoes detectorees de escolha
botao_azul = pygame.draw.circle(interface, cor_azul,center=(251,282),radius=130,draw_top_left=True)
botao_verde = pygame.draw.circle(interface, cor_verde,center=(251,282),radius=130,draw_top_right=True)
botao_vermelho = pygame.draw.circle(interface, cor_vermelho,center=(251,282),radius=130,draw_bottom_right=True)
botao_laranja = pygame.draw.circle(interface, cor_laranja,center=(251,282),radius=130,draw_bottom_left=True)

#textos
texto_comeco = fonte_botoes.render('START',True,cor_preto)
pontos = 0
cores_sequencia = []
jogando = False


#Looping
while not jogando:
    interface.blit(Fundo,(0,30)) #escreve o background
    botao_comecar = pygame.draw.rect(interface,cor_branco,(180,70,150,60)) #Desenha o botao de começo passando as coordenadas de iinicio de final
    interface.blit(texto_comeco,(200,74))
    pygame.display.update() #atualiza a interface para o usuário
    for evento in pygame.event.get(): #para cada clique no usuário
        if evento.type== QUIT:
            quit()
        if evento.type == MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if botao_comecar.collidepoint(mouse):
                jogando =True

interface.blit(Fundo,(0,30))
pygame.display.update()


while jogando:
    barra_status.fill(cor_preto) #sobrescrever o texto antigo para o novo
    pontuacao = fonte_contagem.render('Pontos: '+str(pontos), True, (cor_branco))
    barra_status.blit(pontuacao,(0,0))
    interface.blit(barra_status,(0,0))
    pygame.display.update()
    time.sleep(.5)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            quit()
    cores_sequencia.append(escolher_cor_aleatoria())
    piscar_cores(cores_sequencia)
    resposta_jogador = obter_resposta(len(cores_sequencia))
    sequencia_cores = []
    for cor in cores_sequencia:
        sequencia_cores.append(cor['cor']) #adiciona cores em sequencia a partir da chave cor
    if sequencia_cores == resposta_jogador:
        pontos += 1
    else:
        jogando=restart() #permite a reinicialização do jogo
        if jogando:
            pontos = 0
            cores_sequencia = []
