from RPA.Browser.Selenium import Selenium
from src.services.ny_times_scrapper import NYTimesScrapper
from src.setup import Config
import time
from src.services.csv_parser import CSVParser

def main():
    config = Config()
    ny_times_scrapper = NYTimesScrapper(Selenium(), config)
    news = ny_times_scrapper.run_flow()
    csv_parser = CSVParser(config.FILE_NAME, config.logger)
    csv_parser.generate_csv(news)

if __name__ == '__main__':
    main()