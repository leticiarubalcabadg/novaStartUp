
from groq import Groq
import streamlit as st
import os
import pandas as pd
import re
import difflib

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image('toolAI2.png',width=200)
    st.title("ToolAI")

# st.subheader("Pregunta sobre pintar tu casa, carpintería, manualidades, o reparar muebles ")
st.markdown("<h4 style='text-align: center;'>¿Te gustaría alquilar pintura para tu casa, herramientas de carpintería, o de manualidades?</h4>", unsafe_allow_html=True)


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
        "Herrerías López",
        "Ferretería El Tornillo",
        "Distribuidora Ferrum",
        "Industrial Martínez",
        "Proveedora Eléctrica",
        "Construcciones Rodri",
        "Materiales Ponce",
        "Accesorios Hnos. García",
        "Suministros Alborada",
        "Herramientas Vega",
        "Proveedores del Norte",
        "Comercializadora Sur",
        "Refacciones del Centro",
        "Equipos y Más",
        "Ferretería del Este",
        "Tecnologías Herrera",
        "Productos Acme",
        "Insumos Perla",
        "Accesorios y Equipos",
        "Soluciones Industriales",
        "Proveedora Central",
        "Distribuciones Galicia",
        "Equipos Monarca",
        "Herramientas Europa",
        "Materiales Anáhuac",
        "Distribuciones Orion",
        "Suministros Premier",
        "Proveedora Total",
        "Materiales y Más",
        "Ferretería Milenio"
    ],
    "Dirección": [
        "Av. Principal 123",
        "Calle Secundaria 456",
        "Carrera Tercera 789",
        "Bulevar Central 101",
        "Avenida Sur 202",
        "Calle Norte 303",
        "Calle Este 404",
        "Calle Oeste 505",
        "Paseo de la Reforma 606",
        "Callejón del Norte 707",
        "Plaza del Sol 808",
        "Avenida del Mar 909",
        "Calle de los Robles 1010",
        "Calle de los Pinos 1111",
        "Avenida del Valle 1212",
        "Calle de las Rosas 1313",
        "Camino Real 1414",
        "Carretera Vieja 1515",
        "Paseo del Lago 1616",
        "Camino del Bosque 1717",
        "Callejón del Rio 1818",
        "Avenida del Parque 1919",
        "Calle de la Montaña 2020",
        "Bulevar del Norte 2121",
        "Calle de las Lomas 2222",
        "Avenida de los Olivos 2323",
        "Camino de la Sierra 2424",
        "Paseo del Prado 2525",
        "Calle de las Flores 2626",
        "Avenida de los Arcos 2727"
    ],
        "Minutos": [
        15, 10, 5, 20, 25,
        5, 30, 5, 10, 15,
        5, 20, 10, 15, 30,
        5, 5, 5, 10, 5,
        10, 5, 10, 5, 5,
        10, 5, 10, 5, 5
    ]
}


data_videos = {
    "Kit": [
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
    "Video de YouTube": [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "https://www.youtube.com/watch?v=oHg5SJYRHA0",
        "https://www.youtube.com/watch?v=2Z4F4fzaJcA",
        "https://www.youtube.com/watch?v=DIYtLMR7g50",
        "https://www.youtube.com/watch?v=1D4MJC1JNbU",
        "https://www.youtube.com/watch?v=djv6hM7_aVI",
        "https://www.youtube.com/watch?v=rZz2-tpK8aM",
        "https://www.youtube.com/watch?v=H6ALv6vKJb8",
        "https://www.youtube.com/watch?v=PxXZONnSoK4",
        "https://www.youtube.com/watch?v=kXYiU_JCYtU"
    ]
}



noEntro= False
noEntro2= False

lista_kits = datos['Kit de Bricolaje']

# Creando el dataframe
herramientas_df = pd.DataFrame(datos)


materiales_compradores_df = pd.DataFrame(datos2)

youtube_videos = pd.DataFrame(data_videos)

def find_most_similar_string(main_string, string_list):
    best_match = difflib.get_close_matches(main_string, string_list, n=1)
    return best_match[0] if best_match else None

# print(chat_completion.choices[0].message.content)
system_prompt_1=[
    {"role": "system", "content": 
     '''
     Tienes que clasificar la pregunta del cliente en alguno de estos cuatro campos. Tu objetivo es devolver únicamente uno de esos 4 campos entre doble comillas:

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
        Tu objetivo es mostrarmelas on guiones , y preguntar al usuario que herramientas quiere comprar. Tienes que ser muy servicial. 
        No te inventes nada y hablame en español.

        {lista_herramientas}

     '''
     }
]


system_prompt_3=[
    {"role": "system", "content": 
     '''
        A continuación vas a tener una tabla con proveedores, herramientas, direcciones, y cuantos minutos tarda en llegar.
        Muestrame la información agrupada por proveedores y pregunta al usuario que proveedor le gusta mas. 
        El formato de la respuesta son bullet points con emojis..
        No te inventes nada y hablame en español.

        {lista_herramientas}

     '''
     }
]


system_prompt_4=[
    {"role": "system", "content": 
     '''
        Eres un asistente de bricolaje que se llama ToolAI y le vas a dar las gracias por seleccionar los proveedores de {prompt}.

        Y le vas a ofrecer instrucciones de como construir {prompt_original}. Utiliza emojis.

     '''
     }
]

        # Y dependiendo de lo que necesita el usuario({prompt_original}) elige algunos de estos videos:

        # - Para colgar un cuadro: https://www.youtube.com/watch?v=hXcqBeZKBvk
        # - Para hacer manualidades: https://www.youtube.com/watch?v=Ct3xVwaUtXI
        # - Pintar la pared: https://www.youtube.com/watch?v=Bw0B0-wS9cs


system_prompt_5=[
    {"role": "system", "content": 
     '''
        Eres un asistente de bricolaje que se llama ToolAI ya le has mandado a los proveedores toda la información necesaria sobre el pedido.
        Recuerdale al usuario que para empezar de nuevo el proceso tiene que refrescar la página, y que su pedido esta ya en camino.

        Ahora ya te puede preguntar todo lo que el usuario quiera
        

     '''
     }
]



if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hola soy ToolAI, ¿Como te puedo ayudar?"}]


for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

global user_kit
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

        # After streaming
        # if True:  # Check and use the full_response as needed
        #     response_message = {"role": "system", "content": response_message_tipo}
        #     st.session_state.messages.append(response_message)

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
        print('len(st.session_state.messages',len(st.session_state.messages))
    elif len(st.session_state.messages)>=3 and len(st.session_state.messages)<5:
        #ya ha elegido el usuario los materiales que quiere con comas, brochas, rodillos
        print('prompt', prompt)
        # Usar una expresión regular para separar por comas o por "y"
        elementos = re.split(r', | y ', prompt)

        # Eliminar espacios adicionales alrededor de cada elemento usando strip()
        user_lista_materiales_aComprar = [elemento.strip().replace('y ','').lower() for elemento in elementos]
        print('user_lista_materiales_aComprar',user_lista_materiales_aComprar)

        materiales_compradores_df['Herramienta'] = materiales_compradores_df['Herramienta'].str.lower()

        materiales_compradores_df['Comprar'] = materiales_compradores_df['Herramienta'].isin(user_lista_materiales_aComprar)

        materiales_compradores_prompt = materiales_compradores_df[materiales_compradores_df['Comprar']==True]
        try:
            materiales_compradores_prompt.drop(columns=['Comprar'], inplace=True) 
        except:
            print('no existe compra')

        # Group by 'proveedor'
        # grupo_proveedor = materiales_compradores_prompt.groupby('Proveedor').count()
        grupo_proveedor= materiales_compradores_prompt
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
                    response_intro= f'Hemos detectado que estas en la direccion: {direccion} \n'
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


    elif len(st.session_state.messages)>4 and len(st.session_state.messages)<7:        #ya ha elegido el usuario los materiales que quiere con comas, brochas, rodillos, sus proveedores, direccion etc
        print('st.session_state.messages',st.session_state.messages)
        prompt_original=st.session_state.messages[1]['content']  

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
    
    else:

        with st.chat_message("assistant"):
            completion = client.chat.completions.create(
                messages= st.session_state.messages + system_prompt_5,
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