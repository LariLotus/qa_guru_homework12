"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene.support.shared import browser


@pytest.fixture(params=[(1920, 1080), (360, 740), (1600, 1200), (740, 360)])
def browser_open(request):
    browser.open('https://github.com')
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield browser
    browser.quit()


@pytest.mark.parametrize('browser_open', [(1920, 1080), (1600, 1200)], indirect=True)
def test_github_desktop(browser_open):
    browser.open('https://github.com')
    browser.element('[href="/login"]').click()


@pytest.mark.parametrize('browser_open', [(360, 740), (740, 360)], indirect=True)
def test_github_mobile(browser_open):
    browser.open('https://github.com')
    browser.element('[class="Button-content"]').click()
    browser.element('[href="/login"]').click()
