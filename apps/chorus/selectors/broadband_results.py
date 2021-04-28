
not_available: str = "//div[contains(@class, 'not-available')]/following-sibling::div/span"
available: str = "//div[@class='top-label']/following-sibling::div/span"
on_request: str = "//div[contains(@class,'available-on-request')]/following-sibling::div/span"
might_be_available: str = "//div[contains(@class,'might-be-available')]/following-sibling::div/span"
current: str = "//div[contains(@class, 'current-connection')]/following-sibling::div/span"
load_spinner: str = "//div[@class='address-spinner-wrapper' and @style='display: none;']"
