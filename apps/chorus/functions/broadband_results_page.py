from typing import List

from apps.chorus.selectors import broadband_results as _sel
from playwright.sync_api import Page


class ResultsPage:

    page: Page

    def __init__(self, page: Page):
        self.page = page

    def get_available_options(self) -> List[str]:
        self.page.wait_for_load_state(state='domcontentloaded')
        self.page.wait_for_selector(_sel.load_spinner, state='attached')
        self.page.wait_for_selector(_sel.available, state='attached', timeout=5000)
        available = self._get_collection_text(_sel.available)
        current = self._get_collection_text(_sel.current)
        return available + current

    def _get_collection_text(self, selector: str) -> List[str]:
        collection = self.page.query_selector_all(selector)
        new_collection: List[str] = []
        for each in collection:
            new_collection.append(each.text_content().strip())
        return new_collection
