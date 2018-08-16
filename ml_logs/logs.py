import logging
import timber

from ml_logs import env

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

timber_handler = timber.TimberHandler(api_key=env.TIMBER_API_KEY, level=logging.INFO)
logger.addHandler(timber_handler)
