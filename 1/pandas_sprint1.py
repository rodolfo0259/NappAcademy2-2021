import pickle
import pandas as pd

with open('lista.bin', 'rb') as list_in_file:
    lista = pickle.load(list_in_file)

df = pd.DataFrame(lista,
        columns=[
            'Nome',
            'CPF',
            'email',
            'data_hora',
            'hostname',
            'IP',
            'dados_navegador',
            'endereco',
            'cartao_credito',
            'expire_date'
            ])

# tarefa 1 e 2
df['start_dr'] = (df['Nome'].str.lower()).str.startswith('dr') # dr dra
df_dr_dra = df.loc[df['start_dr'] == True]
tuple_df = (df_dr_dra.apply(tuple, axis=1)).values.tolist()
# print(tuple_df)
# print(type(tuple_df))

# tarefa 3 e 4
df['start_only_dr'] = (df['Nome'].str.lower()).str.startswith('dr.') # dr
df_dr = df.loc[df['start_only_dr'] == True]
tuple_df = (df_dr.apply(tuple, axis=1)).values.tolist()

# tarefa 5 e 6
df['start_dra'] = (df['Nome'].str.lower()).str.startswith('dra') # dra
df_dra = df.loc[df['start_dra'] == True]
tuple_df = (df_dra.apply(tuple, axis=1)).values.tolist()


# print(df)
# tuple_df = df.apply(tuple, axis=1)
# print(tuple_df)
# df.to_csv('df.csv', sep=';')