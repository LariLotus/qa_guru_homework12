"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene.support.shared import browser


@pytest.fixture(params=[(1920, 1080), (1600, 1200)])
def web_browser_for_desktop(request):
    browser.open('https://github.com')
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield browser
    browser.quit()


@pytest.fixture(params=[(360, 740), (740, 360)])
def web_browser_for_mobile(request):
    browser.open('https://github.com')
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield browser
    browser.quit()


def test_github_desktop(web_browser_for_desktop):
    browser.open('https://github.com')
    browser.element('[href="/login"]').click()


def test_github_mobile(web_browser_for_mobile):
    browser.open('https://github.com')
    browser.element('[class="Button-content"]').click()
    browser.element('[href="/login"]').click()
