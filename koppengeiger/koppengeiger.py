# https://webmap.ornl.gov/ogcdown/dataset.jsp?dg_id=10012_1
from os.path import join, abspath, dirname

from rasters import Raster, RasterGeometry

KOPPEN_GEIEGER_FILENAME = join(abspath(dirname(__file__)), "KG_simplified_uint8.tif")

def load_koppen_geiger(geometry: RasterGeometry = None) -> Raster:
    """
    Load the Köppen-Geiger land-cover classification raster.

    This function loads a subset of the Köppen-Geiger land-cover classification raster as a `rasters.Raster` object given a spatial area defined by `rasters.RasterGeometry` object.

    The Köppen-Geiger land-cover classification is a widely used vegetation and climate classification system. More details can be found at https://koppen.earth/.

    Parameters
    ----------
    geometry : RasterGeometry, optional
        The geometry to which the raster should be transformed. If None, the original raster geometry is used.

    Returns
    -------
    Raster
        The loaded Köppen-Geiger land-cover classification raster, potentially transformed to the given geometry.

    References
    ----------
    Beck, H. E., Zimmermann, N. E., McVicar, T. R., Vergopolan, N., Berg, A., & Wood, E. F. (2018). Present and future Köppen-Geiger climate classification maps at 1-km resolution. Scientific Data, 5, 180214.
    """
    koppen_geiger = Raster.open(KOPPEN_GEIEGER_FILENAME)

    if geometry is not None:
        koppen_geiger = koppen_geiger.to_geometry(geometry)

    return koppen_geiger
