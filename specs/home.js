'use strict';

module.exports = {
  'sample test': function(browser) {
    browser
      .url(browser.launch_url)
      .waitForElementVisible('#test', 1000)
      .expect.element('#test')
      .text.to.equal('');
    browser.end();
  }
};
