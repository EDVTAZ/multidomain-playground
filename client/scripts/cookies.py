from playwright.sync_api import sync_playwright


def show_js_cookies(location, page):
    print(f"Cookies from JS {location}: {page.evaluate('document.cookie')}")


with sync_playwright() as playwright:
    context = playwright.chromium.launch_persistent_context(
        "/tmp",
        headless=True,
        devtools=True,
    )

    page = context.new_page()
    page.goto("https://a.com/cookies")
    page.wait_for_load_state("domcontentloaded")
    print(f"Cookies after 1st page load:\n{context.cookies()}")

    page.evaluate(
        """
async () => {
    data = JSON.stringify([{key: "general", value: "kenobi", domain: "a.com"},{key: "hello", value: "there"},{key: "no", value: "way", domain: "b.com"}])
    await fetch('https://a.com/cookies', {method: "POST", headers: {"Content-Type": "application/json"}, body: data})
}
"""
    )
    page.reload()
    page.wait_for_load_state("domcontentloaded")
    print(f"Cookies after fetch load:\n{context.cookies()}")
    page.screenshot(path="screenshot.png", full_page=True)

    show_js_cookies("on a.com", page)

    page.goto("https://sub1.a.com/cookies")
    page.wait_for_load_state("domcontentloaded")
    show_js_cookies("on sub1.a.com", page)

    page.goto("https://b.com/cookies")
    page.wait_for_load_state("domcontentloaded")
    show_js_cookies("on b.com", page)
