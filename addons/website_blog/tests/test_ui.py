import openerp.addons.website.tests.test_ui as test_ui,full_path

def load_tests(loader, base, _):
    base.addTest(test_ui.WebsiteUiSuite(full_path(__file__,'post_test.js'),   { 'action': 'website.action_website_homepage' }, 60.0))
    return base