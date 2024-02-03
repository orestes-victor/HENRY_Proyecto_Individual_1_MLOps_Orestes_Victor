from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()
    
#1° Endpoint________________________________________________________________________________________________________________________________________________________________________________
    
def developer(dataframe, desarrollador):
    df_desarrollador = dataframe[dataframe['developer'] == desarrollador]
    stats_por_anio = df_desarrollador.groupby('release_anio').agg({
        'items_free': 'sum',
        'items_total': 'sum',
        'percentage_free': lambda x: (pd.to_numeric(x.str.rstrip('%'), errors='coerce') / 100).mean() * 100
    }).reset_index()
    stats_por_anio['percentage_free'] = stats_por_anio['percentage_free'].round(2)
    stats_por_anio = stats_por_anio.rename(columns={'release_anio': 'Año'})
    stats_por_anio = stats_por_anio.rename(columns={'items_total': 'Items'})
    stats_por_anio = stats_por_anio.rename(columns={'percentage_free': '% Free'})
    return stats_por_anio[['Año', 'Items', '% Free']]
#get_stats_por_desarrollador

@app.get("/developer/{desarrollador}")
async def get_developer(desarrollador: str):
    try:
        parquet_path = "C:/Users/Usuario/Desktop/Bootcamp_HENRY/HENRY_Proyecto_Individual_1_MLOps_Orestes_Victor/Datasets/dataset_endpoint_1.parquet"
        df = pd.read_parquet(parquet_path)
        result = developer(df, desarrollador)
        return result.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la solicitud: {str(e)}")


#2° Endpoint________________________________________________________________________________________________________________________________________________________________________________

def userdata(df, user_id):
    usuario = df[df['user_id'] == user_id]

    if usuario.empty:
        raise HTTPException(status_code=404, detail=f"El usuario {user_id} no existe en el DataFrame.")

    dinero_gastado = usuario['cantidad total gastado'].iloc[0]
    porcentaje_recomendacion = float(usuario['percentage_true'].iloc[0].rstrip('%'))
    cantidad_items = usuario['item_id'].nunique()

    resultado = {
        "Usuario": user_id,
        "Dinero gastado": f"${dinero_gastado:.2f} USD",
        "% de recomendación": f"{porcentaje_recomendacion:.2f}%",
        "Cantidad de items": cantidad_items
    }

    return resultado

@app.get("/userdata/{user_id}")
async def get_user_id(user_id: str, file_path: str = 'C:/Users/Usuario/Desktop/Bootcamp_HENRY/HENRY_Proyecto_Individual_1_MLOps_Orestes_Victor/Datasets/dataset_endpoint_2.parquet'):
    try:
        # Lee el DataFrame desde el archivo Parquet
        df = pd.read_parquet(file_path)
        
        # Llama a la función userdata
        result = userdata(df, user_id)
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


#3° Endpoint________________________________________________________________________________________________________________________________________________________________________________

def UserForGenre(genre: str, df):
    df['release_anio'] = pd.to_numeric(df['release_anio'], errors='coerce', downcast='integer')
    genre_df = df[df['genres'] == genre]
    genre_df['playtime_forever'] = (genre_df['playtime_forever'] / 60 / 60).astype(int)
    max_playtime_user = genre_df.loc[genre_df['playtime_forever'].idxmax(), 'user_id']
    yearly_playtime = genre_df.groupby('release_anio')['playtime_forever'].sum().reset_index()
    playtime_list = [{'Año': int(year), 'Horas': int(hours)} for year, hours in zip(yearly_playtime['release_anio'], yearly_playtime['playtime_forever'])]
    result = {"Usuario con más horas jugadas para género " + genre: max_playtime_user, "Horas jugadas": playtime_list}
    return result

@app.get("/user_for_genre/{genre}")
async def get_user_for_genre(genre: str, file_path: str = 'C:/Users/Usuario/Desktop/Bootcamp_HENRY/HENRY_Proyecto_Individual_1_MLOps_Orestes_Victor/Datasets/dataset_endpoint_3.parquet'):
    try:
        df = pd.read_parquet(file_path)
        result = UserForGenre(genre, df)
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


#4° Endpoint________________________________________________________________________________________________________________________________________________________________________________

def best_developer_year(dataframe, year):
    df_year = dataframe[dataframe['release_anio'] == year]
    df_filtered = df_year[df_year['sentiment_analysis'] == 2]
    df_grouped = df_filtered.groupby('developer')['sentiment_analysis'].sum().reset_index()
    df_sorted = df_grouped.sort_values(by='sentiment_analysis', ascending=False)
    top_developers = df_sorted.head(3)
    result = [{"Puesto {}: {}".format(i+1, row['developer']): row['sentiment_analysis']} for i, (_, row) in enumerate(top_developers.iterrows())]
    return result

@app.get("/best_developer_year/{year}")
async def get_best_developer_year(year: int, file_path: str = 'C:/Users/Usuario/Desktop/Bootcamp_HENRY/HENRY_Proyecto_Individual_1_MLOps_Orestes_Victor/Datasets/dataset_endpoint_4.parquet'):
    try:
        df = pd.read_parquet(file_path)
        result = best_developer_year(df, year)
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


#5° Endpoint________________________________________________________________________________________________________________________________________________________________________________

def developer_reviews_analysis(df, desarrolladora):
    filtered_data = df[df['developer'] == desarrolladora]
    positive_count = 0
    negative_count = 0

    for sentiment in filtered_data['sentiment_analysis']:
        if sentiment == 0:
            negative_count += 1
        elif sentiment == 2:
            positive_count += 1

    result = {desarrolladora: [f"Negative = {negative_count}", f"Positive = {positive_count}"]}
    return result

@app.get("/developer_reviews_analysis/{desarrolladora}")
async def get_developer_reviews_analysis(desarrolladora: str, file_path: str = 'C:/Users/Usuario/Desktop/Bootcamp_HENRY/HENRY_Proyecto_Individual_1_MLOps_Orestes_Victor/Datasets/dataset_endpoint_5.parquet'):
    try:
        df = pd.read_parquet(file_path)
        result = developer_reviews_analysis(df, desarrolladora)
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
