from dotenv import load_dotenv
from os import getenv
from loguru import logger as log
from datetime import datetime
from RPA.Robocorp.WorkItems import WorkItems

load_dotenv()
ENV = getenv('ENV', 'PROD')
class Config:
    SEARCH_FRASE = None
    SECTIONS = None
    MONTHS = None
    FILE_NAME = None
    logger = None
    
    def __init__(self, logger=None):
        self.logger = logger or log
        current_timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.logger.add('logs/{}.log'.format(current_timestamp), retention='10 days')
        if ENV == 'dev':
            self.setup_with_env()
            self.logger.info('Config initialized in dev mode')
        else:
            try:
                work_items = WorkItems()
                work_items.get_input_work_item()
                self.SEARCH_FRASE = work_items.get_work_item_variable('SEARCH_PHRASE', 'Bitcoin')
                self.SECTIONS = [section.strip() for section in  work_items.get_work_item_variable('SECTIONS', 'Business').split(',')]
                self.MONTHS = work_items.get_work_item_variable('MONTHS', 2)
                self.FILE_NAME = work_items.get_work_item_variable('FILE_NAME', 'report')
                self.logger.info('Config initialized in prod mode')
            except Exception as e:
                self.logger.error('Config initialization error: {}'.format(e))
                self.setup_with_env()
                self.logger.info('Config initialized in dev mode due to error')

    def setup_with_env(self):
        self.SEARCH_FRASE = self.get_from_env('SEARCH_PHRASE', 'Bitcoin')
        self.SECTIONS = [section.strip() for section in  self.get_from_env('SECTIONS', 'Arts, Business').split(',')]
        self.MONTHS = self.get_from_env('MONTHS', 2)
        self.FILE_NAME = self.get_from_env('FILE_NAME', 'news')
        self.logger.info('Config initialized with env variables')

    def get_from_env(self, name, default=None):
        return getenv(name, default)
    