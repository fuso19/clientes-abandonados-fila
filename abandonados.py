'''
PEDRO DAMASCENO
PROGRAMA PARA LER O BANCO DE DADOS, PROCURAR NA TABELA QUAIS USUÁRIOS ABANDONARAM A FILA E
    GERAR UM MAILING COM ESSES USUÁRIOS PARA REPESCAGEM
'''
import pyodbc

# data_inicio =
# data_final =

# FUNÇÃO PARA LEITURA DOS NÚMEROS ABANDONADOS NA FILA


def read(conn):
    print('Read')
    cursor = conn.cursor()
    cursor.execute("select [DateTime], [DialedNumberString], [ANI], [RouterErrorCode], \
        [RouterQueueTime] from [pcce_hds].[dbo].[t_Route_Call_Detail] where DialedNumberString in \
        ('3030') and RouterErrorCode = 448 and RouterQueueTime > 0 and \
        [DateTime] >= '2020-01-04 12:00:00 AM' and [DateTime] <= '2020-01-04 12:00:00 PM' \
        GROUP BY [DateTime], [DialedNumberString], [ANI], [RouterErrorCode], [RouterQueueTime]")

    i = 0
    for row in cursor:
        i = i + 1
        #print(f'row = {row}')
        print('Fila:\t\t' + row[1])
        print('ANI Cliente:\t' + row[2])
        print('Codigo:\t\t' + str(row[3]))
        print('Tempo Aband:\t' + str(row[4]) + '\n')
        gera_arquivo(row[2], i)
    print('\n')


def gera_arquivo(ani, n):
    f = open('PATH TO FILE', 'a+')
    f.write('ABAND' + str(n) + '|' + str(ani) + '|0|0|0|0|0|0|0|0|0\n')


# DADOS DE CONEXÃO AO BANDO DE DADOS DO AW-A
conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server}; \
    Server=SERVERNAME; \
    Database=DATABASENAME; \
    Trusted_Connection=yes;")


read(conn)
conn.close()
