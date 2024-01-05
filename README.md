This is a mini project to explore selenium's waiting features in combination with Django.

The functional tests show that in websites with elements in non viewable parts of the site no scrolling down and waiting is (any more) necessary for these elements to be found by selenium (see test_do_not_scroll_and_do_not_wait).

The tests use the headless option of the chrome driver. You can set the env var HEADLESS to False to be able to see the browser in action (export HEADLESS=False). 

Two simple demo sites are created with Django:

http://localhost:8000/demo-scrolldown
<br>
Django creates a html file with 500000 lines (!) and a 'click me!' link at the very bottom of the site. Selenium clicks this link and is forwarded to a rudimentary site under http://localhost:8000/demo-success with the title 'demo success' which can be verified inside tests.

http://localhost:8000/demo-element-load
<br>
At the core of this site sits a simple jQuery script that creates a timer counting up to 5 before creating a save input button.

All tests are also run as a CI workflow using GitHub Actions and pytest. (see .github/workflows/python-app.yml)
