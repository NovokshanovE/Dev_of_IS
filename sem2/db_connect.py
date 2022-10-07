from pymysql import connect

def work_with_db(config):
    conn = connect(**config) #создаем объект соединения
    cursor = conn.cursor() #создаем объект курсор(который хранится в ОП)
    _SQL = """select * from ordering""" #позволяют записать запрос на несколько строчек
    cursor.execute(_SQL)
    #result = cursor.fetchall() #
    #print(cursor.description) #конструкция в которой хранится вся информация о курсоре(для каждого результата вся доп инфа)
    schema = [i[0] for i in cursor.description]
    #print(schema)

    result = []
    for i in cursor.fetchall():
        M_dict = dict(zip(schema,i))
        result.append(M_dict)
    conn.commit() # завершение транзакции (успех)
    cursor.close()
    conn.close()
    return result



if __name__ == '__main__':
    db_config = {'host': '127.0.0.1','user': 'zhenya','password':'12345','database':'restaurant'}
    res = work_with_db(db_config)
    Res = []
    for i in res:

        print(i)
   # print(res)