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
        SELECT
          Latitud AS latitud,
          Longitud AS longitud,
          Sitio AS sitio,
          Calle AS calle,
          Estado AS estado,
          Ciudad AS ciudad,
          Colonia AS colonia,
          COUNT(1) AS total_atms,
          COUNTIF(status=false) AS total_atms_falla
        FROM (
          WITH
          my_location AS (SELECT ST_GEOGPOINT({longitud}, {latitud}) AS point),
          atms_geo AS (
            SELECT *, ST_GEOGPOINT(Longitud,Latitud) AS latlon_geo
            FROM rocket.atms
          ),
          failed_atms AS (
            SELECT ATM_ID
            FROM rocket.issues
            WHERE FECHA_INICIO < '{fecha.strftime('%Y-%m-%d %H:%M:%S')}'
            AND '{fecha.strftime('%Y-%m-%d %H:%M:%S')}' < FECHA_FIN
            GROUP BY ATM_ID
          )
          SELECT
            atms_geo.*,
            IF(fatms.ATM_ID IS NULL, true, false) AS status
          FROM my_location, atms_geo
          LEFT JOIN failed_atms fatms ON fatms.ATM_ID = atms_geo.ATM
          WHERE ST_DWITHIN(my_location.point, atms_geo.latlon_geo, {radio})
        ) AS atm_status
        GROUP BY latitud, longitud, sitio, calle, estado, ciudad, colonia
        '''
    ).mappings().all()
    return [
        Atm(**atm) for atm in atms
    ]
