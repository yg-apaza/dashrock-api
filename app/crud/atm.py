from typing import List
from sqlalchemy.orm import Session
from datetime import datetime

from app.schemas.atm import Atm


def get_nearby(
    db: Session,
    latitud: float, longitud: float, radio: float, fecha: datetime
) -> List[Atm]:
    atms = db.execute(
        f'''
        WITH
        my_location AS (SELECT ST_GEOGPOINT({longitud}, {latitud}) AS point),
        atms_geo AS (
            SELECT *, ST_GEOGPOINT(Longitud,Latitud) AS latlon_geo
            FROM rocket.atms
        ),
        failed_atms as (
            SELECT ATM_ID
            FROM rocket.issues
            WHERE FECHA_INICIO < "{fecha.strftime('%Y-%m-%d %H:%M:%S')}"
            AND "{fecha.strftime('%Y-%m-%d %H:%M:%S')}" < FECHA_FIN
            GROUP BY ATM_ID
        )
        SELECT
            atms_geo.*,
            IF(fatms.ATM_ID IS NOT NULL, true, false) AS status,
            ST_DISTANCE(my_location.point, atms_geo.latlon_geo) AS metros
        FROM my_location, atms_geo
        LEFT JOIN failed_atms fatms ON fatms.ATM_ID = atms_geo.ATM
        WHERE ST_DWITHIN(my_location.point, atms_geo.latlon_geo, {radio});
        '''
    ).mappings().all()
    return [
        Atm(
            atm_id=atm.get('ATM'),
            latitud=atm.get('Latitud'),
            longitud=atm.get('Longitud'),
            status=atm.get('status'),
            sitio=atm.get('Sitio'),
            calle=atm.get('Calle'),
            estado=atm.get('Estado'),
            ciudad=atm.get('Ciudad'),
            colonia=atm.get('Colonia'),
        ) for atm in atms
    ]
