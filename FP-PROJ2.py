#RAFAEL ALVES 199308
def cria_posicao(c,l):
    if type(c)!=str or type(l)!=str or c not in ['a','b','c'] or \
       l not in['1','2','3']:
        raise ValueError ('cria_posicao: argumentos invalidos')
    return [c,eval(l)]

def cria_copia_posicao(p):
    return [p[0],p[1]]

def obter_pos_c(p):
    return p[0]
def obter_pos_l(p):
    return str(p[1])

def eh_posicao(arg):
    if type(arg)!=list or type(arg[0])!=str or type(arg[1])!=int or \
       arg[0] not in ['a','b','c'] or 3<arg[1] or arg[1]<1:
        return False
    return True
    
def posicoes_iguais(p1,p2):
    if p1==p2:
        return True
    return False

def posicao_para_str(p):
    return str(p[0])+str(p[1])

def obter_posicoes_adjacentes(p):
    tuplo=()  
    #CENTRO DO TABULEIRO:
    if p == ['b', 2]:   
        m=(cria_posicao('a', '1'), cria_posicao('b', '1'),\
    cria_posicao('c', '1'),cria_posicao('a', '2'),cria_posicao('c','2'),\
    cria_posicao('a','3'),cria_posicao('b','3'),cria_posicao('c','3'))
    
    #CANTOS DO TABULEIRO:
    elif obter_pos_l(p) in ['1','3'] and obter_pos_c(p) in ["a", "c"]: 
        m=(cria_posicao('b','2'),cria_posicao('b', obter_pos_l(p))\
            ,cria_posicao(obter_pos_c(p), '2'))
    
    #LATERAIS DO TABULEIRO:
    elif obter_pos_l(p) in ['1','2','3'] and obter_pos_c(p) in ['a','b','c']:
        if obter_pos_c(p) == 'b': #LATERAIS NA COLUNA B
            m=(cria_posicao('b', '2'), cria_posicao('a', obter_pos_l(p)),\
                cria_posicao('c',obter_pos_l(p)))
        if obter_pos_l(p) == '2': #LATERAIS NA LINHA 2 
            m=(cria_posicao('b', '2'), cria_posicao(obter_pos_c(p),'1'),\
                 cria_posicao(obter_pos_c(p),'3'))  
    for l in [1,2,3]:
        for c in ['a','b','c']:
            if [c,l] in m:
                tuplo+=([c,l],)       
    return tuplo

def cria_peca(s):
    if s!='X' and s!='O' and s!=' ':
        raise ValueError ('cria_peca: argumento invalido')
    return [s]

def cria_copia_peca(j):
    return  [j[0]]      

def eh_peca(arg):
    if arg in [['X'],['O'],[' '],'[X]','[O]','[ ]']:    
        return True
    return False 

def pecas_iguais(j1,j2):
    if j1==j2 and eh_peca(j1) and eh_peca(j2):
        return True
    return False

def peca_para_str(j):
    x=str(j[0])
    return '[' + x + ']' 

def peca_para_inteiro(j):
    if pecas_iguais(cria_copia_peca(j),['X']):
        return 1
    elif pecas_iguais(cria_copia_peca(j),['O']):
        return -1
    elif pecas_iguais(cria_copia_peca(j),[' ']):
        return 0
    
def cria_tabuleiro():
    return [ [' ']*3,[' ']*3,[' ']*3] 

def cria_copia_tabuleiro(t):
    copia = []
    for lista in t:
        sublista = []
        for posicao in lista:
            sublista.append(posicao)
        copia.append(sublista)
    return copia
    
def index_posicoes(p):
    index=[None,None]
    index[0]=int(obter_pos_l(p))-1
    if obter_pos_c(p)=='a':
        index[1]=0
    elif obter_pos_c(p)=='b':
        index[1]=1
    elif obter_pos_c(p)=='c':
        index[1]=2  
    return index

def index_pos2(l):
    pos=[None,None]
    if obter_pos_l(l)=='0':
        pos[0]='a'
    if obter_pos_l(l)=='1':
        pos[0]='b'
    if obter_pos_l(l)=='2':
        pos[0]='c'
    pos[1]=l[0]+1
    return pos

    
def obter_peca(t,p):
    index=index_posicoes(p)
    if cria_peca(t[index[0]][index[1]])==cria_peca('X'):
        return cria_peca('X')
    elif cria_peca(t[index[0]][index[1]])==cria_peca('O'):
        return cria_peca('O')
    elif cria_peca(t[index[0]][index[1]])==cria_peca(' '):
        return cria_peca(' ') 

def obter_vetores_iguais(v1,v2):
    if len(v1)!=len(v2):
        return False
    for i in range(len(v1)):
        if not pecas_iguais(v1[i],v2[i]):
            return False
    return True


def obter_vetor(t,s):
    if s=='1':
        return (cria_peca(t[0][0]),cria_peca(t[0][1]),cria_peca(t[0][2])) 
    if s=='2':
        return (cria_peca(t[1][0]),cria_peca(t[1][1]),cria_peca(t[1][2]))
    if s=='3':
        return (cria_peca(t[2][0]),cria_peca(t[2][1]),cria_peca(t[2][2]))
    if s=='a':
        return (cria_peca(t[0][0]),cria_peca(t[1][0]),cria_peca(t[2][0]))
    if s=='b':
        return (cria_peca(t[0][1]),cria_peca(t[1][1]),cria_peca(t[2][1]))
    if s=='c':
        return (cria_peca(t[0][2]),cria_peca(t[1][2]),cria_peca(t[2][2]))

def coloca_peca(t,j,p):
    j=j[0]
    index=index_posicoes(p)
    t[index[0]][index[1]]=j
    return t 

def remove_peca(t,p):
    index=index_posicoes(p)
    t[index[0]][index[1]]=' '
    return t

def move_peca(t,p1,p2):
    peca=obter_peca(t,p1)
    remove_peca(t,p1)
    coloca_peca(t,peca,p2)
    return t

def eh_tabuleiro(arg):
    if type(arg)!=list or len(arg)!=3 or len(arg[0])!=3 or len(arg[1])!=3 \
       or len(arg[2])!=3:
        return False
    for linha in [0,1,2]:
        for coluna in [0,1,2]:
            if cria_peca(arg[linha][coluna])!=cria_peca('X') and cria_peca(arg[linha][coluna])!=cria_peca('O')\
               and cria_peca(arg[linha][coluna])!=cria_peca(' '):
                return False               
    contX,contO,vencedor=0,0,0
    for x in range(len(arg)):
        for index in arg[x]:
            if pecas_iguais(cria_peca(index),cria_peca('X')):
                contX+= 1 
            if pecas_iguais(cria_peca(index),cria_peca('O')):
                contO+= 1
    for i in ['a','b','c','1','2','3']:
        if obter_vetor(arg,i) in [(cria_peca('X'),cria_peca('X'),cria_peca('X')),\
                                (cria_peca('O'),cria_peca('O'),cria_peca('O'))]:
            vencedor+=1
    if abs(contX - contO)>1 or contX>3 or contO>3 or vencedor>1:
        return False
    return True

def eh_posicao_livre(t,p):
    if pecas_iguais(obter_peca(t,p),cria_peca(' ')):
        return True
    return False

def tabuleiros_iguais(t1,t2):
    if not eh_tabuleiro(t1) or not eh_tabuleiro(t2):
        return False
    for l in range(len(t1)):
        for c in range(len(t1[l])):
            if not pecas_iguais([t1[l][c]],[t2[l][c]]):
                return False
    return True
    
                                    
def tabuleiro_para_str(t):
    return('   a   b   c\n'
    '1 [{t[0][0]}]-[{t[0][1]}]-[{t[0][2]}]\n'
    '   | \ | / |\n'
    '2 [{t[1][0]}]-[{t[1][1]}]-[{t[1][2]}]\n'
    '   | / | \ |\n'
    '3 [{t[2][0]}]-[{t[2][1]}]-[{t[2][2]}]'.format(t=t))

def inteiro_input_peca(jogador):
    if jogador==1:
        return 'X'
    if jogador==-1:
        return 'O'
    if jogador==0:
        return ' '
    
def tuplo_para_tabuleiro(t):
    lista=[]
    for i in range(len(t)):
        for elem in t[i]:
            lista+=[inteiro_input_peca(elem),]
    return [lista[:3],lista[3:6],lista[6:]]

def obter_ganhador(t):
    for s in ['a','b','c','1','2','3']:
        if obter_vetores_iguais(obter_vetor(t,s),(cria_peca('X'),cria_peca('X'),cria_peca('X'))):
            return cria_peca('X')
        if obter_vetores_iguais(obter_vetor(t,s),(cria_peca('O'),cria_peca('O'),cria_peca('O'))):
            return cria_peca('O')
    return cria_peca(' ')

def obter_posicoes_livres(t):
    tuplo=()
    for i in range(len(t)):
        for elem in range(3):
            if pecas_iguais(obter_peca(t,index_pos2([i,elem])),cria_peca(' ')):
                tuplo += (index_pos2([i,elem]),)
    return tuplo 

def obter_posicoes_jogador(t,j):
    tuplo=()
    for i in range(len(t)):
        for elem in range(3):
            if pecas_iguais(obter_peca(t,index_pos2([i,elem])),j):
                tuplo += (index_pos2([i,elem]),)
    return tuplo 

def intvec(v):
    return (peca_para_inteiro(v[0]),peca_para_inteiro(v[1]),peca_para_inteiro(v[2]))

def vitoria(t,jogador):
    l=['a','b','c']
    for i in ['a','b','c']:
        if sum(intvec(obter_vetor(t,i)))==2*peca_para_inteiro(jogador):
            for x in [0,1,2]:
                if pecas_iguais(obter_vetor(t,i)[x],cria_peca(' ')):
                    return [i,x+1]
    for i in ['1','2','3']:
        if sum(intvec(obter_vetor(t,i)))==2*peca_para_inteiro(jogador):
            for y in [0,1,2]:
                if pecas_iguais(obter_vetor(t,i)[y],cria_peca(' ')):
                    return cria_posicao(l[y],i)
    return False

def outro_jogador(j):
    if pecas_iguais(j,cria_peca('X')):
        return cria_peca('O')
    if pecas_iguais(j,cria_peca('O')):
        return cria_peca('X')

def bloqueio(t,j):
    return vitoria(t,outro_jogador(j)) 

def centro(t):
    if eh_posicao_livre(t,cria_posicao('b','2')):
        return cria_posicao('b','2')    
    return False

def canto_vazio(t):
    for i in (cria_posicao('a','1'),cria_posicao('c','1'),\
              cria_posicao('a','3'),cria_posicao('c','3')):
        if eh_posicao_livre(t,i):
            return i 
    return False

def lateral_vazio(t):
    for i in (cria_posicao('b','1'),cria_posicao('a','2'),\
              cria_posicao('c','2'),cria_posicao('b','3')):
        if eh_posicao_livre(t,i):
            return i 
    return False

def minimax(t, jog, prof, seq):
    melhor_seq_movimentos = ()
    if obter_ganhador(t) in [ cria_peca('X'), cria_peca('O') ] or prof == 0:
        return peca_para_inteiro(obter_ganhador(t)), seq
    else:
        melhor_resultado = peca_para_inteiro(outro_jogador(jog))
        for posicao_mov in obter_posicoes_jogador(t,jog):
            for posicao_adj in obter_posicoes_adjacentes(posicao_mov):
                if posicao_adj in obter_posicoes_livres(t):
                    tab = cria_copia_tabuleiro(t)
                    tab2 = move_peca(tab, posicao_mov, posicao_adj)
                    jj = seq + (posicao_mov, posicao_adj)
                    novo_resul, nova_seq = minimax(tab2, outro_jogador(jog),\
                                                   prof - 1, jj)
                    
                    if melhor_seq_movimentos==() or (jog == ['X'] \
                                and novo_resul > melhor_resultado) or \
                            (jog == ['O'] and novo_resul < melhor_resultado):
                        melhor_resultado, melhor_seq_movimentos = novo_resul, nova_seq
        return melhor_resultado, melhor_seq_movimentos

def obter_movimento_manual(t,j):
    if len(obter_posicoes_livres(t))>3:
        pos=input('Turno do jogador. Escolha uma posicao: ')
        if  pos[0] not in ['a','b','c'] or pos[1] not in ['1','2','3'] or len(pos)!=2 or not eh_posicao_livre(t,cria_posicao(pos[0],pos[1])) :
            raise ValueError ('obter_movimento_manual: escolha invalida')
        return (pos,)
    
    pos=input('Turno do jogador. Escolha um movimento: ')
    if len(pos)!=4 or pos[0] not in ['a','b','c'] or pos[1] not in ['1','2','3'] \
       or pos[2] not in ['a','b','c'] or pos[3] not in ['1','2','3'] \
       or not eh_posicao(cria_posicao(pos[0],pos[1]))\
       or not pecas_iguais(peca_para_str(obter_peca(t,cria_posicao(pos[0],pos[1]))),peca_para_str(j)) \
       or not( eh_posicao_livre(t,cria_posicao(pos[2],pos[3])) \
       or posicoes_iguais(cria_posicao(pos[0],pos[1]),cria_posicao(pos[2],pos[3]))):
        raise ValueError ('obter_movimento_manual: escolha invalida')
    return (pos[:2],pos[2:])

def estrategias(t,j):
    fimdejogada=vitoria(t,j)
    if fimdejogada==False:
        fimdejogada=bloqueio(t,j)
        if fimdejogada==False:
            fimdejogada=centro(t)
            if fimdejogada==False:
                fimdejogada=canto_vazio(t)
                if fimdejogada==False:
                    fimdejogada=lateral_vazio(t)
    return fimdejogada


def obter_movimento_auto(t,j,str1):
    seq=()
    if str1=='facil':    
        if len(obter_posicoes_livres(t))>3:
            return (estrategias(t,j),)
        else:
            for posicao in obter_posicoes_jogador(t,j):
                for posicao2 in obter_posicoes_adjacentes(posicao):
                    if posicao2 in obter_posicoes_livres(t):
                        return (posicao,posicao2)           
    if str1=='normal':
        if len(obter_posicoes_livres(t))>3:
            return (estrategias(t,j),)
        else:
            minimax2=minimax(t,j,1,seq)
            return minimax2[1][0],minimax2[1][1]
    if str1=='dificil':
        if len(obter_posicoes_livres(t))>3:
            return (estrategias(t,j),)
        else:
            minimax2=minimax(t,j,5,seq)
            return (minimax2[1][0],minimax2[1][1])


def moinho(str1,str2):
    if str2 not in ['facil','normal','dificil'] or (str1!='[X]' and str1!='[O]'):
        raise ValueError ('moinho: argumentos invalidos')
    if str1=='[X]':
        computador=cria_peca('O')
        jogador_humano=cria_peca('X')
        jogador_atual=jogador_humano
        
    if str1=='[O]':
        computador=cria_peca('X')
        jogador_humano=cria_peca('O')
        jogador_atual=computador
        
    print ('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade {n}.'.format(n=str2))
    print(tabuleiro_para_str(cria_tabuleiro()))
    t=cria_tabuleiro()
    
    while pecas_iguais(obter_ganhador(t), cria_peca(' ')):
        if pecas_iguais(jogador_atual,jogador_humano):
            posicao=obter_movimento_manual(t,jogador_humano)
            if len(obter_posicoes_livres(t))>3:
                t=coloca_peca(t,jogador_humano,posicao[0])
            else:
                t=move_peca(t,posicao[0],posicao[1])
            print(tabuleiro_para_str(t))
        else:
            posicao=obter_movimento_auto(t,computador,str2)
            if len(obter_posicoes_livres(t))>3:
                t=coloca_peca(t,computador,posicao[0])
            else:
                t=move_peca(t,posicao[0],posicao[1])
            print('Turno do computador ({n}):'.format(n=str2))
            print(tabuleiro_para_str(t))
        
        if pecas_iguais(jogador_atual,jogador_humano):
            jogador_atual=computador
        elif pecas_iguais(jogador_atual,computador):
            jogador_atual=jogador_humano
    return peca_para_str(obter_ganhador(t))