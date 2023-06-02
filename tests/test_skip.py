"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, be


@pytest.fixture(
    params=[(1920, 1080), (1600, 1200), (360, 740), (740, 360)],

    ids=['desktop', 'desktop', 'mobile', 'mobile'],
)
def browser_open(request):
    browser.open('https://github.com')
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    if request.param[2] == 'desktop':
        is_desktop = True
    else:
        is_desktop = False

    yield is_desktop
    browser.quit()


def test_github_desktop(browser_open):
    if not browser_open:
        pytest.skip(reason='Пропускаем, тест для мобильного')
    browser.open('https://github.com')
    browser.element('[href="/login"]').click()


def test_github_mobile(browser_open):
    if browser_open:
        pytest.skip(reason='Пропускаем, тест для desktop')
    browser.open('https://github.com')
    browser.element('[class="Button-content"]').click()
    browser.element('[href="/login"]').click()
