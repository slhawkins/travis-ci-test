'use strict';

module.exports = {
  'sample test': function(browser) {
    browser
      .url(browser.launch_url)
      .waitForElementVisible('#test', 8000)
    browser.end();
  }
};
