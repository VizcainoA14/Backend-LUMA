from pydantic import BaseModel


class DataStructure(BaseModel):
    index: int
    date: str
    url: str
    entropy: float
    mean_intensity: float
    standard_deviation: float
    skewness: float
    kurtosis: float
    relative_smoothness: float
    uniformity: float
    fractal_dimension: float
    taruma_contrast: float
    taruma_directionality: float
    taruma_coarseness: float
    taruma_linelikeness: float
    taruma_regularity: float
    taruma_roughness: float