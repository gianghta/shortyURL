from .base import Base

# Import all models, so that Base has
# them before being imported by Alembic
from models import models
