import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("astronauts.csv")

df['Year'] = pd.to_numeric(df['Year'], errors="coerce")


df['Group'] = pd.to_numeric(df['Group'], errors="coerce")

df['Birth Date'] = pd.to_datetime(df['Birth Date'], format="%m/%d/%y", errors="coerce")

df[['Birth_city', 'Birth_state']] = (
        df['Birth Place']
        .str.split(';', n=1, expand=True)
        .fillna("")
        .apply(lambda col: col.str.strip())
                )
df['Birth_country'] = df['Birth_state'].apply(
        lambda x: "USA" if len(x) <= 2 else x
        )

df['Birth_state'] = df['Birth_state'].apply(
    lambda x: x if len(x) <= 2 else ""
)


df[['Ugrad_school', 'Grad_school']] = (
df['Alma Mater']
    .str.split(";", n=1, expand=True)

    .fillna("")

    .apply(lambda col: col.str.strip())
    )
df['Grad_school'] = df['Grad_school']
df['Military Rank'] = df['Military Rank'].fillna('Non-Military')
df['Military Branch'] = df['Military Branch'].fillna('Non-military')
df['Missions'] = (
df['Missions']
    .fillna("No missions")
    .str.replace(';',',',regex=False)
    .str.replace('/',',', regex=False)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
    )
User = "Your_user"
Password = "Your_password"
Host = "Your_HOST"
Port = "Your_port"
Database = "Your_db"

df = df.drop(columns=['Birth Place','Alma Mater'])
url = f"mysql+pymysql://{User}{Password}{Host}:{Port}/{Database}"
engine = create_engine(url)
df.to_sql(
    "my_clean_data7",
    con = engine,
    if_exists="replace",
    index=False

)