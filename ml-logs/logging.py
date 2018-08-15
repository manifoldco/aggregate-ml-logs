import logging
import timber

logger = logging.getLogger(__name__)

timber_handler = timber.TimberHandler(api_key='...')
logger.addHandler(timber_handler)
