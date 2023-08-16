from src.setup import Config
from datetime import datetime
from datetime import timedelta
from src.models.news import News
from src.resources.ny_times_resources import NYTimesResources
from RPA.Browser.Selenium import By
import time
import requests

class NYTimesScrapper:

    url = NYTimesResources.URL

    def __init__(self, browser, config: Config):
        self.browser = browser
        self.config = config
        self.logger = config.logger

    def open_page(self):
        self.logger.info(f'Opening page {self.url}')
        self.browser.open_available_browser(self.url)
    
    def remove_compliance_overlay(self):
        """Remove compliance overlay if it exists"""
        try:
            self.logger.info('Removing compliance overlay')
            self.browser.click_button_when_visible(NYTimesResources.COMPLIANCE_OVERLAY_BUTTON)
            self.browser.wait_until_element_is_not_visible(NYTimesResources.COMPLIANCE_OVERLAY)
        except:
            self.logger.info('Compliance overlay not found')
            pass

    def search(self):
        self.logger.info(f'Searching for {self.config.SEARCH_FRASE}')
        self.browser.click_button_when_visible(NYTimesResources.SEARCH_BUTTON)
        self.browser.input_text_when_element_is_visible(NYTimesResources.SEARCH_INPUT, self.config.SEARCH_FRASE)
        self.browser.press_keys(NYTimesResources.SEARCH_INPUT, 'ENTER')

    def select_sections(self):
        self.logger.info(f'Selecting sections {self.config.SECTIONS}')
        self.browser.click_button_when_visible(NYTimesResources.SELECT_SECTIONS)
        for section in self.config.SECTIONS:
            self.browser.click_element_if_visible(f'xpath://input[contains(@value, "{section}")]')
        

    def sort_by_newest(self):
        self.logger.info('Sorting articles by newest')
        self.browser.click_element_when_visible(NYTimesResources.SORT_BY)
        self.browser.click_element_when_visible(NYTimesResources.SORT_BY_NEWEST)

    def select_date_range(self):
        self.logger.info(f'Selecting date range {self.config.MONTHS} months')
        start_date = (datetime.now() - timedelta(days=int(self.config.MONTHS) * 30)).strftime('%m/%d/%Y')
        end_date = datetime.now().strftime('%m/%d/%Y')
        self.browser.click_button_when_visible(NYTimesResources.DATES_DROPDOWN)
        self.browser.click_button_when_visible(NYTimesResources.SPECIFC_DATES)
        self.browser.input_text_when_element_is_visible(NYTimesResources.START_DATE, start_date)
        self.browser.input_text_when_element_is_visible(NYTimesResources.END_DATE, end_date)
        self.browser.press_keys(NYTimesResources.END_DATE, 'ENTER')

    def download_images(self, article, title):
        try:
            self.logger.info('Downloading image from article' + title)
            image = article.find_element(By.CLASS_NAME, NYTimesResources.IMAGE_CLASS).get_attribute('src')
            image_url = image.split('?')[0]
            file_name = image_url.split('/')[-1]
            with open(f'output/{file_name}', 'wb') as f:
                f.write(requests.get(image_url).content)
            return file_name
        except:
            self.logger.info('Image not found')
            return None
        
            

    def get_news(self):
        """Get news from the page"""
        news: list[News] = []
        self.logger.info('Getting news from the page')
        articles = self.browser.get_webelements(NYTimesResources.ARTICLES)
        for article in articles:
            title = article.find_element(By.CLASS_NAME, NYTimesResources.ARTICLE_TITLE_CLASS).text
            news.append(News(
                title = title,
                description = article.find_element(By.CLASS_NAME, NYTimesResources.ARTICLE_DESCRIPTION_CLASS).text,
                date = article.find_element(By.CLASS_NAME, NYTimesResources.ARTICLE_DATE_CLASS).text,
                search_phrase=self.config.SEARCH_FRASE,
                image=self.download_images(article, title)
            ))
        return news
    
    def run_flow(self) -> list[News]:
        try:
            self.logger.info('Running the entire flow to get news/articles')
            self.open_page()
            self.remove_compliance_overlay()
            self.search()
            self.select_date_range()
            self.select_sections()
            self.sort_by_newest()
            time.sleep(2)
            return self.get_news()
        except Exception as e:
            self.logger.error(f'Error while running the flow: {e}')
            return []
