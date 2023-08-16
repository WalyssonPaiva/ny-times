from src.models.news import News
import pandas
from dataclasses import asdict

class CSVParser:

    def __init__(self, filename, logger):
        self.filename = filename
        self.logger = logger
    
    def generate_csv(self, data: list[News]):
        try:
            self.logger.info(f'Generating CSV file for {self.filename}')
            df = pandas.DataFrame([asdict(news) for news in data])
            df.to_csv(f'output/{self.filename}.csv', index=False)
            self.logger.info(f'CSV file generated for {self.filename}')
        except Exception as e:
            self.logger.error(f'Error generating CSV file for {self.filename}')
            self.logger.error(e)
        
