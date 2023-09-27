import streamlit as st

st.set_page_config(page_title='Calculador de Preços')

with st.form('Calculo de Preços'):
    col1, col2, col3 = st.columns(3)

    with col1:
        valor_milho = st.text_input(label='Valor do Milho', value=0)
        valor_açucar = st.text_input(label='Valor do Açucar', value=0)
        valor_chocolate = st.text_input(label='Valor do Chocolate', value=0)
        valor_ninho = st.text_input(label='Valor do Leite em pó', value=0)
        valor_local = st.text_input(label='Valor de venda para Locais',value=10)

    with col2:
        gramatura_milho = st.text_input(label='Gramatura do Milho', value=500)
        gramatura_açucar = st.text_input(label='Gramatura do Açucar', value=5000)
        gramatura_chocolate = st.text_input(label='Gramatura do Chocolate', value=1010)
        gramatura_ninho = st.text_input(label='Gramatura do Leite em pó', value=400)
        valor_turista = st.text_input(label='Valor de venda para Turistas',value=12)
        submit = st.form_submit_button('Calcular')

    with col3:
        usado_milho = st.text_input(label='Milho na Receita', value=250)
        usado_açucar = st.text_input(label='Açucar na Receita', value=400)
        usado_chocolate = st.text_input(label='Chocolate na Receita', value=330)
        usado_ninho = st.text_input(label='Leite em pó na Receita', value=200)
        quantidade = st.text_input(label='Rendimento da Receita', value=10)

if submit:
    milho = (float(valor_milho) / float(gramatura_milho)) * float(usado_milho)
    açucar = (float(valor_açucar) / float(gramatura_açucar)) * float(usado_açucar)
    chocolate = (float(valor_chocolate) / float(gramatura_chocolate)) * float(usado_chocolate)
    ninho = (float(valor_ninho) / float(gramatura_ninho)) * float(usado_ninho)
    rendimento = float(quantidade)
    resultado = milho + açucar + chocolate + ninho

    milho_receita = milho / rendimento
    açucar_receita = açucar / rendimento
    chocolate_receita = chocolate / rendimento
    ninho_receita = ninho / rendimento
    resultado_receita = resultado / rendimento
    lucro_local = float(valor_local) - resultado_receita
    lucro_turista = float(valor_turista) - resultado_receita

    colu1, colu2 = st.columns(2)
    with colu1:
        st.write(f'Valor do Milho = R$ {milho:.2f}')
        st.write(f'Valor do Açucar = R$ {açucar:.2f}')
        st.write(f'Valor do Chocolate = R$ {chocolate:.2f}')
        st.write(f'Valor do Leite em Pó = R$ {ninho:.2f}')
        st.write(f'Valor da Receita = R$ {resultado:.2f}')
        st.write(f'Lucro venda para Local = R$ {lucro_local:.2f}')


    with colu2:
        st.write(f'Custo do milho em cada pacote = R$ {milho_receita:.2f}')
        st.write(f'Custo do açucar em cada pacote = R$ {açucar_receita:.2f}')
        st.write(f'Custo do chocolate em cada pacote = R$ {chocolate_receita:.2f}')
        st.write(f'Custo do leite em pó em cada pacote = R$ {ninho_receita:.2f}')
        st.write(f'Custo de cada pacote  = R$ {resultado_receita:.2f}')
        st.write(f'Lucro venda para Turista = R$ {lucro_turista:.2f}')
