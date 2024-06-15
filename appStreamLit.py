
from groq import Groq
import streamlit as st
import os
import pandas as pd
import re
import difflib

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image('novalogo.png',width=200)
    st.title("ToolAI")

#groq
GROQ_API_KEY = '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'


client = Groq(
    api_key=GROQ_API_KEY,
)
datos = {
    "Kit de Bricolaje": [
        "Kit de reparación del hogar",
        "Kit de pintura para principiantes",
        "Kit de carpintería básico",
        "Kit de jardinería",
        "Kit de electricidad doméstica",
        "Kit de costura",
        "Kit de fontanería",
        "Kit de reparación de bicicletas",
        "Kit de manualidades",
        "Kit de reparación de muebles"
    ],
    "Herramientas": [
        "Martillo, destornillador, alicates",
        "Brochas, rodillos, cinta de pintor",
        "Sierra, clavos, escuadra",
        "Tijeras de podar, guantes, rastrillo",
        "Destornillador, pelacables, multímetro",
        "Agujas, hilo, tijeras",
        "Llave inglesa, cinta de teflón, soplete",
        "Llave Allen, bomba de aire, parches",
        "Tijeras, pegamento, papel de colores",
        "Lija, cera, trapos"
    ]
}


datos2 = {
    "Herramienta": [
        "Martillo",
        "Destornillador",
        "Alicates",
        "Brochas",
        "Rodillos",
        "Cinta de pintor",
        "Sierra",
        "Clavos",
        "Escuadra",
        "Tijeras de podar",
        "Guantes",
        "Rastrillo",
        "Destornillador",
        "Pelacables",
        "Multímetro",
        "Agujas",
        "Hilo",
        "Tijeras",
        "Llave inglesa",
        "Cinta de teflón",
        "Soplete",
        "Llave Allen",
        "Bomba de aire",
        "Parches",
        "Tijeras",
        "Pegamento",
        "Papel de colores",
        "Lija",
        "Cera",
        "Trapos"
    ],
    "Proveedor": [
        "Proveedor1",
        "Proveedor2",
        "Proveedor3",
        "Proveedor4",
        "Proveedor5",
        "Proveedor6",
        "Proveedor7",
        "Proveedor8",
        "Proveedor9",
        "Proveedor10",
        "Proveedor11",
        "Proveedor12",
        "Proveedor13",
        "Proveedor14",
        "Proveedor15",
        "Proveedor16",
        "Proveedor17",
        "Proveedor18",
        "Proveedor19",
        "Proveedor20",
        "Proveedor21",
        "Proveedor22",
        "Proveedor23",
        "Proveedor24",
        "Proveedor25",
        "Proveedor26",
        "Proveedor27",
        "Proveedor28",
        "Proveedor29",
        "Proveedor30"
    ],
    "Dirección": [
        "Dirección1",
        "Dirección2",
        "Dirección3",
        "Dirección4",
        "Dirección5",
        "Dirección6",
        "Dirección7",
        "Dirección8",
        "Dirección9",
        "Dirección10",
        "Dirección11",
        "Dirección12",
        "Dirección13",
        "Dirección14",
        "Dirección15",
        "Dirección16",
        "Dirección17",
        "Dirección18",
        "Dirección19",
        "Dirección20",
        "Dirección21",
        "Dirección22",
        "Dirección23",
        "Dirección24",
        "Dirección25",
        "Dirección26",
        "Dirección27",
        "Dirección28",
        "Dirección29",
        "Dirección30"
    ]
}


noEntro= False
noEntro2= False

lista_kits = datos['Kit de Bricolaje']

# Creando el dataframe
herramientas_df = pd.DataFrame(datos)


materiales_compradores_df = pd.DataFrame(datos2)

def find_most_similar_string(main_string, string_list):
    best_match = difflib.get_close_matches(main_string, string_list, n=1)
    return best_match[0] if best_match else None

# print(chat_completion.choices[0].message.content)
system_prompt_1=[
    {"role": "system", "content": 
     '''
     Tienes que clasificar la pregunta del cliente en alguno de estos cuatro campos. Tu objetivo es devolver únicamente uno de esos 4 campos:

     -   "Kit de pintura para principiantes",
     -   "Kit de carpintería básico",
     -   "Kit de manualidades",
     -   "Kit de reparación de muebles"
     '''
     }
]


system_prompt_2=[
    {"role": "system", "content": 
     '''
        A continuación vas a tener una lista de herramientas necesarias.        
        Tu objetivo es tranformamelas a bullet points, y preguntar al usuario que herramientas quiere comprar. Tienes que ser muy friendly. No te inventes nada.

        {lista_herramientas}

     '''
     }
]


system_prompt_3=[
    {"role": "system", "content": 
     '''
        A continuación vas a tener una tabla con proveedores, herramientas, y direcciones.  
        Y pregunta al usuario que proveedor le gusta mas. 
        El formato de la respuesta son bullet points.
        No te inventes nada.

        {lista_herramientas}

     '''
     }
]


system_prompt_4=[
    {"role": "system", "content": 
     '''
        Eres un asistente de bricolaje que se llama ToolAI y le vas a dar las gracias por seleccionar los proveedores de {prompt}.

        Y le vas a ofrecer instrucciones de como construir {prompt_original}.

     '''
     }
]

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hola soy ToolAI, ¿Como te puedo ayudar?"}]


for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    if len(st.session_state.messages)==0:
        global prompt_original 
        prompt_original =  st.session_state.messages[0]
        print('no hemos entrado en nada',prompt_original)

    st.session_state.messages.append({"role": "user", "content": prompt})

    st.chat_message("user").write(prompt)

    print('noEntro',noEntro, 'noEntro2',noEntro2)

    
    if len(st.session_state.messages)<3 and not noEntro:

        system_prompt= system_prompt_1

        
        chat_completion = client.chat.completions.create(
            messages= st.session_state.messages + system_prompt,
            model="llama3-8b-8192",
            temperature=0,
            max_tokens=1024,
            top_p=1,
            stop=None,
            stream=False,
            )

        print('response = chunk.choices[0].delta.content', chat_completion.choices[0].message.content)
        response_message_tipo = chat_completion.choices[0].message.content


        response_message = {"role": "assistant", "content": chat_completion}
        # Use a regular expression to extract the relevant classification
        match = re.search(r'\"(.+?)\"', response_message_tipo)
        if match:
            extracted_string = match.group(1)
        else:
            extracted_string = ""

        print('lista_kits',lista_kits)
        user_kit = find_most_similar_string(extracted_string, lista_kits)
        print('user_kit', user_kit)
        lista_herramientas_bd= herramientas_df[herramientas_df['Kit de Bricolaje']== user_kit]['Herramientas'].to_list()


        system_prompt_2[0]['content'] = system_prompt_2[0]['content'].format(lista_herramientas= lista_herramientas_bd)

        messages_html = system_prompt_2

        print('Le pasamos lo siguiente:', messages_html)

        with st.chat_message("assistant"):
            completion = client.chat.completions.create(
                messages= messages_html,
                model="mixtral-8x7b-32768",
                temperature=0.01,
                max_tokens=1024,
                top_p=1,
                stop=None,
                stream=True,
            )

        full_response = ""  # Initialize outside the generator

        def generate_responses(completion):
            global full_response
            for index, chunk in enumerate(completion):
                response = chunk.choices[0].delta.content or ""
                if response:
                    full_response += response  # Append to the full response
                    yield response

        stream = generate_responses(completion)
        st.write_stream(stream)

        # After streaming
        if full_response:  # Check and use the full_response as needed
            response_message = {"role": "assistant", "content": full_response}
            # with st.chat_message("assistant"):
            #     st.markdown(full_response)
            st.session_state.messages.append(response_message)

        noEntro= True
    elif len(st.session_state.messages)>=3 and len(st.session_state.messages)<5:
        #ya ha elegido el usuario los materiales que quiere con comas, brochas, rodillos
        print('prompt', prompt)
        # Usar una expresión regular para separar por comas o por "y"
        elementos = re.split(r', | y ', prompt)

        # Eliminar espacios adicionales alrededor de cada elemento usando strip()
        user_lista_materiales_aComprar = [elemento.strip().replace('y ','').lower() for elemento in elementos if elemento.strip()]

        materiales_compradores_df['Herramienta'] = materiales_compradores_df['Herramienta'].str.lower()

        materiales_compradores_df['Comprar'] = materiales_compradores_df['Herramienta'].isin(user_lista_materiales_aComprar)

        materiales_compradores_prompt = materiales_compradores_df[materiales_compradores_df['Comprar']==True]
        materiales_compradores_prompt.drop('Comprar')

        # Group by 'proveedor'
        grupo_proveedor = materiales_compradores_prompt.groupby('Proveedor').count()
        system_prompt_3[0]['content'] = system_prompt_3[0]['content'].format(lista_herramientas= grupo_proveedor)



        messages_listaProveedores= system_prompt_3
        noEntro2= True


        print('Le pasamos lo siguiente:', messages_listaProveedores)

        with st.chat_message("assistant"):
            completion = client.chat.completions.create(
                messages= messages_listaProveedores,
                model="mixtral-8x7b-32768",
                temperature=0.01,
                max_tokens=1024,
                top_p=1,
                stop=None,
                stream=True,
            )

        full_response = ""  # Initialize outside the generator

        def generate_responses(completion):
            global full_response
            for index, chunk in enumerate(completion):
                if index==0:
                    direccion="Calle de Fernández de la Hoz, 7, Chamberí, 28003 Madrid"
                    response_intro= f'Hemos detectado que estas en la direccion: {direccion}. A continuación te ponemos los proveedores más cerca: \n'
                    yield response_intro
                response = chunk.choices[0].delta.content or ""
                if response:
                    full_response += response  # Append to the full response
                    yield response

        stream = generate_responses(completion)
        st.write_stream(stream)
        print(len(st.session_state.messages))

        
        # After streaming
        if full_response:  # Check and use the full_response as needed
            response_message = {"role": "assistant", "content": full_response}
            # with st.chat_message("assistant"):
            #     st.markdown(full_response)
            st.session_state.messages.append(response_message)


    elif len(st.session_state.messages)>=4:        #ya ha elegido el usuario los materiales que quiere con comas, brochas, rodillos, sus proveedores, direccion etc
        print('prompt', prompt, 'st.session_state.messages[0]', st.session_state.messages) #TODO
        prompt_original=st.session_state.messages[1]

        system_prompt_4[0]['content'] = system_prompt_4[0]['content'].format(prompt= prompt,prompt_original=prompt_original)


        messages_instrucciones= system_prompt_4

        print('Le pasamos lo siguiente:', messages_instrucciones)

        with st.chat_message("assistant"):
            completion = client.chat.completions.create(
                messages= messages_instrucciones,
                model="mixtral-8x7b-32768",
                temperature=0.01,
                max_tokens=1024,
                top_p=1,
                stop=None,
                stream=True,
            )

        full_response = ""  # Initialize outside the generator

        def generate_responses(completion):
            global full_response
            for chunk in completion:
                response = chunk.choices[0].delta.content or ""
                if response:
                    full_response += response  # Append to the full response
                    yield response

        stream = generate_responses(completion)
        st.write_stream(stream)
        noEntro2= True

        
        # After streaming
        if full_response:  # Check and use the full_response as needed
            response_message = {"role": "assistant", "content": full_response}
            # with st.chat_message("assistant"):
            #     st.markdown(full_response)
            st.session_state.messages.append(response_message)



    # st.chat_message("assistant").write(full_response)