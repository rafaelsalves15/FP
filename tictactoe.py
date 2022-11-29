#RAFAEL ALVES 199308
def eh_tabuleiro(tab):                  
        #universal -> booleano
        '''Recebe um argumento (tab) de qualquer tipo e devolve True se o seu 
argumento correesponde a um tabuleiro.Senao devolve False.'''

        if type(tab)!=tuple:
                return False
        if len(tab)!=3:
                return False
        for i in range(len(tab)):
                if type(tab[i])!=tuple:
                        return False
                if len(tab[i])!=3:
                        return False
                for x in range(len(tab[i])):         
                        if type(tab[i][x])!=int or abs(tab[i][x])!=1 and tab[i][x]!=0:
                                return False
        return True
                                

def eh_posicao(n):    
        #universal -> booleano
        '''Recebe um argumento (n) de qualquer tipo e devolve True se o 
argumento corresponde a uma posicao do tabuleiro.Senao devolve False.'''

        if type(n)==int and n>=1 and n<=9:
                return True
        return False

def obter_coluna(tab,n):               
        #tabuleiro x inteiro -> vector
        '''Recebe um tabuleiro (tab) e um inteiro (n) ,entre 1 e 3,que 
representa o numero da coluna.Devolve um vetor com os valores da coluna introduzida '''

        if type(n)!=int or n>3 or n<1 or not eh_tabuleiro(tab):
                raise ValueError ('obter_coluna: algum dos argumentos e invalido')
        else:
                return ((tab[0])[n-1]  , (tab[1])[n-1] , (tab[2])[n-1])


def obter_linha(tab,n):                
        #tabuleiro x inteiro -> vector
        '''Recebe um tabuleiro (tab) e um inteiro (n) ,entre 1 e 3,que 
representa o numero da linha.Devolve um vetor com os valores da linha introduzida'''
        
        if type(n)!=int or n>3 or n<1 or not eh_tabuleiro(tab):
                raise ValueError ('obter_linha: algum dos argumentos e invalido')
        else:
                return (tab[n-1])

def obter_diagonal(tab,n):            
        #tabuleiro x inteiro -> vector
        '''Recebe um tabuleiro (tab) e um inteiro (n) ,entre 1 e 2,que 
representa a direcao da diagonal,onde 1 representa a diagonal descendente da 
esquerda para a direita e 2 representa a diagonal ascendente da esquerda para 
a direitra.Devolve um vetor com os valores dessa diagonal'''
 
        if type(n)!=int or n<1 or n>2 or not eh_tabuleiro(tab):
                raise ValueError ('obter_diagonal: algum dos argumentos e invalido') 
        else:
                if n==1:
                        return (tab[0][0],tab[1][1],tab[2][2])
                        
                else:
                        return (tab[2][0],tab[1][1],tab[0][2])   

def tabuleiro_str(tab):            
        #tabuleiro -> cad. carateres
        '''Recebe um tabuleiro(tab) e devolve a cadeira de carateres que o representa'''
        
        representacao_do_tab=''
        if not eh_tabuleiro(tab):
                raise ValueError('tabuleiro_str: o argumento e invalido')
        for i in range(len(tab)):
                contador=0
                for elemento in tab[i]:
                        contador=contador+1
                        if elemento==-1:
                                representacao_do_tab=representacao_do_tab + ' O '
                        elif elemento==0:
                                representacao_do_tab=representacao_do_tab + '   '
                        elif elemento==1:
                                representacao_do_tab=representacao_do_tab + ' X '
                        if contador < 3:
                                representacao_do_tab=representacao_do_tab + '|'
                                                       
                if i<2:
                        representacao_do_tab=representacao_do_tab+ '\n-----------\n'                             
        return representacao_do_tab  

def eh_posicao_livre(tab,n):           
        #tabuleiro x posicao -> booleano
        '''Recebe um tabuleiro (tab) e uma posicao (n) e devolve True caso 
        a posicao introduzida corresponda a uma posicao livre do tabuleiro,
        caso contrario devolve False'''

        if not eh_posicao(n) or not eh_tabuleiro(tab):   
                raise ValueError ('eh_posicao_livre: algum dos argumentos e invalido')
        else:
                valorlogico=False
                if n<=3:
                        if tab[0][n-1]==0:
                                valorlogico=True
                        else:
                                valorlogico=False
                elif 3<n and n<=6:
                        if tab[1][n-4]==0:
                                valorlogico=True 
                        else:
                                valorlogico=False
                else:
                        if tab[2][n-7]==0:
                                valorlogico=True
                        else:
                                valorlogico=False      
        return valorlogico

def obter_posicoes_livres(tab):          
        #tabuleiro -> vector 
        '''Recebe um tabuleiro(tab) e devolve um vector ordenado com as posicoes 
        livres do tabuleiro'''
          
        if not eh_tabuleiro(tab):
                raise ValueError ('obter_posicoes_livres: o argumento e invalido')
        else:
                resultado=()
                for i in range(1,10):
                        if eh_posicao_livre(tab,i):
                                resultado=resultado + (i,)
        return resultado

def jogador_ganhador(tab):              
        #tabuleiro -> inteiro
        '''Recebe um tabuleiro(tab) e devolve um numero inteiro que indica 
o jogador que ganhou o jogo,sendo o numero referido igual a 1 caso o jogador 
ganhador jogar com 'X',igual a -1 caso o jogador ganhador seja o que 
joga com 'O' ou 0 se nao houver vencedor. '''
 
        if not eh_tabuleiro(tab):
                raise ValueError ('jogador_ganhador: o argumento e invalido')
        else:
                for i in range(1,4):
                        if obter_linha(tab,i)==(1,1,1):
                                return 1
                        elif obter_linha(tab,i)==(-1,-1,-1):
                                return -1
                        elif obter_coluna(tab,i)==(1,1,1):
                                return 1
                        elif obter_coluna(tab,i)==(-1,-1,-1):
                                return -1
                for i in range(1,3):
                        if obter_diagonal(tab,i)==(1,1,1):
                                return 1 
                        if obter_diagonal(tab,i)==(-1,-1,-1):
                                return -1
                return 0
 
def marcar_posicao(tab,k,n):           
        #tabuleiro x inteiro x posicao -> tabuleiro
        '''Recebe um tabuleiro(tab), um inteiro (k)-que corresponde ao jogador 
que ira fazer a jogada(1 para jogador 'X' ,-1 para jogador 'O')- e um inteiro(n)
que corresponde a  uma posicao livre onde o jogador k ira jogar.'''


        if not eh_tabuleiro(tab)  or type(k)!=int or  k<-1 or k>1 or k==0 \
           or not eh_posicao(n) or not eh_posicao_livre(tab,n):
                raise ValueError ('marcar_posicao: algum dos argumentos e invalido')
        novo_tab=() 
        if n<=3:       
                novo_tab=novo_tab+((tab[0][:n-1]+(k,)+tab[0][n:]),(tab[1]),(tab[2]))             
        elif 3<n and n<=6:
                novo_tab=novo_tab+((tab[0]),(tab[1][:n-4]+(k,)+tab[1][n-3:]),(tab[2]))      
        else:
                novo_tab=novo_tab+((tab[0]),(tab[1]),(tab[2][:n-7]+(k,)+tab[2][n-6:]))
        
        #Criar um novo tuplo com a posicao n alterada para k
        #Fazendo um if para cada linha pois os tabuleiros estao representados  
        #por um tuplo com 3 tuplos,onde cada um corresponde a uma linha.
        return novo_tab

def escolher_posicao_manual(tab):           
        #tabuleiro -> posicao
        '''Esta funcao faz a leitura de uma posicao introduzida manualmente
        pelo jogador humano,devolvendo essa mesma posicao.  '''
 
        if not eh_tabuleiro(tab) :
                raise ValueError ('escolher_posicao_manual: o argumento e invalido')
        posicao_escolhida=eval(input('Turno do jogador. Escolha uma posicao livre: '))
        if not eh_posicao(posicao_escolhida):  
                raise ValueError ('escolher_posicao_manual: a posicao introduzida e invalida')
        if not eh_posicao_livre(tab,posicao_escolhida):
                raise ValueError ('escolher_posicao_manual: a posicao introduzida e invalida')
        return posicao_escolhida
  
def formulas(i):
        #posicao -> linha da posicao x coluna da posicao
        '''estas funcao recebe uma posicao(i) e ,utilizando formulas, devolve
o numero da linha e da coluna da posicao introduzida'''
        linha_de_i = 1 +((i-1)//3)
        coluna_de_i = i -(((i-1)//3)*3)   
        return linha_de_i, coluna_de_i     

def vitoria(tab,jogador): 
        #tabuleiro x jogador -> posicao
        '''Recebe um tabuleiro(tab) e um inteiro(jogador) que indica um jogador
e devolve a posicao onde o jogador ,que foi passado como argumento,tera de jogar
para vencer.Se nao for possivel vencer a funcao devolve False'''
        
        for i in (obter_posicoes_livres(tab)):
  
                linha_de_i, coluna_de_i = formulas(i)
                
                if sum(obter_linha(tab, linha_de_i)) == 2 * jogador:
                        return i
                if sum(obter_coluna(tab, coluna_de_i)) == 2 * jogador:
                        return i
                if i == 1 or i == 5 or i == 9:
                        if sum(obter_diagonal(tab, 1)) == 2 * jogador:
                                return i
                if i == 3 or i == 5 or i == 7:
                        if sum(obter_diagonal(tab, 2)) == 2 * jogador:
                                return i
        return False

  
def bloqueio(tab,jogador):
        #tabuleiro x jogador -> posicao
        '''Recebe um tabuleiro(tab) e um inteiro(jogador) que indica um jogador
e devolve a posicao onde o jogador ,que foi passado como argumento,tera de jogar
para bloquear a vitoria ao adversario.Se nao for possivel bloquear a funcao 
devolve False '''
        return vitoria(tab,-jogador)
        

def bifurcacao(tab,jogador):
        #tabuleiro x jogador -> posicao
        '''Recebe um tabuleiro(tab) e um inteiro(jogador) que representa um
jogador e devolve a posicao onde o jogador tera de jogar para fazer uma bifurcacao'''
        
        for i in ( obter_posicoes_livres(tab) ):
                linha_de_i,coluna_de_i=formulas(i)
  
                if sum(obter_linha(tab,linha_de_i))==jogador \
                   and sum(obter_coluna(tab,coluna_de_i))==jogador:             
                        return i
                #bifurcacao entre linhas e colunas
                if i==1 or i==5 or i==9:
                        if sum(obter_diagonal(tab,1))==jogador \
                           and ( sum(obter_linha(tab,linha_de_i))==jogador \
                                 or sum(obter_coluna(tab,coluna_de_i))==jogador):     
                                return i
               #bifurcacao entre uma linha ou uma coluna e a diagonal 1
                if i==3 or i==5 or i==7:
                        if sum(obter_diagonal(tab,2))==jogador \
                           and ( sum(obter_linha(tab,linha_de_i))==jogador \
                                 or sum(obter_coluna(tab,coluna_de_i))==jogador):     
                                return i                        
                #bifurcacao entre uma linha ou uma coluna e a diagonal 2
        return False

def dois_em_linha(tab,jogador):
        #tabuleiro x jogador -> lista 
        '''Recebe um tabuleiro(tab) e um inteiro(jogador) que representa um
jogador e devolve uma lista com as posicoes onde o jogador introduzido consegue
fazer um dois em linha.'''
        
        lista=[]
        for i in (obter_posicoes_livres(tab)):
  
                linha_de_i, coluna_de_i = formulas(i)
                
                if sum(obter_linha(tab, linha_de_i)) ==  jogador:
                        lista=lista+[i]
                if sum(obter_coluna(tab, coluna_de_i)) == jogador:
                        lista=lista+[i]
                if i == 1 or i == 5 or i == 9:
                        if sum(obter_diagonal(tab, 1)) == jogador:
                                lista=lista+[i]
                                
                if i == 3 or i == 5 or i == 7:
                        if sum(obter_diagonal(tab, 2)) == jogador:
                                lista=lista+[i]
        return lista      


def bloqueio_bifurcacao(tab,jogador):
        #tabuleiro x jogador -> posicao 
        '''Recebe um tabuleiro(tab) e um inteiro(jogador) que identifica 
um jogador e devolve a posicao onde o jogador tera de jogar para bloquear a 
bifurcacao do adversario. Caso o oponente tenha mais do que uma bifurcacao
a funcao devolve a posicao onde se deve jogar para fazer um dois em linha
,obrigandoo adversario a defender( desta jogada nao pode resultar uma bifurcacao
para o adversario.).'''
        
        
        intersecoes=[]
        for i in ( obter_posicoes_livres(tab) ):
                linha_de_i,coluna_de_i=formulas(i)
  
                if sum(obter_linha(tab,linha_de_i))==-jogador \
                   and sum(obter_coluna(tab,coluna_de_i))==-jogador:            
                        intersecoes=intersecoes+ [i]
                
                if i==1 or i==5 or i==9:
                        if sum(obter_diagonal(tab,1))==-jogador \
                           and ( sum(obter_linha(tab,linha_de_i))==-jogador \
                                 or sum(obter_coluna(tab,coluna_de_i))==-jogador):    
                                intersecoes=intersecoes+ [i]

                if i==3 or i==5 or i==7:
                        if sum(obter_diagonal(tab,2))==-jogador \
                           and ( sum(obter_linha(tab,linha_de_i))==-jogador \
                                 or sum(obter_coluna(tab,coluna_de_i))==-jogador):     
                                
                                intersecoes=intersecoes+ [i]
        if len(intersecoes)==1:
                return bifurcacao(tab,-jogador)
        if len(intersecoes)==0:
                return False
        else:
                for i in (dois_em_linha(tab, jogador)):
                        tab_simulada = marcar_posicao(tab, jogador, i)
                        b = bloqueio(tab_simulada, -jogador)
                        while b not in intersecoes and b != False:
                                return i                
                                         
def centro(tab):
        #tabuleiro -> 5
        '''Recebe um tabuleiro(tab) e devolve o inteiro 5, caso o centro do 
tabuleiro (quinta posicao) estiver livre e for possivel jogar nele.Se isto nao 
se verificar devolve False'''
        
        if tab[1][1]==0:
                return 5
        return False

def canto_oposto(tab,jogador):
        #tabuleiro x jogador -> posicao
        ''' Recebe um tabuleiro(tab) e um inteiro (jogador) que identifica um 
jogador.Se um canto estiver ocupado pelo adversario, devolve a posicao do canto 
oposto,caso este esteja vazio.Senao devolve False. '''
        if tab[0][0]==-jogador and tab[2][2]==0:
                return 9
        if tab[0][2]==-jogador and tab[2][0]==0:
                return 7
        if tab[2][0]==-jogador and tab[0][2]==0:
                return 3
        if tab[2][2]==-jogador and tab[0][0]==0:
                return 1
        return False

def canto_vazio(tab):
        #tabuleiro -> posicao
        '''Recebe um tabuleiro(tab) e devolve a posicao de um canto vazio.Se nao
        existirem cantos vazios devolve False.''' 
        cantos=(1,3,7,9)
        for i in cantos:
                if eh_posicao_livre(tab,i):
                        return i
        return False

def lateral_vazio(tab):
        #tabuleiro -> posicao
        ''' Recebe um tabuleiro(tab) e devolve a posicao de um lateral vazio.Se 
nao existirem laterais vazios devolve False'''
        laterais=(2,4,6,8)
        for i in laterais:
                if eh_posicao_livre(tab,i):
                        return i
        return False


def escolher_posicao_auto(tab,jogador,estrategia):    
        #tabuleiro x inteiro x cad.carateres -> posicao
        '''Recebe um tabuleiro(tab), um inteiro (jogador) que identifica um 
jogador(1 para jogador 'X', -1 para jogador 'O') e uma cadeia de carateres 
correspondente a estrategia que ira ser utilizada pelo computador.  '''
        
        if not eh_tabuleiro(tab)  or type(jogador)!=int or \
           abs(jogador)!=1 or ( estrategia!='basico'\
           and estrategia!='normal' and estrategia!='perfeito' ): 
                raise ValueError ('escolher_posicao_auto: algum dos argumentos e invalido')
        
        if estrategia=='basico':
                fimdejogada=False
                if fimdejogada==False:
                        fimdejogada=centro(tab)
                if fimdejogada==False:
                        fimdejogada=canto_vazio(tab)
                if fimdejogada==False:                                        
                        fimdejogada=lateral_vazio(tab)
                return fimdejogada

        if estrategia=='normal':                
                fimdejogada=False
                if fimdejogada==False:
                        fimdejogada=vitoria(tab,jogador)
                if fimdejogada==False:
                        fimdejogada=bloqueio(tab,jogador)
                if fimdejogada==False:
                        fimdejogada=centro(tab)
                if fimdejogada==False:
                        fimdejogada=canto_oposto(tab,jogador)
                if fimdejogada==False:
                        fimdejogada=canto_vazio(tab)
                if fimdejogada==False:
                        fimdejogada=lateral_vazio(tab)
                return fimdejogada
                 
        if estrategia=='perfeito':
                fimdejogada=False
                if fimdejogada==False:
                        fimdejogada=vitoria(tab,jogador)
                if fimdejogada==False:
                        fimdejogada=bloqueio(tab,jogador)
                if fimdejogada==False:
                        fimdejogada=bifurcacao(tab,jogador)
                if fimdejogada==False:
                        fimdejogada=bloqueio_bifurcacao(tab,jogador)                
                if fimdejogada==False:
                        fimdejogada=centro(tab)
                if fimdejogada==False:
                        fimdejogada=canto_oposto(tab,jogador)
                if fimdejogada==False:
                        fimdejogada=canto_vazio(tab)
                if fimdejogada==False:
                        fimdejogada=lateral_vazio(tab)
                return fimdejogada
        
def jogo_do_galo(letra,estrategia):             
        #cad. carateres x cad carateres -> cad. carateres 
        ''' Esta funcao permite jogar o jogo do galo completo(humano vs computador).
O primeiro jogador a jogar e sempre aquele que joga com  'X',podendo este ser 
o computador ou o humano.

O jogo acaba quando existir um vencedor, ou quando se der 
um empate, estando todas as posicoes do tabuleiro preenchidas.Quando o jogo 
acabar a funcao devolve a letra do jogador vencedor, ou em caso de empate 
devolve a cadeia de carateres 'EMPATE' .

A funcao recebe duas cadeias de carateres sendo que a primeira destas (letra) 
identifica a letra com a qual o jogador humano jogara ('X' ou 'O'), e a 
segunda(estrategia) identifica a estrategia que 
ira ser utilizada pelo computador durante a partida.'''
        
               
        if (letra!='O' and letra!='X') or (estrategia!='basico' and \
                estrategia!='normal' and estrategia!='perfeito'):
                raise ValueError('jogo_do_galo: algum dos argumentos e invalido')
        
        tab=((0,0,0),(0,0,0),(0,0,0))
        
        if letra=='X':
                jogador_atual='humano'
                jogador=1
        else:
                jogador_atual='computador'
                jogador=1
        
        print("Bem-vindo ao JOGO DO GALO.")
        print("O jogador joga com '"+letra+"'.")
        
        while len(obter_posicoes_livres(tab))!=0 and jogador_ganhador(tab)==0:
                if jogador_atual=='humano':  
                        tab=marcar_posicao(tab,jogador,escolher_posicao_manual(tab))
                        print(tabuleiro_str(tab))
                        jogador_ganhador(tab)
                        jogador_atual='computador'
                        jogador=-jogador
                
                if len(obter_posicoes_livres(tab))!=0 and \
                   jogador_atual=='computador' and jogador_ganhador(tab)==0:  
                        tab= marcar_posicao(tab,jogador,escolher_posicao_auto(tab,jogador,estrategia))
                        print('Turno do computador ('+estrategia+'):' )
                        print(tabuleiro_str(tab))
                        jogador_ganhador(tab)
                        jogador_atual='humano'
                        jogador=-jogador
                        
        if len(obter_posicoes_livres(tab))==0 and jogador_ganhador(tab)==0 :
                return('EMPATE')
        if jogador_ganhador(tab)==1:
                return('X')
        if jogador_ganhador(tab)==-1:
                return('O')                        