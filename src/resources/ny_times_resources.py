from dataclasses import dataclass

@dataclass
class NYTimesResources:
    URL = 'https://www.nytimes.com/'
    COMPLIANCE_OVERLAY = '//div[@id="complianceOverlay"]'
    COMPLIANCE_OVERLAY_BUTTON = '//div[@id="complianceOverlay"]//div//button'
    SEARCH_BUTTON = '//button[@aria-controls="search-input"]'
    SEARCH_INPUT = '//input[@data-testid="search-input"]'
    SELECT_SECTIONS = '//button[@data-testid="search-multiselect-button"]'
    SORT_BY = '//select[@data-testid="SearchForm-sortBy"]'
    SORT_BY_NEWEST = '//option[@value="newest"]'
    DATES_DROPDOWN = '//button[@data-testid="search-date-dropdown-a"]'
    SPECIFC_DATES = '//button[@aria-label="Specific Dates"]'
    START_DATE = '//input[@id="startDate"]'
    END_DATE = '//input[@id="endDate"]'
    IMAGE_CLASS = 'css-rq4mmj'
    ARTICLES = 'class:css-1l4w6pd'
    ARTICLE_TITLE_CLASS = 'css-2fgx4k'
    ARTICLE_DESCRIPTION_CLASS = 'css-16nhkrn'
    ARTICLE_DATE_CLASS = 'css-17ubb9w'